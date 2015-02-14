#created by duknust
#find in https://github.com/Duknust

import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost",safe=True) #connection to database

# get a handle to the school database
db=connection.school
students = db.students #get students collection

def removeWorst(): #for each student remove his worst grade of type homework
  i = 0
  cursor = None
  minimumValid = False
  minimum=-1
  for i in range (0, 200):
    print(i)
    try:
        cursor = students.find({'_id':i}) #all students from type homework for user i
    except:
      print "Unexpected error:", sys.exc_info()[0]
    # print(cursor)
    for doc in cursor:
      #print(doc)
      tmp = doc['scores'];
      for x in tmp:
        if x['type'] == "homework":
          print x['score']
          if minimum<0:
            minimum = x['score']
          else:
            if x['score']<minimum:
              minimum = x['score']
    print minimum
    print tmp
    res = []
    for k in tmp:
      if k['type'] == "homework":
        if k['score'] != minimum:
          res.append(k)
      else:
        res.append(k)
    print res
    students.update({'_id':i},
                      {'$set':{'scores':res}})
    minimum=-1

      