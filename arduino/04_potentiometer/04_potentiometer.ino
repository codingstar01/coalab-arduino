// 코아랩 파이썬 x 아두이노 - 04 가변저항(포텐셔미터)
const int POT_PIN = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(POT_PIN);
  Serial.println(value);
  delay(100);
}
