"""코아랩 파이썬 x 아두이노 - 11 서보모터

파이썬이 각도를 보내 서보모터를 0 -> 180 -> 0도로 쓸고 지나갑니다.
실행: python python/11_servo.py --port COM3
"""
import argparse
import time

import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)
time.sleep(2)  # 아두이노 재시작 대기


def move(angle):
    ser.write(f"{angle}\n".encode())
    reply = ser.readline().decode(errors="ignore").strip()
    print(f"각도 {angle:3d}  (아두이노 응답: {reply})")


for angle in list(range(0, 181, 30)) + list(range(150, -1, -30)):
    move(angle)
    time.sleep(0.5)
