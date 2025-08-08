Python Alarm Clock ⏰
A simple command-line Python program that lets you set an alarm and get notified when the current time matches the alarm time.

Features
Uses 12-hour time format (HH:MM AM/PM).

Works with both AM and PM.

Checks the system clock every second.

Lightweight and runs directly in the terminal.

How It Works
The program prompts you to enter the alarm time in the format HH:MM AM/PM.

It continuously checks the current system time.

When the current time matches the alarm time, it displays "Wake Up!".

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
Requirements
Python 3.x installed on your system.

How to Run
Save the script as alarm_clock.py.

Open your terminal or command prompt.

Navigate to the folder where the script is saved.

Run:

bash
Copy
Edit
python alarm_clock.py
Enter your desired alarm time when prompted.

Notes
The format must be HH:MM AM/PM (e.g., 07:05 PM).

The alarm triggers at the exact minute you set.

Press Ctrl + C to stop the program before it rings.
