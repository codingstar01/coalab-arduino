// 코아랩 파이썬 x 아두이노 - 05 푸시버튼
const int BTN_PIN = 2;
const int LED_PIN = 13;

void setup() {
  pinMode(BTN_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int pressed = (digitalRead(BTN_PIN) == LOW);
  digitalWrite(LED_PIN, pressed);
  Serial.println(pressed);
  delay(50);
}
