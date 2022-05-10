#include<Servo.h>

String x;
Servo thumb;
Servo index;
Servo ring;
Servo middle;
Servo little;
int LED = 8;

int time = 1500;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  thumb.attach(3);
  index.attach(7);
  middle.attach(6);
  ring.attach(5);
  little.attach(4);
  pinMode(LED, OUTPUT);
}

void led_on() {
  digitalWrite(LED, HIGH);
}
void led_off() {
  digitalWrite(LED, LOW);
}

void thumb_open(bool full) {
  if (full) {
    thumb.write(10);
    delay(400);
    thumb.write(92);
  }
  else {
    thumb.write(10);
    delay(200);
    thumb.write(92);
  }
}
void thumb_close(bool full) {
  if (full) {
    thumb.write(170);
    delay(400);
    thumb.write(92);
  }
  else {
    thumb.write(170);
    delay(200);
    thumb.write(92);
  }
}
void index_open(bool full) {
  if (full) {
    index.write(10);
    delay(650);
    index.write(92);
  }
  else {
    index.write(10);
    delay(150);
    index.write(92);
  }
}
void index_close(bool full) {
  if (full) {
    index.write(170);
    delay(700);
    index.write(92);
  }
  else {
    index.write(170);
    delay(200);
    index.write(92);
  }
}
void middle_open(bool full) {
  if (full) {
    middle.write(10);
    delay(620);
    middle.write(92);
  }
  else {
    middle.write(10);
    delay(280);
    middle.write(92);
  }
}
void middle_close(bool full) {
  if (full) {
    middle.write(170);
    delay(780);
    middle.write(92);
  }
  else {
    middle.write(170);
    delay(400);
    middle.write(92);
  }
}
void ring_open(bool full) {
  if (full) {
    ring.write(10);
    delay(750);
    ring.write(92);
  }
  else {
    ring.write(10);
    delay(170);
    ring.write(92);
  }
}
void ring_close(bool full) {
  if (full) {
    ring.write(170);
    delay(700);
    ring.write(92);
  }
  else {
    ring.write(170);
    delay(200);
    ring.write(92);
  }
}
void little_open(bool full) {
  if (full) {
    little.write(10);
    delay(600);
    little.write(92);
  }
  else {
    little.write(10);
    delay(150);
    little.write(92);
  }
}
void little_close(bool full) {
  if (full) {
    little.write(170);
    delay(720);
    little.write(92);
  }
  else {
    little.write(170);
    delay(150);
    little.write(92);
  }
}

void loop() {
  while (!Serial.available());
  x = Serial.readString();
  Serial.print(x);
  if (x == "a") {
    index_close(true);
    delay(time);
    middle_close(true);
    delay(time);
    ring_close(true);
    delay(time);
    little_close(true);
    led_on();
    delay(time);
    led_off();

    index_open(true);
    delay(time);
    middle_open(true);
    delay(time);
    ring_open(true);
    delay(time);
    little_open(true);
  }
  if (x == "b") {
    thumb_close(true);
    led_on();
    delay(time);
    led_off();
    thumb_open(true);
  }
  if (x == "c") {
    index_close(false);
    delay(time);
    middle_close(false);
    delay(time);
    ring_close(false);
    delay(time);
    little_close(false);
    led_on();
    delay(time);
    led_off();

    index_open(false);
    delay(time);
    middle_open(false);
    delay(time);
    ring_open(false);
    delay(time);
    little_open(false);
  }
  if (x == "d") {
    middle_close(true);
    delay(time);
    ring_close(true);
    delay(time);
    little_close(true);
    led_on();
    delay(time);
    led_off();

    middle_open(true);
    delay(time);
    ring_open(true);
    delay(time);
    little_open(true);
  }
  if (x == "e") {
    thumb_close(true);
    delay(time);
    index_close(true);
    delay(time);
    middle_close(true);
    delay(time);
    ring_close(true);
    delay(time);
    little_close(true);
    led_on();
    delay(time);
    led_off();

    index_open(true);
    delay(time);
    middle_open(true);
    delay(time);
    ring_open(true);
    delay(time);
    little_open(true);
    delay(time);
    thumb_open(true);
  }
  if (x == "f") {
    thumb_close(true);
    delay(time);
    index_close(true);
    led_on();
    delay(time);
    led_off();

    index_open(true);
    delay(time);
    thumb_open(true);
  }
  if (x == "i") {
    thumb_close(true);
    delay(time);
    index_close(true);
    delay(time);
    middle_close(true);
    delay(time);
    ring_close(true);
    led_on();
    delay(time);
    led_off();

    index_open(true);
    delay(time);
    middle_open(true);
    delay(time);
    ring_open(true);
    delay(time);
    thumb_open(true);
  }
  if (x == "u") {
    thumb_close(true);
    delay(time);
    ring_close(true);
    delay(time);
    little_close(true);
    led_on();
    delay(time);
    led_off();

    ring_open(true);
    delay(time);
    little_open(true);
    delay(time);
    thumb_open(true);
  }
  if (x == "w") {
    thumb_close(true);
    delay(time);
    little_close(true);
    led_on();
    delay(time);
    led_off();

    little_open(true);
    delay(time);
    thumb_open(true);
  }
}
