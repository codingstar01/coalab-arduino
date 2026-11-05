"""코아랩 파이썬 x 아두이노 - 10 소리센서

소리센서로 소리 크기를 읽어 막대로 보여주고, 큰 소리가 나면 알려줍니다.
실행: python python/10_sound_sensor.py --port COM3
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
    level = int(line)
    bar = "#" * (level // 20)
    print(f"소리 {level:3d}  {bar}")
    if level > 150:
        print("큰 소리!")
