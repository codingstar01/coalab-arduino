// 코아랩 파이썬 x 아두이노 - 01 LED 깜빡이기 (파이썬으로 제어)
// 회로: 13번 핀 - 220Ω - LED(+) , LED(-) - GND
// 파이썬이 '1'을 보내면 켜고 '0'을 보내면 끈다.

const int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '1') digitalWrite(LED_PIN, HIGH);
    if (c == '0') digitalWrite(LED_PIN, LOW);
  }
}
