import json
import random

#read
email = open(r'C:\Users\t-lindat\Desktop\coding_exercise\project\Email.json')
emailContent = email.read()
email.close()

#parse
emails = json.loads(emailContent)

#order the emails from first to last
emailsFirstToLast = [x for x in emails[::-1]]

"""
#bare minimum: 
for index in range(len(emailsFirstToLast)):
    email = emailsFirstToLast[index]
    print('Email ' + str(index+1) + ' is from sender ' + email['sender'] + ', the subject is ' + email['subject'] + ' and the summary is ' + email['summary'] + '.') 
"""

#some options for the voice to refer to the emails which are not the first one or the last one
nextEmailOptions = ['The next one is from ', 'Your next email is from ', 'Next, you got an email from ']

#let's make it sound more "natural"
for index in range(len(emailsFirstToLast)):
    email = emailsFirstToLast[index]
    if index == 0 and email['summary'] != '':
        print('Your first email is from ' + email['sender'] + ' about ' + email['subject'] + '. The summary is: ' + email['summary'] + '.')
    elif index == 0 and email['summary'] == '':
         print('Your first email is from ' + email['sender'] + ' about ' + email['subject'] + '. I cannot provide a summary for this email.')
    elif index != 0 and index < (len(emailsFirstToLast) - 1) and email['summary'] != '':
         print(random.choice(nextEmailOptions)+ email['sender'] + ' about ' + email['subject'] + '. The summary is: ' + email['summary'] + '.')    
    elif index != 0 and index < (len(emailsFirstToLast) - 1) and email['summary'] == '':
         print(random.choice(nextEmailOptions)+ email['sender'] + ' about ' + email['subject'] + '. I cannot provide a summary for this email.')    
    elif index == (len(emailsFirstToLast) - 1) and email['summary'] != '':
         print('Your last email is from ' + email['sender'] + ' about ' + email['subject'] + '. The summary is: ' + email['summary'] + '.')    
    elif index == (len(emailsFirstToLast) - 1) and email['summary'] == '':
         print('Your last email is from ' + email['sender'] + ' about ' + email['subject'] + '. I cannot provide a summary for this email.')    
    







