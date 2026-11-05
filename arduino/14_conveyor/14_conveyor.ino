// 코아랩 파이썬 x 아두이노 - 14 컨베이어벨트
const int ENA = 6, IN1 = 7, IN2 = 8, IR = 2;
bool last = false;
void setup() {
  Serial.begin(9600);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IR, INPUT);
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  analogWrite(ENA, 150);
}
void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == 'S') analogWrite(ENA, 0);
    if (c == 'G') analogWrite(ENA, 150);
  }
  bool seen = (digitalRead(IR) == LOW);
  if (seen && !last) Serial.println("ITEM");
  last = seen;
  delay(20);
}
