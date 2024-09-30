# Import modules
import random 
import time 
import secrets
import string
import threading
from threading import Thread
from threading import Timer
import time
import os
from twilio.rest import Client

# Set individual access
accessList = [''] #<- enter user ids (first initial last name with id number) e.g. JDoe1234
validAccess = '' #<- enter authorized user ids

# Define a function to gain access to the system
def access():
    # Attain user imput
    verAccess = input('Please enter your first and last initial followed by your ID number. (e.g. JDoe1234): ')
    # Edit the user input to the proper format
    verAccess = verAccess[0].upper() + verAccess[1].upper() + verAccess[2:100].lower()
    # Proceed if the individual has access
    if verAccess == '': #<- enter user ids that have access to this program 
        print('System active')
    else:
        # In real world scenerio code would be entered here as an alarm to notify that someone without access attempted to get access to the program
        exit()

# Define a function to generate a password
def passwordGen():
    # Set the password length to 10-20
    length = random.randrange(10, 20)
    # Allow the password to contain capital and lowercase letters, numbers, and punctuation.
    newPassword = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation)
                     for i in range(length))
    # Update the current password to the password generated
    password = newPassword

    # Send the new password via txt to a secure phone
    account_sid = '' #<- enter the account sid from Twilio
    auth_token = 'token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+1', #<- eter the from number from the Twilio subscription
        body=(password),
        to='+1' #<- enter the to number 
        )
    print(message.sid)

    # Define a function that sets a timer and allows an action to be taken within that time
    def timedAccess():
        # Set the timer length 
        timeLimit = int(600)
        # Inform the user of the time length
        print('You have ten minutes to enter the password for access')
        # Set what happens when timer returns 0
        t = Timer(timeLimit, lambda: print( 
                '\nA new password has been generated and the timer has been reset.', passwordGen()))
        # Start the timer
        t.start() 
        print("You have 10 minutes before a new password is generated and sent") 
        # Prompt the user to enter the password once the timer begins
        userInput = input('Enter the password: ') 
        # If the incorrect password is entered, generate a new password
        if userInput != password:
            passwordGen()
        # If the correct password is entered, gain access to the information
        if userInput == password:
            print('Access granted')
            print('----------PUBLIC DATA DISPLAY----------')
            # Ask the admin what infomration they are looking for and set the infmormation contained within those categoties
            def dataInfo():
                dataType = input('What data type are you looking to access? (Public, Private, Iternal, Confidential, or Restricted) ')
                if dataType == 'Public':
                    print('---First & last names---\n---Company names and founder or executive information---\n---dates of birth or dates of incorporation---')
                    Exit = input("'Press 'e' followed by the 'Enter' key to exit and generate a new password ")
                    if Exit == 'e':
                        passwordGen()
                elif dataType == 'Private':
                    print('---Personal contact information---\n---Research data or online browsing history---\n---Email inboxes or cellphone content---')
                    Exit = input("'Press 'e' followed by the 'Enter' key to exit and generate a new password ")
                    if Exit == 'e':
                        passwordGen()
                elif dataType == 'Internal':
                    print('---Business plans and strategies---\n---Internal emails or memos---\n---Company intranet platforms---\n---Internet protocol (IP) addresses---')
                    Exit = input("'Press 'e' followed by the 'Enter' key to exit and generate a new password ")
                    if Exit == 'e':
                        passwordGen()
                # If the information is highly private or classified, do not grant access from this program
                elif dataType == 'Confidential' or 'Restricted':
                    print('Access denied')
                    # In real time, code would be entered here to send out a high alert alarm and lock out the program fully until the IT admin or higher-up intervenes
                    exit()

# Call all functions in proper order
            dataInfo()
                    
        t.cancel() 
    
    timedAccess()


access()
passwordGen()
