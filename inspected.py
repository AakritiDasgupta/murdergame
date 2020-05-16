import logging 
LOG_FILENAME = 'murder.log' # this is my log file name

logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO) #starting my logging

def inspected():
  logging.info('inside inspected')
  print('As we sent the blood to be inspected we have found that it directly connects to a man named Nicholas')
  chance5 =str(input('Do you want to bring him in for questioning, Yes or No: '))
  if chance5 == 'Yes' or chance5 =='yes':
    print('You bring him in for questioning and he breaks down confessing that he murdered the earl for money.')
    final = str(input('Do you want to arrest him? yes or no: '))
    if final == 'Yes' or final == 'yes':
      print('Excellent job Detective! You are promoted')
    else:
      print('Game Over')
  else:
    print('Are u crazy? You cannot be a detective')