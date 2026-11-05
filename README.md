# 코아랩 파이썬 × 아두이노

파이썬과 아두이노를 시리얼 통신으로 연결해 센서를 읽고 LED·부저 같은 부품을 제어하는 실습 소스 모음입니다.

## 폴더 구성

```
coalab-arduino/
├── arduino/        # 아두이노 스케치 (.ino)
├── python/         # 파이썬 실습 코드 (.py)
├── images/         # 회로도·배선 사진
├── requirements.txt
└── README.md
```

## 준비물

- 아두이노 (Uno / Nano 등), USB 케이블
- 브레드보드, 점퍼선, 실습별 센서·부품
- Python 3.9 이상, Arduino IDE

## 실행 방법

1. 저장소를 내려받습니다.
   ```bash
   git clone https://github.com/codingstar01/coalab-arduino.git
   cd coalab-arduino
   ```
2. 파이썬 패키지를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```
3. `arduino/` 폴더의 스케치를 Arduino IDE로 열어 보드에 업로드합니다.
4. 포트 이름을 확인하고(Windows `COM3`, 맥 `/dev/cu.usbmodem...`, 리눅스 `/dev/ttyUSB0`), 파이썬 코드를 실행합니다.
   ```bash
   python python/serial_reader.py --port COM3
   ```

## 실습 목록

| 회차 | 주제 | 아두이노 | 파이썬 |
|------|------|----------|--------|
| 01 | LED 깜빡이기 | `arduino/01_led_blink/` | `python/01_led_blink.py` |
| 02 | 조도센서(LDR) | `arduino/02_light_sensor/` | `python/02_light_sensor.py` |
| 03 | 온도센서(LM35) | `arduino/03_temperature_lm35/` | `python/03_temperature_lm35.py` |
| 04 | 가변저항 | `arduino/04_potentiometer/` | `python/04_potentiometer.py` |
| 05 | 푸시버튼 | `arduino/05_push_button/` | `python/05_push_button.py` |
| 06 | 초음파 거리센서 | `arduino/06_ultrasonic/` | `python/06_ultrasonic.py` |
| 07 | 부저 | `arduino/07_buzzer/` | `python/07_buzzer.py` |
| 08 | PIR 인체감지센서 | `arduino/08_pir_motion/` | `python/08_pir_motion.py` |
| 09 | DHT11 온습도센서 | `arduino/09_dht11/` | `python/09_dht11.py` |
| 10 | 소리센서 | `arduino/10_sound_sensor/` | `python/10_sound_sensor.py` |
| 11 | 서보모터 | `arduino/11_servo/` | `python/11_servo.py` |
| 12 | 로봇암 만들기(3축) | `arduino/12_robot_arm/` | `python/robot_arm.py` |
| 13 | 센서 + 로봇암 (티칭&재생, 자동 집기) | 12장 펌웨어 그대로 | `python/13_teach_replay.py`, `python/13_auto_pick.py` |
| 14 | 컨베이어벨트 (L298N + IR 센서 가정) | `arduino/14_conveyor/` | `python/14_conveyor.py` |
| 15 | 스마트팜 (토양수분 + 릴레이 펌프) | `arduino/15_smart_farm/` | `python/15_smart_farm.py` |

> 09장은 Arduino IDE 라이브러리 관리자에서 "DHT sensor library"(Adafruit)를 설치해야 합니다.

## 문의

코아랩 (COALAB) · https://coalab.co.kr
