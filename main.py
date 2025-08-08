from datetime import datetime
import time

# Input alarm time
alarm_time = input("Enter the time of alarm to be set (HH:MM AM/PM): ").strip().upper()
print("Setting up alarm...")

while True:
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  # 12-hour format, with AM/PM

    if current_time == alarm_time:
        print("Wake Up!")
        break

    time.sleep(1)
