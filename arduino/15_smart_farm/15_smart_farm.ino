// 코아랩 파이썬 x 아두이노 - 15 스마트팜
const int SOIL = A0, RELAY = 7;
void setup() {
  Serial.begin(9600);
  pinMode(RELAY, OUTPUT);
  digitalWrite(RELAY, HIGH);  // 꺼짐
}
void loop() {
  Serial.println(analogRead(SOIL));
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == 'P') {
      digitalWrite(RELAY, LOW);   // 켜기
      delay(2000);
      digitalWrite(RELAY, HIGH);  // 끄기
    }
  }
  delay(500);
}
