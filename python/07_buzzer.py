"""코아랩 파이썬 x 아두이노 - 07 부저

파이썬이 시리얼로 '1'을 보내면 아두이노가 부저를 0.2초 울립니다.
실행: python python/07_buzzer.py --port COM3
"""
import argparse
import time
import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)
time.sleep(2)  # 아두이노 재시작 대기

for i in range(3):
    ser.write(b"1")  # 삑!
    print(f"삑! ({i + 1}/3)")
    time.sleep(0.7)
