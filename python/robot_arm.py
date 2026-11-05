"""코아랩 파이썬 x 아두이노 - 12 로봇암 제어 라이브러리

12장 펌웨어(12_robot_arm.ino)와 대화하는 Arm 클래스입니다.
단독 실행하면 간단한 데모를 보여 줍니다.
실행: python python/robot_arm.py --port COM3
"""
import argparse
import time

import serial  # pip install pyserial

HOME = (90, 90, 60)  # 베이스, 어깨, 집게 (집게 60 = 반쯤 열림)


class Arm:
    def __init__(self, port, baud=9600):
        self.ser = serial.Serial(port, baud, timeout=3)
        time.sleep(2)  # 아두이노 재시작 대기
        self.ser.reset_input_buffer()

    def move(self, base, shoulder, grip, wait=True):
        """목표 각도로 이동한다. wait=True면 도착(DONE)할 때까지 기다린다."""
        self.ser.write(f"{base},{shoulder},{grip}\n".encode())
        if wait:
            self._wait_done()

    def _wait_done(self, timeout=15):
        end = time.time() + timeout
        while time.time() < end:
            line = self.ser.readline().decode(errors="ignore").strip()
            if line == "DONE":
                return
        raise TimeoutError("로봇암이 응답하지 않아요. 전원과 배선을 확인하세요.")

    def distance(self):
        """초음파 거리(cm). 측정 실패 시 None."""
        self.ser.reset_input_buffer()
        self.ser.write(b"D\n")
        line = self.ser.readline().decode(errors="ignore").strip()
        if line.startswith("DIST,"):
            cm = float(line.split(",")[1])
            return cm if cm > 0 else None
        return None

    def home(self):
        self.move(*HOME)

    def close(self):
        self.ser.close()


def demo(arm):
    print("홈 위치로 이동")
    arm.home()
    print("손 흔들기")
    for _ in range(2):
        arm.move(60, 90, 60)
        arm.move(120, 90, 60)
    arm.home()
    print("집게 열고 닫기")
    arm.move(90, 90, 80)
    arm.move(90, 90, 30)
    arm.home()
    print("끝!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
    args = parser.parse_args()
    arm = Arm(args.port)
    try:
        demo(arm)
    finally:
        arm.close()
