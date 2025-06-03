#!/usr/bin/env python3
task = input("Task: ")
priority = input("Priority: ").lower()
time_bound = input("Time Bound: ").lower()

reminder = f"Reminder: Your task '{task}' with {priority} priority"
match priority:
    case "high":
        reminder += " requires urgent attention"
    case "medium":
        reminder += " should be completed today"
    case "low":
        reminder += " can be done later"
    case _:
        reminder += " has an unrecognized priority"

if time_bound == "yes":
    reminder += " and immediate action is required"

print(reminder + ".")
