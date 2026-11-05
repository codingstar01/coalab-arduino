// 코아랩 파이썬 x 아두이노 - 11 서보모터
// 회로: 서보 주황(신호) - D9, 빨강(+) - 5V, 갈색(-) - GND
// 파이썬이 "각도\n"(0~180)를 보내면 서보가 그 각도로 움직인다.

#include <Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9);
  myServo.write(90);  // 시작은 가운데
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();       // 숫자 읽기
    angle = constrain(angle, 0, 180);    // 범위 제한
    myServo.write(angle);
    Serial.println(angle);               // 받은 각도를 되돌려 보낸다
  }
}
