import random
print('*'*60,'WELCOME TO THE WORD GUESSING GAME','*'*60)
print()
print()
level=int(input('Level 1: Eassy (length of Word < 6) \nLevel 2: Medium (length of Word < 8)\nLevel 3: Hard (length of Word > 8) \n \nselect Level(1,2,3) : '))


def retry():
    if level==1:
        words=['Bread','Brush','Chair','Chest','Chord','Click','Clock','Cloud','Dance',
              'Diary','Drink','Earth','Flute','Fruit','Ghost','Grape','Green','Happy','Heart','House','Juice','Light','Money','Music','Party','Pizza','Plant','Radio','River','Salad','Sheep','Shoes'
              'Smile','Snack','Snake','Spice','Spoon','Storm','Table','Toast','Tiger','Train','Water','Whale','Wheel','Woman','World','Write','Youth']

    elif level==2:
        words=['Ability','Backing','Cabinet','Absence','Balance','Caliber','Academy','Banking','Calling','Account','Barrier','Capable','Accused','Battery','Capital','Achieve','Bearing','Captain','License','Nothing','Million','Limited','Nowhere','Mineral','Listing','Nuclear',
              'Minimal','Logical','Nursing','Minimum','Loyalty','Pacific','Missing','Obvious','Package','Mission','Offense','Painted','Mistake']
    
    elif level==3:
        words=['Feedback','Programming','Computer','Exchange','Football','Function','Graphics','Keyboard','Maturity','Location','Printing','Platform','Backbitten','Bulletproof','Calculator','Deadlift','Friendship']    

    random_word = random.choice(words)
    random_words = list(random_word)
    random.shuffle(random_words)
    print(' '*30,random_words)


    for i in range(1,4):
        print('chance left: ', 4-i)
        guessed_word = input('Guess the word: ' )
        if guessed_word==random_word:
            print('Right Guess..!!')
            play_again =input('You Won the Game by guessing Right \n Wanna play next level : ')
            if play_again== 'yes' or play_again== 'Yes' or  play_again == 'YES':
                retry()
                break                      ## fixed a bug 
            else:
                print('Thanks for playing...!!!!')
                break
                
                
                
            

        else:
            print('Wrong guess..!')
            if i<3:
                print('Try again..')
            elif i==3 :
                print(' '*503 , 'Right Answer is: ', random_word)
                play_again =input('You lose the Game by guessing 3 times wrong \n Wanna play again: ')
                if play_again== 'yes' or play_again== 'Yes' or  play_again == 'YES':
                    retry()
                else:
                    print('Thanks for playing...!!!!')
                    break


retry()

            



            