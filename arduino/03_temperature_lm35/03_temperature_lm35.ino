// 코아랩 파이썬 x 아두이노 - 03 온도센서(LM35)
// 회로: LM35 왼쪽 다리(+Vs) - 5V, 가운데 다리(Vout) - A0, 오른쪽 다리(GND) - GND
// (센서의 평평한 면이 나를 향하게 놓았을 때)

const int LM35_PIN = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int raw = analogRead(LM35_PIN);        // 0 ~ 1023
  float celsius = raw * 500.0 / 1024.0;  // LM35: 1℃ = 10mV, 기준 전압 5V
  Serial.println(celsius);
  delay(500);
}
