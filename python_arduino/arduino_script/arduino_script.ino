#include <Servo.h>

Servo servo1; // Create servo object for motor 1
int pos=0; //variable to store the servo position
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo1.attach(9); //ataches the servo on pin 9 to the servo object
  servo1.write(pos);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0) {
    char jul = Serial.read();
     if (jul == 'o'){
      pos=0;
      servo1.write(pos);
     }
     if (jul == 'c'){
      //Serial.println("you pressed c");
      pos=360;
      servo1.write(pos);
      }
  }
  delay(15);
 }
