"""코아랩 파이썬 x 아두이노 - 02 조도센서(LDR)

아두이노가 보내는 밝기 값(0~1023)을 읽어 밝음/어두움을 판단합니다.
실행: python python/02_light_sensor.py --port COM3
"""
import argparse

import serial  # pip install pyserial

THRESHOLD = 500  # 이 값보다 작으면 "어두움"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud, timeout=1) as ser:
        print("조도센서 읽는 중... (종료: Ctrl+C)")
        while True:
            line = ser.readline().decode(errors="ignore").strip()
            if not line.isdigit():
                continue
            value = int(line)
            state = "어두움" if value < THRESHOLD else "밝음"
            print(f"밝기 {value:4d}  →  {state}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n종료합니다.")
