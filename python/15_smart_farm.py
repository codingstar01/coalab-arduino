"""코아랩 파이썬 x 아두이노 - 15 스마트팜

토양수분센서 값이 기준보다 건조하면 릴레이로 워터펌프를 켜서 물을 줍니다. (릴레이는 LOW에서 켜지는 모듈 기준)
실행: python python/15_smart_farm.py --port COM3
"""
import argparse
import time
import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)
DRY = 600

while True:
    line = ser.readline().decode().strip()
    if not line.isdigit():
        continue
    soil = int(line)
    print(f"토양 수분 값 {soil}")
    if soil > DRY:
        print("건조! 물 주기")
        ser.write(b"P")
        time.sleep(10)
