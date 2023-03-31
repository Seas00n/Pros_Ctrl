//本文件定义了一个串口类
#ifndef SERIAL_H
#define SERIAL_H

#include "Stream.hpp"
#include "Timestamp.hpp"
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <pthread.h>

//串口类
class Serial
{

public:
    //无校验
    static const int PARITY_NONE=0;
    //奇校验
    static const int PARITY_ODD=1;
    //偶校验
    static const int PARITY_EVEN=2;
    //函数成功
    static const int OK=1;
    //设备未找到
    static const int DEV_NOT_FOUND=-1;
    //不支持该波特率
    static const int BAUD_NOT_SUPPORTED=-2;
    //不支持该数据位数
    static const int DATABITS_NOT_SUPPORTED=-3;
    //不支持该校验模式
    static const int PARITYMODE_NOT_SUPPORTED=-4;
    //不支持该停止位数
    static const int STOPBITS_NOT_SUPPORTED=-5;
    //未知配置错误
    static const int CONFIG_FAIL=-6;
    //创建线程出错
    static const int NEW_THREAD_FAIL=-7;
    //成功读到结尾符
    static const int READ_END=1;
    //读取超时
    static const int READ_TIMEOUT=-1;
    //读取时缓冲区满
    static const int READ_BUFFER_FULL=-2;

private:
    //串口设备文件描述符
    int fd;
    //字符流
    Stream stream;
    //后台接收线程
    pthread_t tid;
    //对字符流加的锁
    pthread_mutex_t mutex;

public:
    Serial();
    ~Serial();
    //开启串口，参数为：设备名、波特率、数据位数、校验模式、停止位数，返回函数执行结果
    int open(const char* dev,int baud,int dataBits,int parityMode,int stopBits);
    //关闭串口
    int close();
    //写串口，参数为：数据、长度，返回实际写入长度
    int write(uint8_t* data,int len);
    //获取可读长度
    int available();
    //读串口，但不移除数据，返回实际读取长度
    int peek(uint8_t* buf,int len);
    //读串口，直到收到预期长度的数据或超时，参数为：接收缓冲区、预期接收长度、超时（毫秒）,返回实际读取长度
    int read(uint8_t* buf,int len,int timeout);
    //读串口，直到读到预期的结尾符或缓冲区满或超时，参数为：接收缓冲区、最大长度、预期结尾符、超时（毫秒）、实际接收长度，返回READ_END、READ_TIMEOUT或READ_BUFFER_FULL
    int read(uint8_t* buf,int maxLen,const char* end,int timeout,int* recvLen);

private:
    //将数字型波特率转化为系统调用参数
    int transformBaud(int baud);
    //将数字型数据位数转化为系统调用参数
    int transformDataBits(int dataBits);
    long long getTimestamp();
    //判断字符串str是否以字符串end结尾
    bool endsWith(const uint8_t* str,int strLen,const char* end,int endLen);

    //后台接收线程函数
    friend void* receiveThread(void* arg);

};
Serial::Serial():stream()
{
    pthread_mutex_init(&mutex,0);
}

Serial::~Serial()
{
    close();
}

void* receiveThread(void* arg)
{
    Serial* serial=(Serial*)arg;
    uint8_t buf[1024];
    while(true)
    {
        pthread_testcancel();
        int len=read(serial->fd,buf,sizeof(buf));
        if(len>0)
        {
            pthread_mutex_lock(&(serial->mutex));
            serial->stream.append(buf,len);
            pthread_mutex_unlock(&(serial->mutex));
        }
        usleep(1000);
    }
}

int Serial::open(const char* dev,int baud,int dataBits,int parityMode,int stopBits)
{
    struct termios options;
    bzero(&options,sizeof(options));
    int baudT=transformBaud(baud);
    if(baudT<0)
        return BAUD_NOT_SUPPORTED;
    cfsetispeed(&options,baudT);
    cfsetospeed(&options,baudT);
    int dataBitsT=transformDataBits(dataBits);
    if(dataBitsT<0)
        return DATABITS_NOT_SUPPORTED;
    options.c_cflag|=dataBitsT;
    if(parityMode==PARITY_ODD)
    {
        options.c_cflag|=PARENB;
        options.c_cflag|=PARODD;
    }
    else if(parityMode==PARITY_EVEN)
        options.c_cflag|=PARENB;
    else if(parityMode!=PARITY_NONE)
        return PARITYMODE_NOT_SUPPORTED;
    if(stopBits==2)
        options.c_cflag|=CSTOPB;
    else if(stopBits!=1)
        return STOPBITS_NOT_SUPPORTED;
    options.c_cc[VTIME]=1;
    options.c_cc[VMIN]=1;
    fd=::open(dev,O_RDWR|O_NOCTTY|O_NDELAY);
    if(fd<0)
        return DEV_NOT_FOUND;
    if(tcsetattr(fd,TCSANOW,&options))
        return CONFIG_FAIL;
    if(tcflush(fd,TCIOFLUSH))
        return CONFIG_FAIL;
    if(pthread_create(&tid,0,receiveThread,this)!=0)
        return NEW_THREAD_FAIL;
    return OK;
}

int Serial::close()
{
    if(fd>=0)
    {
        ::close(fd);
        pthread_cancel(tid);
        pthread_mutex_destroy(&mutex);
        fd=-1;
        return 0;
    }
    return 0;
}

int Serial::write(uint8_t* data,int len)
{
    return ::write(fd,data,len);
}

int Serial::available()
{
    int len=stream.getLength();
    return len;
}

int Serial::peek(uint8_t* buf,int len)
{
    len=stream.peek(buf,len);
    return len;
}

int Serial::read(uint8_t* buf,int len,int timeout)
{
    timestamp_t start=Timestamp::now();
    int total=0;
    while(total<len)
    {
        pthread_mutex_lock(&mutex);
        int readLen=stream.take(buf+total,len-total);
        pthread_mutex_unlock(&mutex);
        if(readLen>0)
            total+=readLen;
        timestamp_t now=Timestamp::now();
        if(now>=start+timeout)
            break;
        usleep(1000);
    }
    return total;
}

int Serial::read(uint8_t* buf,int maxLen,const char* end,int timeout,int* recvLen)
{
    int endLen=strlen(end);
    timestamp_t start=Timestamp::now();
    int total=0;
    while(total<maxLen)
    {
        pthread_mutex_lock(&mutex);
        int readLen=stream.take(buf+total,1);
        pthread_mutex_unlock(&mutex);
        if(readLen>0)
        {
            total+=readLen;
            if(endsWith(buf,total,end,endLen))
            {
                if(recvLen!=0)
                    *recvLen=total;
                return READ_END;
            }
        }
        timestamp_t now=Timestamp::now();
        if(now>=start+timeout)
            return READ_TIMEOUT;
        usleep(1000);
    }
    return READ_BUFFER_FULL;
}

int Serial::transformBaud(int baud)
{
    int map[][2]={{2400,B2400},{4800,B4800},{9600,B9600},
                  {19200,B19200},{38400,B38400},{57600,B57600},
                  {115200,B115200}};
    for(int i=0;i<sizeof(map)/sizeof(int)/2;i++)
        if(map[i][0]==baud)
            return map[i][1];
    return -1;
}

int Serial::transformDataBits(int dataBits)
{
    int map[][2]={{5,CS5},{6,CS6},{7,CS7},{8,CS8}};
    for(int i=0;i<sizeof(map)/sizeof(int)/2;i++)
        if(map[i][0]==dataBits)
            return map[i][1];
    return -1;
}

bool Serial::endsWith(const uint8_t* str,int strLen,const char* end,int endLen)
{
    if(strLen<endLen)
        return false;
    for(int i=endLen-1;i>=0;i--)
        if(end[i]!=str[strLen-endLen+i])
            return false;
    return true;
}
#endif