# Speech-To-ASL
Changes Speech to American Sign Language

![Hand](https://user-images.githubusercontent.com/97162452/167584723-996113b8-c4d6-47f8-a1f2-2b8b7b80813e.png)

## Branches

### Pyserial
* Enables the communication between python and Arduino.
* Performs speech recognition.
* Converts speech to text.
* Sneds the letters to the Arduino

###Arduino

* Receives the letters through pyserial.
* Controls the servos to convey the letter received

###MATLAB
![MATLAB](https://user-images.githubusercontent.com/97162452/167585680-59272525-0923-4f89-aaca-a4fca306f695.png)

* Simulink model that displays all the ASL letters
* Controlled by servo motors

