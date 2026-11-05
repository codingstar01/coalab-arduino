// 코아랩 파이썬 x 아두이노 - 10 소리센서
const int MIC_PIN = A0;

int readLevel() {
  unsigned long start = millis();
  int sMax = 0, sMin = 1023;
  while (millis() - start < 50) {
    int s = analogRead(MIC_PIN);
    if (s > sMax) sMax = s;
    if (s < sMin) sMin = s;
  }
  return sMax - sMin;
}

void setup() { Serial.begin(9600); }

void loop() { Serial.println(readLevel()); }
