from laptopsearch import laptopsearch
import logging 

# starting logging for easier debugging

LOG_FILENAME = 'murder.log' # this is my log file name

logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO) #starting my logging

def counter():
  logging.info('inside counter')
  guess = 0
  print('What am I? Keep in mind you only have 3 tries before the computer refuses to open.')
  answer = str(input('Guess: '))
  if answer == "Bookkeeper" or answer== 'bookkeeper':
    print('Good Job')
  else:
    guess = guess+1
    print('You have ',guess,' of 3 chances remaining. The meaning of this word is the one who keeps books')
    answer =str(input('Guess:'))
    if answer  == "Bookkeeper" or answer== 'bookkeeper':
      logging.info('going to call laptop search - 1st try')
      laptopsearch()
    else:
      logging.info('did not call laptopsearch because first try incorrect')
      guess = guess+1
      print('You have ',guess,' of 3 chances remaining. The meaning of this word is the one who keeps books')
      answer =str(input('Guess:'))
      if answer  == "Bookkeeper" or answer== 'bookkeeper':
        logging.info('going to call laptop search - 2nd try try')
        laptopsearch()
      else: 
        logging.info('did not call laptopsearch because 2nd try incorrect')
        guess = guess+1
        print('This is your last chance')
        answer =str(input('Guess:'))
        if answer  == "Bookkeeper" or answer== 'bookkeeper':
          logging.info('going to call laptop search - 3rd try')
          laptopsearch()
        else: 
          logging.info('did not call laptopsearch because 3rd try incorrect')
          print('Game Over')