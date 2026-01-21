# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 15:47:13 2026

@author: user
"""

## Questions:

#1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>

#2.  What is the difference between the continue and break statements in Python?
Difference between continue and break
break
Immediately stops the loop completely and exits it.
continue
Skips the current iteration and moves to the next iteration of the loop.
#3. Can you explain the difference between for loop and while loop?
for loop	while loop
Used when number of iterations is known
while loop
Used when condition-based
#4. How would you implement a nested for loop system? Provide an example.
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

## Homeworks:

#**1.** Return uncommon elements of lists. Order of elements does not matter.

"""
input:
    list1 = [1, 1, 2]
    list2 = [2, 3, 4]
output: [1, 1, 3, 4]



input:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
output: [1, 2, 3, 4, 5, 6]



input:
    list1 = [1, 1, 2, 3, 4, 2]
    list2 = [1, 3, 4, 5]
output: [2, 2, 5]
"""
def uncommon_elements(list1, list2):
    result = []

    for x in list1:
        if x not in list2:
            result.append(x)

    for x in list2:
        if x not in list1:
            result.append(x)

    return result


"""
**2.** Print the square of each number which is less than `n` on a separate line.


input: n = 5
output:
    1
    4
    9
    16
"""
"""
**3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.


input: hello
output: hel_lo



input: assalom
output: ass_alom



input: abcabcdabcdeabcdefabcdefg
output: abc_abcd_abcdeab_cdef_abcdefg

"""
def add_underscore(txt):
    vowels = "aeiou"
    result = ""
    count = 0

    for i in range(len(txt)):
        result += txt[i]
        count += 1

        if count == 3 and i != len(txt) - 1:
            if txt[i] not in vowels:
                result += "_"
                count = 0

    return result


"""
**4. Number Guessing Game**
Create a simple number guessing game.
- The computer randomly selects a number between 1 and 100. 
- If the guess is high, print "Too high!". 
- If the guess is low, print "Too low!". 
- If they guess correctly, print "You guessed it right!" and exit the loop.
- The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
- If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.


> Hint: Use Python’s `random.randint()` to generate the number.
"""
import random

while True:
    secret=random.randint(1, 100)
    attemps=10
    
    while attemps>0:
        guess=int(input("Guess the number: "))
        
        if guess> secret:
            print('Too high')
        elif guess<secret:
            print('Too low')
        else:
            print('You guessed it right')
            break
        
        attemps-=1
        
    if attemps==0:
        print('You lost.')
        
    again=input('wanna play again: (y, yes, ok)')
    if again.lower() not in ['y', 'yes', 'ok']:
        break


"""
**5. Password Checker**
Task: Create a simple password checker.
- Ask the user to enter a password. 
- If the password is shorter than 8 characters, print "Password is too short." 
- If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
- If the password meets both criteria, print "Password is strong."

"""
password=input("Enter your password: ")
if len(password)<8:
    print("Password too short.")
elif not any(c.isupper() for c in password):
    print("Your password should contain capital lettters. ")
else:
    print("Password accepted.")


"""
**6. Prime Numbers**
Task: Write a Python program that prints all prime numbers between 1 and 100.

> A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

---
"""
for num in range (2, 101):
    is_prime=True
    
    for i in range (2, int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)

"""
### Bonus Challenge
Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
- The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
- The player enters their choice.
- Display the winner and keep track of scores for the player and the computer.
- First to 5 points wins the match.

"""


choices=['rock, 'paper, 'scissors']
p_score=0
c_scrore=0

while p_score<5 and c_score<5:
    player=input("Enter rock/paper/scissors: ").lower()
    computer=random.choice(choices)
    print("Computer chose:", computer)
    
    if player==computer:
        print("Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        p_score+=list1
    else:
        print("Computer won this round!")
        computer_score+=1
    print("Ypur score:", p_score, "COmputer:", c_score)
    
print("Game over!")
