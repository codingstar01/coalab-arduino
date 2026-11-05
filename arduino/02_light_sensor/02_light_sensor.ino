// 코아랩 파이썬 x 아두이노 - 02 조도센서(LDR)
// 회로: 5V - LDR - A0 - 10kΩ - GND (A0는 LDR과 저항 사이에 연결)

const int LDR_PIN = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(LDR_PIN);  // 0 ~ 1023 (밝을수록 큰 값)
  Serial.println(value);
  delay(100);
}
