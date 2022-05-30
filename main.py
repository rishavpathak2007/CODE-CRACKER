import random 
import time 

print("Welcome to Code Cracker") 

def factorials(n): 
  if n == 1: 
    return 1
  else: 
    return n*factorials(n-1) 

def checkEvenOdd(n):
  if n % 2 == 0:
    return True 
  else: 
    return False

def countEven(n):
  count = 0 
  for x in n: 
    if checkEvenOdd(int(x)) == True: 
     count = count + 1 
  return count 
# print(countEven(str(678924)))
def caculateSum(n): 
  s = 0 
  for x in n: 
    s = s + int(x) 
  return s 

def calculateProduct(n): 
  p = 1 
  for x in n: 
    p = p * int(x) 
  return p 

integers = random.randint(3 , 5)
numzb = "1234567890" 
password = random.sample(numzb , integers) 
lives = factorials(integers) 
passwordSum = caculateSum(password) 
passwordProduct = calculateProduct(password) 
passwordEvenCount = countEven(password)
passwordOddCount = integers - passwordEvenCount
print("loading..")
time.sleep(3) 
password = "".join(password)
print("CODE IS GENERATED!")
print("It is " + str(integers) + " integers long")
print("The sum of the passcode is " + str(passwordSum)) 
print("The product of the passcode is " + str(passwordProduct)) 
print("The number of even numbers are " + str(passwordEvenCount)) 
print("The number of the odd numbers are " + str(passwordOddCount) )
print("The first number is " + str(password[0]))
print("The last number is " + str(password[-1])) 
print("The highest number is  " + str(max(password)))
print("The lowest number is " + str (min(password))) 
print("You have " + str (lives) + " lives ") 

while lives > 0:
  answer = input("What is your password: ") 
  if answer == password:
    print("Awesome! you have cracked the code, you are superb") 
    break 
  else: 
    lives = lives - 1 
    print("oops! your password is wrong ")
    print("You have " + str (lives) + " lives ") 
    if lives <= 1:
      print("GAME OVER! The password was " + str(password)) 

  