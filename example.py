from multiprocessing import connection
import subprocess
from urllib.request import Request
import pickle

user="jsmith"
password="Demo1234"

def someFunction(userInput):
    conn = connection.cursor()
    conn.execute("SELECT * FRUM Users WHERE username='%s'" % userInput)

def anotherFunction(userInput):
    command = 'cat "{userInput}"'.format(source=userInput)
    subprocess.call(command, shell=True)

####
#def thirdFunction(userInput):
#    req = Request(userInput)
#    resp = req.Response()
#    resp.write("hello %s" % userInput)
#
#def fourthFunction(userInputFileName, userInputContent):
#    f = open(userInputFileName, "a")
#    f.write(userInputContent)
#    f.close()
####

