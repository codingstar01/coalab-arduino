// 코아랩 파이썬 x 아두이노 - 06 초음파 거리센서(HC-SR04)
const int TRIG = 10;
const int ECHO = 9;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long us = pulseIn(ECHO, HIGH, 30000);
  Serial.println(us * 0.034 / 2);
  delay(200);
}
