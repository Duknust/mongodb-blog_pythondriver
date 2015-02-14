#created by duknust
#find in https://github.com/Duknust

import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost",safe=True) #connection to database

# get a handle to the students database
db=connection.students
grades = db.grades #get grades collection

def removeWorst(): #for each student remove his worst grade
  i = 0
  cursor = None
  minimumValid = False
  minimum = None
  for i in range (0, 200):
    print(i)
    try:
        cursor = grades.find({'student_id':i, 'type':'homework'}) #all grades from type homework for user i
    except:
      print "Unexpected error:", sys.exc_info()[0]
    print(cursor)
    for doc in cursor:
      print(doc)
      if (not minimumValid):
        minimum = doc
        minimumValid = True
      else:
        if(doc['score']<minimum['score']):
          minimum=doc
  grades.remove(minimum) #removes the minimum grade
  minimumValid = False