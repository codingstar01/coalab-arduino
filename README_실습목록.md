## 실습 목록

README.md의 "실습 목록" 부분을 아래 표로 바꿔 넣으세요.

| 장 | 주제 | 아두이노 스케치 | 파이썬 |
|---|---|---|---|
| 01 | LED 깜빡이기 | arduino/01_led_blink | python/01_led_blink.py |
| 02 | 조도센서(LDR) | arduino/02_light_sensor | python/02_light_sensor.py |
| 03 | 온도센서(LM35) | arduino/03_temperature_lm35 | python/03_temperature_lm35.py |
| 04 | 가변저항 | arduino/04_potentiometer | python/04_potentiometer.py |
| 05 | 푸시버튼 | arduino/05_push_button | python/05_push_button.py |
| 06 | 초음파 거리센서 | arduino/06_ultrasonic | python/06_ultrasonic.py |
| 07 | 부저 | arduino/07_buzzer | python/07_buzzer.py |
| 08 | PIR 인체감지센서 | arduino/08_pir_motion | python/08_pir_motion.py |
| 09 | DHT11 온습도센서 | arduino/09_dht11 | python/09_dht11.py |
| 10 | 소리센서 | arduino/10_sound_sensor | python/10_sound_sensor.py |
| 11 | 서보모터 | arduino/11_servo | python/11_servo.py |
| 12 | 로봇암 만들기(3축) | arduino/12_robot_arm | python/robot_arm.py |
| 13 | 센서 + 로봇암 (티칭&재생, 자동 집기) | 12장 펌웨어 그대로 | python/13_teach_replay.py, python/13_auto_pick.py |
| 14 | 컨베이어벨트 (L298N + IR 센서 가정) | arduino/14_conveyor | python/14_conveyor.py |
| 15 | 스마트팜 (토양수분 + 릴레이 펌프) | arduino/15_smart_farm | python/15_smart_farm.py |

주의: 11~15장 소스는 실제 하드웨어로 시험하지 않았습니다. 로봇암 각도, 릴레이 동작(LOW=켜짐 기준), 컨베이어 부품은 내 장치에 맞게 조정하세요.
09장은 Arduino IDE 라이브러리 관리자에서 "DHT sensor library"(Adafruit)를 설치해야 합니다.
