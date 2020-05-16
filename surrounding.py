from inspected import inspected
from counter import counter
import logging 
LOG_FILENAME = 'murder.log' # this is my log file name

logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO) #starting my logging

def surrounding():
  logging.info('I am in the surrounding function')
  print('As you check the your surrounding you find a drop of blood on the ground. ')  
  chance2 = str(input('Do you wish to send the blood to testing? Yes or No: '))
  if chance2 == "yes" or chance2 == "Yes":
      print('The forensics team came game and found that the blood found on the floor does not belong to the deceased person')
      chance3 = str(input('do you wish to inspect it? Yes or No: '))
      logging.info('going to call inspected')
      if chance3 == 'Yes' or chance3 == 'yes':
        inspected()
      else:
        print('You are fired')
  elif chance2 == "no" or chance2 == "No":
    logging.info('did not call inspected')
    print('As you keep looking you find a laptop.')
    chance4 = str(input( 'Do you want to inspect it? Yes or No: '))
    if chance4 == "yes" or chance4 == "Yes":
      print('You find that the laptop is locked but there is a hint for the password. It reads "I am an english word with three consecutive doulbe letters" ')
      logging.info('going to call counter')
      counter()
    else:
      logging.info('Did not go to counter')
      print('Are you kidding me? You are fired')
  else: 
    logging.info('did not go to inspected')
    print('This is not a joke.You are fired')