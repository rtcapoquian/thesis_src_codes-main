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
  //int mq7Val = analogRead(A5);

  // Print all sensor values in one line
  Serial.print(mq2Val);
  Serial.print(",");
  Serial.print(mq3Val);
  Serial.print(",");
  Serial.print(mq4Val);
  Serial.print(",");
  Serial.print(mq5Val);
  Serial.print(",");
  Serial.println(mq6Val);
  //Serial.print(",");
  //Serial.println(mq7Val);

  // Delay before the next reading
  delay(100);
}
