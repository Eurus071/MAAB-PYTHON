# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 18:49:27 2026

@author: user
"""

### Task 1

def convert_cel_to_far(celsius):
    return celsius * 9 / 5 + 32


def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Convert Fahrenheit to Celsius
f = float(input("Enter a temperature in degrees F: "))
c_result = convert_far_to_cel(f)
print(f"{f} degrees F = {c_result:.2f} degrees C\n")

# Convert Celsius to Fahrenheit
c = float(input("Enter a temperature in degrees C: "))
f_result = convert_cel_to_far(c)
print(f"{c} degrees C = {f_result:.2f} degrees F")


### Task 2

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")


# User input
principal = float(input("Enter the initial amount: "))
annual_rate = float(input("Enter the annual rate of return (e.g., 0.05 for 5%): "))
num_years = int(input("Enter the number of years: "))

# Call the function
invest(principal, annual_rate, num_years)

### Task 3

# Ask the user for a positive integer
n = int(input("Enter a positive integer: "))

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    if n % i == 0:
        print(f"{i} is a factor of {n}")


### Task 4

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(data):
    students = []
    tuition = []

    for uni in data:
        students.append(uni[1])
        tuition.append(uni[2])

    return students, tuition


def mean(values):
    return sum(values) / len(values)


def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]


# Get enrollment and tuition data
students, tuition = enrollment_stats(universities)

# Calculations
total_students = sum(students)
total_tuition = sum(tuition)

student_mean = mean(students)
student_median = median(students)

tuition_mean = mean(tuition)
tuition_median = median(tuition)

# Output
print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")

print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}\n")

print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("*" * 30)


### Task 5

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
