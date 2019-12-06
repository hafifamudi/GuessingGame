#Author by Hafif Nur Muhammad | Simple Game Written in Python 3

#import the os and time module for create animation
import os,time
os.system('clear')
filenames = ["animate1.txt","animate2.txt"]
#create the game function
def check_answer(guess,answer):
 #make global varaible for access the variable from the outside function
 global score
 still_guessing = True
 attempt = 0
 while still_guessing and attempt < 3:
	 #make sure the user input the function in lower case
	 if guess.lower() == answer.lower():
		 print('Correct Answer')
		 score = score + 1
		 still_guessing = False
	 else:
		 if attempt < 2:
			 guess = input('Sorry Wrong Answer Try Again ')
		 attempt = attempt + 1
 if attempt == 3:
	 print('The correct Answer is ' + answer)

#Function for the animation
def animation(filesnames,delay = 1,repeat = 10):
 frames = []
 for name in filenames:
  with open(name,"r",encoding="utf8") as f:
   frames.append(f.readlines())

 for i in range(repeat) :
  for frame in frames:
   print("".join(frame))
   time.sleep(delay)
#    os.system('clear')
animation(filenames,delay = 1,repeat=2)
#initialiaze the score variable      
score = 0 
#Give the user Choice to play the game or not
#Print the Title of the game
print('  ________                            .__                   ________                       ')
print(' /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  ')
print('/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ ')
print('\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ ')
print(' \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >')
print('        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ ')
#Lets start the game 
print()
def main():
	play_game = input('Do you want tou start the Game? (Yes/No)')
	if play_game == 'Yes':
	 #make the exercise and give the user input
	 guess3 = input('Which is the largest animal?\n\
 A)Blue Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
 Type A, B, C, D => ')
	 #call the game function
	 check_answer(guess3, 'A')
	 print()
	 guess2 = input('which is the great rapteal?\n\
 A) Cobra\n B) Boa\n C) Python\n D) Snake\n\
 Type A, B, C, D => ')
	 check_answer(guess2,'D')
	 print()
	 guess1 = input('which is the killer animal?\n\
 A) Cobra\n B) Bear\n C) Lion\n D) Tiger\n\
 Type A, B, C, D => ')
	 check_answer(guess1,'A')
	 print('Your Score is ' + str(score))
	 
	 
	else:
	 print('Oke see you next time :)')

#call the function
main()
#for repeat the game
repeat_game = input('Do you want to play the game again ? (Yes/No) ')
if repeat_game == 'Yes':
	main()
else:
	print('Oke see you next time :)')
