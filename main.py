from accident import accident
from counter import counter
from inspected import inspected
from laptopsearch import laptopsearch
from surrounding import surrounding
import logging 
# starting logging for easier debugging
LOG_FILENAME = 'murder.log' # this is my log file name
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO) #starting my logging

def murder():
  logging.info('Starting my murder mystery')

  print('There has been a murder in America. The body of an Earl has been found and it is your job to determine his cause of death. If you find the murder you will be promoted to the job of a detective for the CIA.')
  lose = str(input('Do you wish to take on this challenge? Yes or No: '))
  if lose== 'yes' or lose == 'Yes':
    print('The body of earl was found in a pool of blood, clearly indicating the stab wound on his stomach. There was a suicide note found, however it is highly suspicious because the earl was known for his love of life')
    guess = str(input('Is this death a murder or an accident? Murder or Accident: ')).lower()
    if guess == 'Murder' or guess == 'murder':
      logging.info('I am going to call function surrounding')
      surrounding()
    elif guess == 'Accident' or guess == 'accident':
      logging.info('I am going to call function accident')
      accident()
  else:
    print('Now is not the time for jokes! You are fired.')
    logging.info('User chose not to play the gome')

murder()