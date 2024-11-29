/*
 * Arduino Sketch for TinyML
 */

#include <TensorFlowLite.h>

void setup() {
  Serial.begin(9600);
  Serial.println("Initializing TFLite Micro...");

  // Setup code here...
}

void loop() {
  // Read sensor
  int sensorValue = analogRead(A0);

  // Normalize
  float input = sensorValue / 1024.0;

  // Run Inference (pseudocode)
  // model.predict(input);

  delay(100);
}
