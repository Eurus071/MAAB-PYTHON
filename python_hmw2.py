# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 12:52:17 2026

@author: user
"""

### Number Data Type Questions:

# 1. Create a program that takes a float number as input and rounds it to 2 decimal places.
a=round(float(input("Enter the number: ")), 2)
print(a)

#2. Write a Python file that asks for three numbers and outputs the largest and smallest.

first=float(input("Input the first number: "))
second=float(input("Input the second number: "))
third=float(input("Input the third number: "))
print("Smallest of all: ", min(first, second, third))
print("Largest of all: ", max(first, second, third))

#3. Create a program that converts kilometers to meters and centimeters.
km = float(input("Enter distance in kilometers: "))

meters = km * 1000
centimeters = km * 100000

print(str(km) +" is in Meters:", meters)
print(str(km)+" is in Centimeters:", centimeters)

#4. Write a program that takes two numbers and prints out the result of integer division and the remainder.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

quotient = a // b
remainder = a % b

print("Integer division result:", quotient)
print("Remainder:", remainder)

#5. Make a program that converts a given Celsius temperature to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

#6. Create a program that accepts a number and returns the last digit of that number.
num = int(input("Enter a number: "))
last_digit = abs(num) % 10
print("Last digit:", last_digit)

#7. Create a program that takes a number and checks if it’s even or not.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

### String Questions:

#1. Create a program to ask name and year of birth from user and tell them their age.
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

age = 2026 - birth_year
print(f"{name}, you are {age} years old.")

#2. Extract car names from this text: txt = 'LMaasleitbtui'
txt = "LMaasleitbtui"
cars = txt[1::2]
print(cars)

#3. Write a Python program to:
#   - Take a string input from the user.
#   - Print the length of the string.
#   - Convert the string to uppercase and lowercase.
text = input("Enter a string: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


#4. Write a Python program to check if a given string is `palindrome` or not.
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#> What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.

#5. Write a program that counts the number of vowels and consonants in a given string.
text = input("Enter a string: ").lower()
vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

#6. Write a Python program to check if one string contains another.
s1 = input("Enter main string: ")
s2 = input("Enter substring: ")

print(s2 in s1)

#7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
#Example:  
#   - Input sentence: "I love apples."  
#   - Replace: "apples"  
#   - With: "oranges"  
#   - Output: "I love oranges."
sentence = input("Enter a sentence: ")
old = input("Word to replace: ")
new = input("Replace with: ")

print(sentence.replace(old, new))

#8. Write a program that asks the user for a string and prints the first and last characters of the string.  
text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])

#9. Ask the user for a string and print the reversed version of it.
text = input("Enter a string: ")
print(text[::-1])

#10. Write a program that asks the user for a sentence and prints the number of words in it.  
sentence = input("Enter a sentence: ")
words = sentence.split()

print("Number of words:", len(words))

#11. Write a program to check if a string contains any digits.  
text = input("Enter a string: ")

has_digit = any(ch.isdigit() for ch in text)
print(has_digit)

#12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  
words = ["Python", "is", "awesome"]
result = "-".join(words)

print(result)

#13. Ask the user for a string and remove all spaces from it.  
text = input("Enter a string: ")
print(text.replace(" ", ""))

#14. Write a program to ask for two strings and check if they are equal or not.  
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(s1 == s2)

#15. Ask the user for a sentence and create an acronym from the first letters of each word.  
#    Example:  
#    - Input: "World Health Organization"  
#    - Output: "WHO"  

sentence = input("Enter a sentence: ")
acronym = "".join(word[0].upper() for word in sentence.split())

print(acronym)

#16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
text = input("Enter a string: ")
char = input("Enter a character to remove: ")

print(text.replace(char, ""))

#17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
text = input("Enter a string: ")
vowels = "aeiouAEIOU"

for v in vowels:
    text = text.replace(v, "*")

print(text)

#18. Write a program that checks if a string starts with one word and ends with another.  
#    Example:  
#    - Input: "Python is fun!"  
#    - Starts with: "Python"  
#    - Ends with: "fun!"  
text = input("Enter a sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")

print(text.startswith(start) and text.endswith(end))


### Boolean Data Type Questions:
#1. Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter username: ")
password = input("Enter password: ")

if username and password:
    print("Username and password are valid.")
else:
    print("Username or password cannot be empty.")

#2. Create a program that checks if two numbers are equal and outputs a message if they are.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

#3. Write a program that checks if a number is positive and even.
num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")

#4. Write a program that takes three numbers and checks if all of them are different.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

#5. Create a program that accepts two strings and checks if they have the same length.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2):
    print("Strings have the same length.")
else:
    print("Strings have different lengths.")

#6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

#7. Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a + b > 50:
    print("The sum is greater than 50.")
else:
    print("The sum is not greater than 50.")
