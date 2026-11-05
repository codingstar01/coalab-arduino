"""코아랩 파이썬 x 아두이노 - 09 DHT11 온습도센서

DHT11 센서로 온도와 습도를 읽어 화면에 표시합니다. (Adafruit DHT sensor library 필요)
실행: python python/09_dht11.py --port COM3
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
        temp, hum = map(float, line.split(","))
    except ValueError:
        continue
    print(f"온도 {temp:.1f}℃  습도 {hum:.0f}%")
