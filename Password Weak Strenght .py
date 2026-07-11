import re

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search("[A-Z]", password):
    score += 1

if re.search("[a-z]", password):
    score += 1

if re.search("[0-9]", password):
    score += 1

if re.search("[@#$%^&*!]", password):
    score += 1

levels = {
    1: "Very Weak",
    2: "Weak",
    3: "Medium",
    4: "Strong",
    5: "Excellent"
}

print("Password Strength:", levels.get(score, "Very Weak"))