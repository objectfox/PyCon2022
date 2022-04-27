"""This example requires seven wav files from the audio folder in Default_Files on the PyCon2022 GitHub
repo. Download the files and copy them to your CIRCUITPY drive. Once copied, try touching the touch
pads on A1-A6 and TX to hear a funky scale of notes!"""
import time
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched A1!")
        cp.play_file("1.wav")
    if cp.touch_A2:
        print("Touched A2!")
        cp.play_file("2.wav")
    if cp.touch_A3:
        print("Touched A3!")
        cp.play_file("3.wav")
    if cp.touch_A4:
        print("Touched A4!")
        cp.play_file("4.wav")
    if cp.touch_A5:
        print("Touched A5!")
        cp.play_file("5.wav")
    if cp.touch_A6:
        print("Touched A6!")
        cp.play_file("6.wav")
    if cp.touch_TX:
        print("Touched TX!")
        cp.play_file("7.wav")
    time.sleep(0.1)
