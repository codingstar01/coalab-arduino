"""코아랩 파이썬 x 아두이노 - 01 LED 깜빡이기

파이썬이 아두이노에 '1'/'0'을 보내 LED를 0.5초 간격으로 5번 깜빡입니다.
실행: python python/01_led_blink.py --port COM3
"""
import argparse
import time

import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)
time.sleep(2)  # 아두이노 재시작 대기

for i in range(5):
    ser.write(b"1")
    print(f"켜짐 ({i + 1}/5)")
    time.sleep(0.5)
    ser.write(b"0")
    print("꺼짐")
    time.sleep(0.5)
