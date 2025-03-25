"""

int a = 0;
float b = 3.14;
bool SimouNao = true;
String = "Kazan";

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  blink();
}

void blink() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}

"""

from machine import Pin
from time import sleep

a = 0
b = 3.14
c = True
d = "Kazan"

led = Pin(2, Pin.OUT)

def blink():
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

while True:
    blink()
    