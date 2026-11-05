"""코아랩 파이썬 x 아두이노 - 03 온도센서(LM35)

아두이노가 보내는 섭씨 온도를 읽어 화면에 표시하고, 기준 이상이면 알려줍니다.
실행: python python/03_temperature_lm35.py --port COM3
"""
import argparse

import serial  # pip install pyserial

HOT = 30.0  # 이 온도 이상이면 "더워요!"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud, timeout=2) as ser:
        print("온도 읽는 중... (종료: Ctrl+C)")
        while True:
            line = ser.readline().decode(errors="ignore").strip()
            try:
                temp = float(line)
            except ValueError:
                continue
            msg = f"현재 온도 {temp:.1f}℃"
            if temp >= HOT:
                msg += "  더워요!"
            print(msg)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n종료합니다.")
