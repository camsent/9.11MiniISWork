//the idea behind this sketch is to figure how to measure voltage across a resistor
//when res is dc'd from GND V = 5
//when res is dc'd from POS V = 0
//normal behavior is V = 2.5

#include <Arduino.h>

int testPoint = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int testVal = analogRead(testPoint);
  float voltageVal = testVal * (5.0/1023.0);
  Serial.println(voltageVal);
  delay(500);
}
