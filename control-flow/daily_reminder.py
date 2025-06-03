#!/usr/bin/env python3
task = input("Enter your task: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

reminder = f"Reminder: Your task '{task}' is {priority} priority"
match priority:
    case "high":
        reminder += " and should be addressed urgently"
    case "medium":
        reminder += " and should be handled today"
    case "low":
        reminder += " and can be addressed when convenient"
    case _:
        reminder += ", but the priority level is unrecognized"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder + ".")
