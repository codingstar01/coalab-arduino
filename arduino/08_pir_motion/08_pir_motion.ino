// 코아랩 파이썬 x 아두이노 - 08 PIR 인체감지센서
const int PIR_PIN = 2;

void setup() {
  pinMode(PIR_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println(digitalRead(PIR_PIN));
  delay(200);
}
