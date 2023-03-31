//本文件定义一个毫秒级的时间戳工具类
#ifndef TIMESTAMP_H
#define TIMESTAMP_H
#include <time.h>
#include <sys/time.h>
//时间戳类型
typedef long long timestamp_t;

class Timestamp
{

public:
    //获取以毫秒计的时间戳
    static timestamp_t now();

};
timestamp_t Timestamp::now()
{
    struct timeval tv;
    gettimeofday(&tv,0);
    timestamp_t time=(timestamp_t)tv.tv_sec*1000+tv.tv_usec/1000;
    return time;
}

#endif