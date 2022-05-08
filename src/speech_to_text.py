import sys
import time
import cv2
from to_arduino import Arduino
import speech_recognition as sr


class speech_to_asl:
    def __init__(self):
        self.detected_text = ""
        self.words = []
        self.letters = []
        self.arduino = Arduino()

    def detect_speech(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Recording')
            audio_data = r.record(source, duration=5)
            print("Recognizing...")
            try:
                self.detected_text = r.recognize_google(audio_data, language='en-US')
            except:
                return None
            print(self.detected_text)
            return self.detected_text

    def speech_to_letters(self):
        self.detected_text = self.detected_text.lower()
        self.words.append(self.detected_text.split())
        # print(self.words)
        self.letters = list(self.detected_text)
        print(self.letters)
        for letter in self.letters:
            value = self.arduino.send(letter)
            while value != letter:
                value = self.arduino.send(letter)
            print('Displaying: ', letter)
            s_asl.display_letter(letter)

    def display_letters(self):
        default = cv2.imread('../Resources/ASL/Space.png')
        default = cv2.resize(default, (138, 167))
        while len(self.letters) != 0:
            to_display = self.letters.pop(0)
            if to_display == ' ':
                to_display = 'Space'
            else:
                to_display = to_display.upper()
            path = '../Resources/ASL/' + to_display + '.png'
            try:
                image = cv2.imread(path)
            except:
                print('Can\'t display symbol')
            image = cv2.resize(image, (138, 167))
            cv2.imshow('ASL', image)
            cv2.waitKey(500)
            cv2.imshow('ASL', default)
            cv2.waitKey(150)

    def display_letter(self, letter):
        to_display = letter
        if to_display == ' ':
            to_display = 'Space'
        else:
            to_display = to_display.upper()
        path = '../Resources/ASL/' + to_display + '.png'
        try:
            image = cv2.imread(path)
        except:
            print('Can\'t display symbol')
        image = cv2.resize(image, (138, 167))
        cv2.imshow('ASL', image)
        cv2.waitKey(3000)


if __name__ == '__main__':
    s_asl = speech_to_asl()
    done = False
    while not done:
        if not s_asl.detect_speech():
            print("Please Try Again!")
        else:
            done = True
            s_asl.speech_to_letters()
