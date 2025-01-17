int trigPin = 12;    // Trigger
int echoPin = 13;    // Echo
long duration, cm, inches;
 
void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
 
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
 
  cm = (duration/2) / 29.1;     
  inches = (duration/2) / 74;   

  if (cm>15){
    cm = 0;
  }

  Serial.println(cm);
  delay(100);
}