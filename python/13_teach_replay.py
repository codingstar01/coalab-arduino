"""코아랩 파이썬 x 아두이노 - 13 티칭 & 재생

각도를 입력해 로봇암을 움직이고, 마음에 드는 자세를 저장해 순서대로 재생합니다.
실행: python python/13_teach_replay.py --port COM3

명령:  90,90,60  이동   s 현재 자세 저장   p 저장한 동작 재생
       save 파일에 저장   load 파일 불러오기   clear 지우기   q 종료
"""
import argparse
import json
import time

from robot_arm import Arm, HOME

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="예: COM3, /dev/ttyUSB0")
parser.add_argument("--file", default="moves.json", help="저장 파일 이름")
args = parser.parse_args()

arm = Arm(args.port)
steps = []
current = HOME
arm.home()
print("명령을 입력하세요. (예: 90,90,60)")

try:
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "q":
            break
        elif cmd == "s":
            steps.append(current)
            print(f"저장 {len(steps)}번째: {current}")
        elif cmd == "p":
            for i, pose in enumerate(steps, 1):
                print(f"재생 {i}/{len(steps)}: {pose}")
                arm.move(*pose)
                time.sleep(0.3)
        elif cmd == "save":
            with open(args.file, "w") as fp:
                json.dump(steps, fp)
            print(f"{args.file}에 {len(steps)}개 저장")
        elif cmd == "load":
            with open(args.file) as fp:
                steps = [tuple(p) for p in json.load(fp)]
            print(f"{len(steps)}개 불러옴")
        elif cmd == "clear":
            steps = []
        else:
            try:
                pose = tuple(int(v) for v in cmd.split(","))
                if len(pose) != 3:
                    raise ValueError
            except ValueError:
                print("형식: 베이스,어깨,집게  예) 90,90,60")
                continue
            current = pose
            arm.move(*pose)
finally:
    arm.home()
    arm.close()
