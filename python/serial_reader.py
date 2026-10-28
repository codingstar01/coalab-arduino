"""아두이노가 시리얼로 보내는 값을 읽어 화면에 출력하는 기본 예제."""
import argparse

import serial


def main():
    parser = argparse.ArgumentParser(description="아두이노 시리얼 읽기")
    parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud, timeout=1) as ser:
        print(f"{args.port} 연결됨 (Ctrl+C로 종료)")
        try:
            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if line:
                    print(line)
        except KeyboardInterrupt:
            print("종료")


if __name__ == "__main__":
    main()
