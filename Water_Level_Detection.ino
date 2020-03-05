#include <Ultrasonic.h>
#include <BoltIoT-Arduino-Helper.h>
Ultrasonic ultrasonic(12, 13);

void setup() {
  Serial.begin(9600);
  
  }

void loop() {

  Serial.println(ultrasonic.distanceRead());
  delay(1000);
}
  
