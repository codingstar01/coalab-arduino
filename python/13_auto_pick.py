"""코아랩 파이썬 x 아두이노 - 13 자동 집기

초음파 센서 앞에 물건이 가까이(10cm 이내) 3번 연속 감지되면
집어서 오른쪽에 내려놓고 돌아옵니다.
실행: python python/13_auto_pick.py --port COM3
"""
import argparse
import time

from robot_arm import Arm

NEAR_CM = 10      # 이 거리 이하면 '물건 있음'
CONFIRM = 3       # 연속 몇 번 감지되면 동작할지
GRIP_OPEN = 80
GRIP_CLOSE = 30

# 각도는 내 로봇암에 맞게 바꾼다 (베이스, 어깨, 집게)
PICK = (90, 60, GRIP_OPEN)
PLACE = (150, 60, GRIP_CLOSE)


def pick_and_place(arm):
    arm.move(*PICK)                       # 물건 위로 내려가며 집게 열기
    arm.move(PICK[0], PICK[1], GRIP_CLOSE)  # 집기
    arm.move(90, 100, GRIP_CLOSE)         # 들어 올리기
    arm.move(PLACE[0], 100, GRIP_CLOSE)   # 오른쪽으로 돌기
    arm.move(*PLACE[:2], GRIP_OPEN)       # 내려놓기(집게 열기)
    arm.home()                            # 돌아오기


parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
args = parser.parse_args()

arm = Arm(args.port)
arm.home()
print("물건을 센서 앞에 가져다 대세요. (종료: Ctrl+C)")
seen = 0
try:
    while True:
        cm = arm.distance()
        if cm is not None and cm <= NEAR_CM:
            seen += 1
            print(f"감지 {seen}/{CONFIRM}  ({cm:.1f}cm)")
        else:
            seen = 0
        if seen >= CONFIRM:
            print("집기 시작!")
            pick_and_place(arm)
            seen = 0
            time.sleep(1)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\n종료합니다.")
finally:
    arm.home()
    arm.close()
