import random
import time
#the theme is very cool and awesome names for your first-born son
words=["sephiroth","waluigi","zekrom"]
select=random.randint(1,3)
a="_"
b="_"
c="_"
d="_"
e="_"
f="_"
g="_"
h="_"
i="_"
j="_"
k="_"
l="_"
m="_"
n="_"
o="_"
p="_"
q="_"
r="_"
s="_"
t="_"
u="_"
v="_"
w="_"
x="_"
y="_"
z="_"
#Sephiroth
if select==1:
    incorrect=[]
    remaining=10
    while remaining>0:
        print(s,e,p,h,i,r,o,t,h)
        if s=="s" and e=="e" and p=="p" and h=="h" and i=="i" and r=="r" and o=="o" and t=="t":
            print('You win! The word is "Sephiroth"')
            time.sleep(0.5)
            exit()
        print("Incorrect guesses remaining:",remaining)
        if len(incorrect) != 0:
            print("Incorrect letters:", end=" ")
            for blah in range (len(incorrect)):
                print(incorrect[blah], end=" ")
        guess=input("\nInput a letter: ")
        if guess.lower()=="s":
            s="s"
        elif guess.lower()=="e":
            e="e"
        elif guess.lower()=="p":
            p="p"
        elif guess.lower()=="h":
            h="h"
        elif guess.lower()=="i":
            i="i"
        elif guess.lower()=="r":
            r="r"
        elif guess.lower()=="o":
            o="o"
        elif guess.lower()=="t":
            t="t"
        else:
            incorrect.append(guess)
            remaining=remaining-1
            if remaining==0:
                print("\nYou have run out of guesses. You lose.")
                exit()
        print("\n \n \n")
#Waluigi
if select==2:
    incorrect=[]
    remaining=10
    while remaining>0:
        print(w,a,l,u,i,g,i)
        if w=="w" and a=="a" and l=="l" and u=="u" and i=="i" and g=="g":
            print('You win! The word is "Waluigi"')
            time.sleep(0.5)
            exit()
        print("Incorrect guesses remaining:",remaining)
        if len(incorrect) != 0:
            print("Incorrect letters:", end=" ")
            for blah in range (len(incorrect)):
                print(incorrect[blah], end=" ")
        guess=input("\nInput a letter: ")
        if guess.lower()=="w":
            w="w"
        elif guess.lower()=="a":
            a="a"
        elif guess.lower()=="l":
            l="l"
        elif guess.lower()=="u":
            u="u"
        elif guess.lower()=="i":
            i="i"
        elif guess.lower()=="g":
            g="g"
        else:
            incorrect.append(guess)
            remaining=remaining-1
            if remaining==0:
                print("\nYou have run out of guesses. You lose.")
                exit()
        print("\n \n \n")
#Zekrom
if select==3:
    incorrect=[]
    remaining=10
    while remaining>0:
        print(z,e,k,r,o,m)
        if z=="z" and e=="e" and k=="k" and r=="r" and o=="o" and m=="m":
            print('You win! The word is "Zekrom"')
            time.sleep(0.5)
            exit()
        print("Incorrect guesses remaining:",remaining)
        if len(incorrect) != 0:
            print("Incorrect letters:", end=" ")
            for blah in range (len(incorrect)):
                print(incorrect[blah], end=" ")
        guess=input("\nInput a letter: ")
        if guess.lower()=="z":
            z="z"
        elif guess.lower()=="e":
            e="e"
        elif guess.lower()=="k":
            k="k"
        elif guess.lower()=="r":
            r="r"
        elif guess.lower()=="o":
            o="o"
        elif guess.lower()=="m":
            m="m"
        else:
            incorrect.append(guess)
            remaining=remaining-1
            if remaining==0:
                print("\nYou have run out of guesses. You lose.")
                exit()
        print("\n \n \n")