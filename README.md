Python Alarm Clock ⏰
A simple command-line Python program that lets you set an alarm and get notified when the current time matches the alarm time.

Features
Works with 12-hour format (HH:MM AM/PM).

Checks the time every second.

Handles both AM and PM correctly.

Lightweight and runs in the terminal.

How It Works
You enter the alarm time in HH:MM AM/PM format.

The program compares the current system time to the alarm time.

When they match, the program prints "Wake Up!".

Example
Input:

pgsql
Copy
Edit
Enter the time of alarm to be set (HH:MM AM/PM): 07:30 AM
Output:

mathematica
Copy
Edit
Setting up alarm...
Wake Up!
Code
python
Copy
Edit


Python 3.x

How to Run
Save the script as alarm_clock.py.

Open a terminal in the same folder.

Run:

bash
Copy
Edit
python alarm_clock.py
Enter the alarm time when prompted.

Notes
You must use HH:MM AM/PM format (e.g., 07:05 PM).

The program will match the exact minute — it will ring as soon as the clock reaches your set time.

To stop the program before the alarm triggers, press Ctrl + C in the terminal.

