import winsound
import time
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

while 1:
    frequency = frequency + 100
    print(frequency)
    winsound.Beep(frequency, duration)
    # time.sleep(0.3)
