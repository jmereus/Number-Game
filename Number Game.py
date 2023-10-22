
import time
import random


b=random.randrange(1,6)

print("This is the number guessing game")
time.sleep(2.0)
print("Each round gets easier, but you need to get through all three to win")
time.sleep(3.0)
correct_guess= False

while(correct_guess==False):
    print("Guess a number from 1 to 10")
    a=random.randrange(1,11)
    ai=int(input("Round 1:"))
   


    if a== ai:
        correct_guess=True
        print("Great Guess!!",a,"is correct!")
        print("Ok, now onto Round 2")
        time.sleep(1.0)
        print("Guess a number from 1 to 5")
        c=random.randrange(1,4)
        ai_2=int(input("Round 2:"))
        if ai_2== b:
             print("Great Guess!!",b,"is correct!")
             time.sleep(1.0)
             print("Ok last round you got this")
             print("Guess a number from 1 to 3")
             ai_3=int(input("Round 3:"))
             if ai_3==c:
                print("....") 
                time.sleep(3.0)
                print("Congratulations You Win!!!")
                
                ai_4=input("Want to Play again? Y/N")
                if ai_4=="Y" or ai_4=="y" or ai_4=="yes" or ai_4=="Yes":
                    correct_guess=False
                else:
                    time.sleep(1.0)
             elif ai_3 < 1 or ai_3 > 3:
                print("YOU BLEW IT THAT'S NOT 1-3!!")
                correct_guess=False
             else:
                print("....")
                time.sleep(3.0)
                print("SOOO CLOSE THE NUMBER WAS", c)
                time.sleep(1.5)
                print("I wouldn't blame you if you quit")
                correct_guess=False


        elif ai_2 < 1 or ai_2 > 5:
            print("That's not 1-5 you lose lol")
            time.sleep(1.5)
            correct_guess=False
        else:
            print("Nice try the number was",b)
            time.sleep(1.5)
            print("Let's try again from the top")
            time.sleep(1.5)
            correct_guess=False
     

    elif ai < 1 or ai > 10:
        print("That's not 1-10 you lose lol")
        time.sleep(1.0)
    elif ai == a-1 or ai==a+1:
        print("SO CLOSE!")
        time.sleep(1.0)
        print("The number was",a)
        time.sleep(1.0)
    elif ai == a+2 or ai == a-2 or ai == a-3 or ai == a+3:
        print("Almost had it")
        time.sleep(1.0)
        print("The number was",a)
        time.sleep(1.0)
        print("Try Again")
    else:
        print("A bit off")
        print("The number was",a)
        time.sleep(1.5)
        print("Try Again")
        time.sleep(1.0)
        
