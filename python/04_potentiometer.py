"""코아랩 파이썬 x 아두이노 - 04 가변저항(포텐셔미터)

가변저항 손잡이를 돌린 값(0~1023)을 읽어 퍼센트와 막대로 보여줍니다.
실행: python python/04_potentiometer.py --port COM3
"""
import argparse
import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)

while True:
    line = ser.readline().decode().strip()
    if not line.isdigit():
        continue
    percent = round(int(line) / 1023 * 100)
    bar = "#" * (percent // 5)
    print(f"{percent:3d}%  {bar}")
