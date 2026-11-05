"""코아랩 파이썬 x 아두이노 - 14 컨베이어벨트

IR 센서로 컨베이어를 지나가는 물건을 세고, 목표 개수가 되면 벨트를 멈춥니다. (L298N 모터 드라이버 + DC 기어모터 가정)
실행: python python/14_conveyor.py --port COM3
"""
import argparse
import time
import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)
time.sleep(2)

GOAL = 5
count = 0
start = time.time()

while count < GOAL:
    line = ser.readline().decode().strip()
    if line == "ITEM":
        count += 1
        print(f"물건 {count}개 통과 ({time.time() - start:.1f}초)")

ser.write(b"S")
print("목표 달성! 컨베이어 정지")
