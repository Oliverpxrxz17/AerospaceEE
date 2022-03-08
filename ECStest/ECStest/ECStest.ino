 
#include <Servo.h>

Servo ESC;     // create servo object to control the ESC

int potValue;  // value from the analog pin
double thrustPercent;
void setup() {
  // Attach the ESC on pin 9
  ESC.attach(9,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  Serial.begin(9600);
}

void loop() {
  potValue = analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
      Serial.print("Pot value = ");Serial.println(potValue);
        thrustPercent = (double(potValue)/1023)*100;

 potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)

  //For continuous servo it rotates right if 0. 180 degrees and left if 0 degrees.
  ESC.write(potValue);    // Send the signal to the ESC


  Serial.print("Current thrust = ");Serial.println(thrustPercent);
  delay(100);
}
