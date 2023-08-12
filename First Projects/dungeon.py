import time
def death():
    Print("Oh dear...")
    Print("I am afraid your journey ends here.")
    print()
    Print("-----YOU DIED-----")
def Print(string):
    for z in list(string):
        time.sleep(0.04)
        print(z,flush=True,end="")
    print()
    time.sleep(0.5)
Print("Hello there!")
Print("My name is Eric.")
answer=input(Print("What is 1+1?"))
if answer=="2":
    Print("I am glad to hear that!")
    Print("You passed the first test!!!!!")
    Print("A lot longer than my previous victim.")
    Print("I mean... friend.")
    Print("Yeah...")
else:
    death()
Print("Let's move on to something harder.")
answer=int(input(Print("What is 2*2*3*4*8?")))
if answer==384:
    Print("Wow...")
    Print("You're pretty good...")
else:
    death()
print()
Print("Let's try something non-math.")
answer=input(Print("Are you older than the Pantheon? y/n"))
if answer=="n":
    Print("Wow...")
    Print("So you know your history too...")
else:
    death()
print()
Print("Let's try some science.")
answer=input(Print("Is water made up of 2 hydrogen atoms and 1 oxygen atom? y/n"))
if answer=="y":
    Print("Congratulations!")
    Print("You have escaped my dungeon!")
    Print("You are the first to have accomplished such a mighty feat.")
    Print("But, I don't like you.")
    death()
else:
    death()