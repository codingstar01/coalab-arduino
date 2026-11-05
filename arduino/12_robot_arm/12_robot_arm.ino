// 코아랩 파이썬 x 아두이노 - 12 로봇암(3축)
// 서보: 베이스 D3, 어깨 D5, 집게 D6 (외부 5V 전원 사용, GND는 아두이노와 연결)
// 명령(파이썬 -> 아두이노, 한 줄):
//   "베이스,어깨,집게\n"  예) 90,90,60  -> 목표 각도로 천천히 이동, 도착하면 "DONE" 응답
//   "D\n"                  -> 초음파 거리 측정(선택 부품), "DIST,12.3" 응답

#include <Servo.h>

Servo base, shoulder, grip;

const int PIN_BASE = 3, PIN_SHOULDER = 5, PIN_GRIP = 6;
const int TRIG = 10, ECHO = 9;

// 관절별 안전 범위 (내 로봇암에 맞게 조정)
const int MIN_ANGLE[3] = {0, 30, 20};
const int MAX_ANGLE[3] = {180, 150, 90};

int cur[3]    = {90, 90, 60};
int target[3] = {90, 90, 60};
bool moving = false;
unsigned long lastStep = 0;
const unsigned long STEP_MS = 15;  // 값이 클수록 천천히 움직인다

void writeAll() {
  base.write(cur[0]);
  shoulder.write(cur[1]);
  grip.write(cur[2]);
}

float readDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long us = pulseIn(ECHO, HIGH, 30000);
  return us * 0.034 / 2;  // 실패하면 0
}

void handleLine(String line) {
  line.trim();
  if (line == "D") {
    Serial.print("DIST,");
    Serial.println(readDistance(), 1);
    return;
  }
  int a, b, c;
  if (sscanf(line.c_str(), "%d,%d,%d", &a, &b, &c) == 3) {
    target[0] = constrain(a, MIN_ANGLE[0], MAX_ANGLE[0]);
    target[1] = constrain(b, MIN_ANGLE[1], MAX_ANGLE[1]);
    target[2] = constrain(c, MIN_ANGLE[2], MAX_ANGLE[2]);
    moving = true;
  }
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  base.attach(PIN_BASE);
  shoulder.attach(PIN_SHOULDER);
  grip.attach(PIN_GRIP);
  writeAll();
}

void loop() {
  if (Serial.available() > 0) {
    handleLine(Serial.readStringUntil('\n'));
  }

  if (millis() - lastStep >= STEP_MS) {
    lastStep = millis();
    bool arrived = true;
    for (int i = 0; i < 3; i++) {
      if (cur[i] < target[i]) { cur[i]++; arrived = false; }
      else if (cur[i] > target[i]) { cur[i]--; arrived = false; }
    }
    writeAll();
    if (arrived && moving) {
      moving = false;
      Serial.println("DONE");
    }
  }
}
