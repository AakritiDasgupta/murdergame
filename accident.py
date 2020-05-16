import logging 
LOG_FILENAME = 'murder.log' # this is my log file name

logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO) #starting my logging

def accident():
  logging.info('I am in the accident function')
  chance1 = str(input('Are you sure this death is an accident? a. yes , b. no '))
  if chance1 == 'a' or chance1 == 'A':
    print("You are quite a lousy detective. You are fired!")
  elif chance1 == 'b' or chance1 == "B":
    print("You were right. Maybe you will be an ok detective.")
  else:
    print('Now is not the time for jokes. You are fired')