 void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Read values from each sensor
  int mq2Val = analogRead(A0);
  int mq3Val = analogRead(A1);
  int mq4Val = analogRead(A2);
  int mq5Val = analogRead(A3);
  int mq6Val = analogRead(A4);
  int mq7Val = analogRead(A8);
  int mq8Val = analogRead(A9);
  int mq9Val = analogRead(A10);
  int mq135Val = analogRead(A11);
  int mq137Val = analogRead(A12);

  // Print all sensor values in one line
  //Serial.print("");
  Serial.print(mq2Val);
  Serial.print(",");
  Serial.print(mq3Val);
  Serial.print(",");
  Serial.print(mq4Val);
  Serial.print(",");
  Serial.print(mq5Val);
  Serial.print(",");
  Serial.print(mq6Val);
  Serial.print(",");
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
