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
   git clone https://github.com/<내 계정>/coalab-arduino.git
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
| 01 | LED | `arduino/01_led/` | `python/01_led.py` |
| 02 | (센서 이름) | `arduino/02_xxx/` | `python/02_xxx.py` |

## 문의

코아랩 (COALAB) · https://coalab.co.kr
