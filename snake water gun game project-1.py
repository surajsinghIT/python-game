#projecr-1
#snake water gun game or rock paper scissor

def gam(comp,you):
    if comp==you:
        return None
    if comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
        elif comp=="w":
            if you=="g":
                return False
            elif you=="s":
                return True
        elif comp=="g":
            if you=="s":
                return False
            elif you=="w":
                return True
                

print("comp turn:snake(s) water(w) or gun(g)?")
import random
randno=random.randint(1,3)
if randno==1:
    comp ="s"
elif randno==2:
    comp ="w"
elif randno==3:
        comp= "g"
       
you=input("your turn :snake(s) water(w)or  gun(g):\n choose between the above:")
a=gam(comp,you)
print("comp choose ",comp)
print("you choose ",you)

if a==None:
    print("the game is a tie!")
elif a:
    print("you win!")
else:
    print("you loose!")

