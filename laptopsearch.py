import logging 
LOG_FILENAME = 'murder.log' # this is my log file name

logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO) #starting my logging

def laptopsearch():
  logging.info('inside laptop search')
  print('As you look through the laptop you find multiple emails that were threatning to the earls life?')
  end =str(input('Do you wish to further investigate? Yes or No: '))
  if end == 'Yes' or end =='yes':
    print('You find that the man emailing the earl was called Nicholas')
    finale = str(input('Do you wish to question him? Yes or No: '))
    if finale == 'Yes' or finale =='yes':
      print('You bring him in for questioning and he breaks down confessing that he murdered the earl for money.')
      final = str(input('Do you want to arrest him? Yes or No: '))
      if final == 'Yes' or final == 'yes':
        print('Excellent job Detective! You are promoted')