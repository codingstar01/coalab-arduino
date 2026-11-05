"""코아랩 파이썬 x 아두이노 - 06 초음파 거리센서(HC-SR04)

초음파센서로 거리를 재서 cm로 표시하고, 가까우면 경고합니다.
실행: python python/06_ultrasonic.py --port COM3
"""
import argparse
import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)

while True:
    line = ser.readline().decode().strip()
    try:
        cm = float(line)
    except ValueError:
        continue
    if cm == 0:
        continue  # 측정 실패
    print(f"거리 {cm:.1f}cm")
    if cm < 20:
        print("너무 가까워요!")
