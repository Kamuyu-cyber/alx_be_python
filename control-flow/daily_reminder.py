#!/usr/bin/env python3
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_message = f"Reminder: '{task}' is a low priority task"
    case _:
        base_message = f"Reminder: '{task}' has an invalid priority"

if time_bound == "yes":
    print(base_message + " that requires immediate attention today!")
else:
    print(base_message + " and does not require immediate attention today.")
