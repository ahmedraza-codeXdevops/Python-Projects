numbers = [4, 2, 4, 7, 2, 4, 9, 7, 7, 7]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

most_frequent = None
least_frequent = None

for num in frequency:
    if most_frequent is None or frequency[num] > frequency[most_frequent]:
        most_frequent = num

    if least_frequent is None or frequency[num] < frequency[least_frequent]:
        least_frequent = num

print("Frequency:", frequency)
print("Most frequent:", most_frequent)
print("Frequency:", frequency[most_frequent])
print("Least frequent:", least_frequent)
print("Frequency:", frequency[least_frequent])