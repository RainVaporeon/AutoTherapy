#!/usr/bin/env python
import random

last_repeat = ""
repeat_count = 0

def determine_max_dot(message: str):
    return int(min(len(message) / 7, 30) + 5)

print("Say something, I'm listening...")
while True:
    prompt = input(">> ")
    if prompt == "":
        continue
    dots = "." * random.randint(1, determine_max_dot(prompt))
    if random.randint(0, 1) ^ (repeat_count > 2):
        if last_repeat != "crazy":
            repeat_count = 0
        print(f"<< That's crazy{dots}")
        last_repeat = "crazy"
    else:
        if last_repeat != "damn":
            repeat_count = 0
        print(f"<< damn{dots}")
        last_repeat = "damn"
    repeat_count = repeat_count + 1
