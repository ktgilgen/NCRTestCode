import pymongo
from mongokit import *
import datetime
import json

class User(Document):
    __collection__ = 'Users'
    __database__ = 'brainlab_test'
    structure = {
        'First_Name': basestring,
        'Last_Name': basestring,
        'Password': basestring,
        'Time_Created': basestring,
        'Last_Activity': basestring,
        'Login_Site': basestring, 
        'Lab': basestring,
        'Rank': basestring,
        'Username': basestring, #email
        'Session_ID': int,
        'Subscription' : basestring,
        'Security_Question' : basestring,
        'Security_Answer' : basestring,
        'Activate' : int
    }

connection = Connection(host="mongodb://braintest:braintest@ds041167.mongolab.com:41167/brainlab_test", port=27017)
connection.register([User])

userList = list ( connection.brainlab_test.Users.find() )
for user in userList:   
    item = connection.User({
                               "First_Name": user['First_Name'],
                               "Last_Name": user['Last_Name'],
                               "Password": user['Password'],
                               "Time_Created": str( datetime.datetime.now() ),
                               "Last_Activity": str( datetime.datetime.now() ),
                               "Login_Site": user['Login_Site'], 
                               "Lab": str (user['Lab']),
                               "Rank": user['Rank'],
                               "Username": user['Username'], #email
                               "Session_ID": int ( user['Session_ID'] ),
                               "Subscription" : str( datetime.datetime.now() ),
                               "Security_Question" : "What is your favorite color?",
                               "Security_Answer" : "Yellow",
                               "Activate" : int(7777777)})
    item.save()
