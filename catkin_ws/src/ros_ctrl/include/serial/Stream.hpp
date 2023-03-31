//本文件实现一个字符流
#ifndef STREAM_H
#define STREAM_H

class Stream
{

private:
    //缓冲区
    uint8_t* buffer;
    //缓冲区容量
    int capacity;
    //流的开头
    int start;
    //流的长度
    int length;

public:
    //初始化一个流，参数为：初始容量
    Stream(int initCapacity=16);
    //清理
    ~Stream();
    //获取流的长度
    int getLength();
    //向流的末尾增加一字符
    void append(uint8_t auint8_t);
    //向流的末尾增加多个字符
    void append(uint8_t* buf,int len);
    //查看流的第一个字符，如果长度为0则返回0
    uint8_t peek();
    //查看流开头的多个字符，返回实际查看到的长度
    int peek(uint8_t* buf,int len);
    //取出流的第一个字符，如果长度为0则返回0
    uint8_t take();
    //取出流开头的多个字符，返回实际取出的长度
    int take(uint8_t* buf,int len);

private:
    //扩大容量至两倍
    void expand();

};

Stream::Stream(int initCapacity)
{
    buffer=new uint8_t[initCapacity];
    capacity=initCapacity;
    start=0;
    length=0;
}

Stream::~Stream()
{
    delete[] buffer;
}

int Stream::getLength()
{
    return length;
}

void Stream::append(uint8_t auint8_t)
{
    if(length>=capacity)
        expand();
    int pos=start+length;
    if(pos>=capacity)
        pos-=capacity;
    buffer[pos]=auint8_t;
    length++;
}

void Stream::append(uint8_t* buf,int len)
{
    for(int i=0;i<len;i++)
        append(buf[i]);
}

uint8_t Stream::peek()
{
    if(length==0)
        return 0;
    return buffer[start];
}

int Stream::peek(uint8_t* buf,int len)
{
    if(len>length)
        len=length;
    for(int i=0;i<len;i++)
    {
        int pos=start+i;
        if(pos>=capacity)
            pos-=capacity;
        buf[i]=buffer[pos];
    }
    return len;
}

uint8_t Stream::take()
{
    if(length==0)
        return 0;
    uint8_t auint8_t=buffer[start];
    start++;
    length--;
    if(start>=capacity)
        start-=capacity;
    return auint8_t;
}

int Stream::take(uint8_t* buf,int len)
{
    if(len>length)
        len=length;
    for(int i=0;i<len;i++)
        buf[i]=take();
    return len;
}

void Stream::expand()
{
    int newCapacity=capacity*2;
    uint8_t* newBuf=new uint8_t[newCapacity];
    int newLength=length;
    take(newBuf,newLength);
    delete[] buffer;
    buffer=newBuf;
    capacity=newCapacity;
    start=0;
    length=newLength;
    return;
}
#endif