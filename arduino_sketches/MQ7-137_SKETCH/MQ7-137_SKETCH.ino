void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Read values from each sensor
  int mq7Val = analogRead(A8);
  int mq8Val = analogRead(A9);
  int mq9Val = analogRead(A10);
  int mq135Val = analogRead(A11);
  int mq137Val = analogRead(A12);

  // Print all sensor values in one line
  //Serial.print("");
  Serial.print(mq7Val);
  Serial.print(",");
  Serial.print(mq8Val);
  Serial.print(",");
  Serial.print(mq9Val);
  Serial.print(",");
  Serial.print(mq135Val);
  Serial.print(",");
  Serial.println(mq137Val);

  // Delay before the next reading
  delay(100);
}
