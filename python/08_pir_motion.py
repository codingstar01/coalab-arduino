"""코아랩 파이썬 x 아두이노 - 08 PIR 인체감지센서

PIR 센서로 움직임을 감지해 횟수를 세고 알려줍니다.
실행: python python/08_pir_motion.py --port COM3
"""
import argparse
import serial  # pip install pyserial

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

ser = serial.Serial(args.port, 9600, timeout=2)
count = 0
last = 0

while True:
    line = ser.readline().decode().strip()
    if line not in ("0", "1"):
        continue
    now = int(line)
    if now == 1 and last == 0:
        count += 1
        print(f"움직임 감지! ({count}번째)")
    last = now
