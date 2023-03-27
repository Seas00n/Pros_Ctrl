#ifndef INC_RINGBUFFER_H_
#define INC_RINGBUFFER_H_
#include "stdint.h"
#define Buffer_MAX 140
typedef struct{
    uint8_t headPosition;
    uint8_t tailPosition;  
    uint8_t ringBuf[Buffer_MAX];
}ringBuffer_t;
void RingBuf_WriteByte(ringBuffer_t* buffer,uint8_t data){
	buffer->ringBuf[buffer->tailPosition]=data;
	if(++(buffer->tailPosition)>=Buffer_MAX){
		buffer->tailPosition = 0;
	}else{}
	if(buffer->tailPosition==buffer->headPosition){
		if(++buffer->headPosition>=Buffer_MAX){
			buffer->headPosition = 0;
		}
	}else{}
}
void RingBuf_WriteByteArray(ringBuffer_t* buffer, uint8_t* pData, uint32_t length){
	for(int i=0;i<length;i++){
		RingBuf_WriteByte(buffer, *(pData+i));
	}
}
int RingBuf_ReadByte(ringBuffer_t* buffer, uint8_t* pData){
	if(buffer->headPosition==buffer->tailPosition){
		return 1;
	}else{
		*pData = buffer->ringBuf[buffer->headPosition];
		if(++(buffer->headPosition)>=Buffer_MAX){
			buffer->headPosition = 0;
			return 0;
		}
	}
	return 0;
}

int RingBuf_ReadByteArray(ringBuffer_t* buffer, uint8_t* pData, uint32_t length){
	for(int j=0;j<length;j++){
		RingBuf_ReadByte(buffer, (uint8_t*)(pData+j));
	}
	return 0;
}

uint8_t RingBuf_PeekByte(ringBuffer_t* buffer){
	return buffer->ringBuf[buffer->headPosition];
}

#endif