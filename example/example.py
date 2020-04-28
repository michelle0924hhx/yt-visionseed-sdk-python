import visionseed as vs
import serial
import time


datalink = vs.YtDataLink( serial.Serial("/dev/ttyACM0",115200,timeout=0.5) )

def recvMsg():
    while True:
        msg = datalink.recvRunOnce()
        if msg:
            if msg.result.HasField('faceDetectionResult'):
                if len(msg.result.faceDetectionResult.face) > 0:
                    print("[%d] %s (confidence: %.3f, traceId: %d)" % (msg.result.frameId, msg.result.faceDetectionResult.face[0].name, msg.result.faceDetectionResult.face[0].nameConfidence, msg.result.faceDetectionResult.face[0].traceId))
                return msg

while True:
    msg = recvMsg()
