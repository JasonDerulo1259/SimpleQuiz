import art
import time
import random
import os
import sys
from art import *
#really large variable below
#Ignore this:
multiquest=("Who was the first Queen of England?"," Who won the Best Actor Oscar in 2020?"," How many counties are there in the UK?"," a) 48 b) 58, c) 68 Which American band had a 1997 UK number one single with Dont Speak?"," Which US actor plays the title character in the movie franchise Deadpool?"," What is the common name for the home of a badger?"," Joseph Smith Jr. founded which religious movement?"," What is the first name of the presenter of Beadles About!, an ITV practical jokes programme which ran from 1986 to 1996?"," What is commonly known as the national fruit of India?"," The City Ground is been the home of which English football club?"," Who did Queen Elizabeth II surpass as Britains longest serving monarch in September 2015?"," Which word game invented by Allan Turoff features a grid of lettered dices?"," Which is the eighth and furthest-known planet from the sun in the solar system?"," Which mammal has the largest brain by weight, a human or a sperm whale?"," Which club does former Chelsea boss Jose Mourinho manage now?"," Coco, Cars and Inside Out are all films produced by which US animated film company?"," What was the busiest London Underground station last year?"," Sandie Shaw won which European music event in 1967 with Puppet on a String?"," In which century did Charlotte Brontë write Jane Eyre?"," S. O. S. is a common example of which electrical telegraph communication system?"," Which Conservative MP became Leader of the House in July 2019?"," The Chronicles of Narnia is a childrens book series written by which author?"," Which first name is shared by Cricketer Flintoff and Tennis player Murray?"," Who was the second US president?"," Who presented the original Through The Keyhole?"," What is the name of the paper company where the UK version of The Office is based?"," What was the name of Guns N Roses famous debut album?"," The Merry Hill Shopping Centre is in which Midland town?"," Which famous British figure died on 24 January 1965?"," How much of the human body is water?"," Where would you find the Sea of Tranquility?"," Who is the missing member of the original Queen band?"," Freddie Mercury, Brian May, _____ _____ and John Deacon. Which King of England was crowned on Christmas Day?"," What is Vic Reeves real name?"," What is the only mammal that cannot jump?"," What is Englands largest county with no coastline?"," What is the Queens surname?"," How many pounds are in a stone?"," Which woman is mentioned most in The Bible?"," What is the capital of Turkey?"," Z and which other letter are worth the most in Scrabble?")
#just ignore that ^^^
#code starts here vvv
def massprint(string,int):
  againagain = int
  while againagain >= 0:
    print(string,flush=True, end=" ")
    time.sleep(0.01)
    againagain -= 1
  if againagain<=1:
    print(" ")
    print(" ")

def quickfire():
  againagainagain=30
  while againagainagain >=0:
    randmultiquest=random.choice(multiquest)
    print(randmultiquest)
    time.sleep(0.2)
    againagainagain-=1
#Functions/Definitions Above ^^^
goagain="y"
score=0
correct=("Well Done!","That's Right!","Wow! That's Correct!","Yep, That's it!", "You got it")
incorrect=("Nope.","Sorry mate, That's wrong","That's wrong","Incorrect mate.","How dumb are you?","Thats not it.")
randcorrect=random.choice(correct)
randincorrect=random.choice(incorrect)
#Variables/Randoms Above ^^^
while goagain=="y":
  os.system("clear")
  print("\033[1;32;40mHello!")
  time.sleep(1)
  print("Welcome To the quiz! Are you ready?")
  time.sleep(2)
  print("\033[1;33;40m3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(2)
  print("\033[1;32;40mQuestion One:")
  print("What is this website called?")
  time.sleep(1)
  print("a, Codecademy")
  print("b, repl.it")
  print("c, SimpleQuiz")
  print("d, JohnHasAGreatTimeCodingSomethingThatIsUsefulForAbsolutelyNothing.com")
  answer=input("\033[1;34;40mPut in the letter:")
  randcorrect=random.choice(correct)
  randincorrect=random.choice(incorrect)
  if "b"==answer:
    time.sleep(1)
    print("\033[1;32;40m",randcorrect)
    score=score+1
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  if "b"!=answer:
    time.sleep(1)
    print("\033[1;32;40m",randincorrect,)
    time.sleep(1)
    print("The Correct answer was repl.it")
    time.sleep(1)
    print("If you put 'repl.it', It does not count. Make sure you put in the letter. (b)")
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  time.sleep(2)
  print("\033[1;32;40mQuestion two:")
  time.sleep(2)
  print("\033[1;32;40mWhat Is this program/project called?")
  time.sleep(1)
  print("a, SimpleQuiz")
  print("b, Chatbot")
  print("c, ComplexQuiz")
  print("d, ThisIsNotAJokeNameIPromiseAlrightThisIsTheRealOneChooseLetterD")
  answer=input("\033[1;34;40mPut in the letter:")
  randcorrect=random.choice(correct)
  randincorrect=random.choice(incorrect)
  if "a"==answer:
    time.sleep(1)
    print("\033[1;32;40m",randcorrect)
    score=score+1
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  if "a"!=answer:
    time.sleep(1)
    print("\033[1;32;40m",randincorrect)
    time.sleep(1)
    print("The Correct answer was 'a' (make sure to only put the letter, Not the name.)")
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  time.sleep(1)
  print("\033[1;32;40mAlright Alright, That was too easy.")
  time.sleep(2)
  print("ooh! I have a tricky one!")
  time.sleep(2)
  print("Question Three:")
  time.sleep(2)
  print("What word is spelled incorrectly in every single dictionary?")
  time.sleep(1)
  answer=input("\033[1;34;40mType in the response \033[1;31;40m(full word)\033[1;34;40m:")
  randcorrect=random.choice(correct)
  randincorrect=random.choice(incorrect)
  if "incorrectly" in answer:
    time.sleep(1)
    print("\033[1;32;40m",randcorrect)
    time.sleep(1)
    print("but how did you know that?")
    time.sleep(0.5)
    print("it was meant to be hard...")
    score=score+1
    time.sleep(2)
    print("whatever,")
    time.sleep(1)
    print("\033[1;37;40mYour current score is",score)
  if "incorrectly" not in answer:
    time.sleep(1)
    print("\033[1;32;40m",randincorrect)
    time.sleep(1)
    print("The Correct answer was the word 'Incorrectly'")
    time.sleep(2)
    print("Told you it was tricky!")
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  time.sleep(2)
  print("\033[1;32;40mOkay, I think that's enough of that now.")
  time.sleep(1)
  print("how about some different ones.")
  time.sleep(2)
  print("Question Four:")
  time.sleep(2)
  print("What is the Capital City of France")
  time.sleep(2)
  print("A. Bristol")
  time.sleep(0.2)
  print("B. New Guinea")
  time.sleep(0.2)
  print("C. Paris")
  time.sleep(0.2)
  print("D. Athens")
  answer=input("\033[1;34;40mPut in the letter:")
  randcorrect=random.choice(correct)
  randincorrect=random.choice(incorrect)
  if "c"==answer:
    time.sleep(1)
    print("\033[1;32;40m",randcorrect)
    time.sleep(2)
    score=score+1
    print("Your current score is",score)
  if "c"!=answer:
    time.sleep(1)
    print("\033[1;32;40m",randincorrect)
    time.sleep(1)
    print("The Correct answer was c")
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  time.sleep(2)
  print("Question Five.")
  time.sleep(2)
  print("What is the name of the account this was created by")
  time.sleep(1)
  print("a, MichaelGordon1")
  print("b, MichaelGordon")
  print("c, MichaleGorden1")
  print("d, MichaelGordon1.com")
  answer=input("\033[1;34;40mPut in the letter:")
  randcorrect=random.choice(correct)
  randincorrect=random.choice(incorrect)
  if "a"==answer:
    time.sleep(1)
    print("\033[1;32;40m",randcorrect)
    score=score+1
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  if "a"!=answer:
    time.sleep(1)
    print("\033[1;32;40m",randincorrect,)
    time.sleep(1)
    print("The Correct answer was repl.it")
    time.sleep(1)
    print("Make sure you put in the letter, Not the name. (a)")
    time.sleep(2)
    print("\033[1;37;40mYour current score is",score)
  time.sleep(2)
  print("\033[1;32;40mUgghhh quizzes are really boring arent they?")
  time.sleep(1)
  print("do you wanna do something else? ")
  answer=input("\033[1;34;40my/n: ")
  if "y" in answer:
    time.sleep(2)
    massprint("\033[1;32;40mha",200)
    print(" ")
    time.sleep(1)
    print("\033[1;32;40mIt Never Ends You Idiot.")
    time.sleep(2)
    os.system("clear")
  if "n" in answer:
    time.sleep(2)
    print("\033[1;32;40mFine. Lets do some more")
  time.sleep(2)
  print("Ready?")
  time.sleep(1)
  print("Cause Here comes the quickfire questions")
  time.sleep(2)
  print("\033[1;32;40mHere we go")
  randmultiquest=random.choice(multiquest)
  time.sleep(1)
  print(" ")
  quickfire()
  time.sleep(2)
  os.system("clear")
  time.sleep(1)
  print("\033[1;32;40mOnly Joking, The Quiz Is over")
  time.sleep(1)
  print("Oh! Actually, One more question...")
  time.sleep(2)
  print("Did you like the quiz")
  answer=input("\033[1;34;40my/n: ")
  if "y" in answer:
    time.sleep(1)
    print("\033[1;32;40mThanks mate.")
    score=score+1
    time.sleep(2)
  if "y" not in answer:
    time.sleep(1)
    print("\033[1;32;40mHOW DARE YOU")
    print("\033[1;32;40mTHE CORRECT ANSWER WAS YES >:(((")
    time.sleep(1)
    print("\033[1;32;40mYOURE WRONG THE QUIZ WAS GOOD I AM ANGRY NOW >:(")
    time.sleep(1)
    massprint(">:(",200)
  time.sleep(2)
  os.system("clear")
  time.sleep(1)
  print("Your final score was",score)
  time.sleep(2)
  if score>=5:
    print("Well done! You got perfect scores!")
  elif score==4 or score==3 or score==2:
    print("Hmm, Not perfect scores. But not terrible either!")
  elif score ==1:
    print("Damn, You're Bad, Try harder")
  else:
    print("Jesus christ HOW ARE YOU THAT BAD?!?! I mean honestly, How did you get none right")
    time.sleep(2)
    print("You didnt even get the one about the capital city of France right.")
    time.sleep(2)
    print("Thanks for wasting my time with your unfathomable stupidy")
    time.sleep(2)
    print("Now get out of my sight.")
    time.sleep(2)
    os.system("clear")
    time.sleep(1)
    tprint("idiot",font='doh')
  time.sleep(3)
  os.system("clear")
  time.sleep(1)
  goagain=input("\033[1;33;40mDo you want to go again? (y/n): ")
os.system("clear")
time.sleep(1)
print("Alright then, Goodbye :)")
time.sleep(1)
exit()