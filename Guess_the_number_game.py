import random
counter=0
print("Hi, What is your name")
name=input()
N1=random.randint(1,10)
print("Well,"+name+", i am thinking of a number now from 1 to 10")
while counter<6:
    print("Enter your Guess")
    N2=input()
    N2=int(N2)
    counter=counter+1
    if N2>N1:
        print("Your guess is too high")
    if N2<N1:
        print("Your guess is too low")
    if N2==N1:
        break
if N1==N2:
    counter=str(counter)
    print('Good Job, '+name+' You guessed my number in '+counter+' Gusses!')

if N2!= N1:
    N1=str(N1)
    print('Nope,The number I thinking was'+N1)
