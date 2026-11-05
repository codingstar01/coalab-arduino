"""코아랩 파이썬 x 아두이노 - 05 푸시버튼

푸시버튼을 누른 횟수를 세어 화면에 표시합니다. (13번 핀 내장 LED도 함께 켜짐)
실행: python python/05_push_button.py --port COM3
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
        print(f"버튼 {count}번 눌림!")
    last = now
