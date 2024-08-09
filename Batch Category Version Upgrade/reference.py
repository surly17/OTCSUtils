import requests
import random
import json
import threading

parentID = 2127317
#Name = "NewFolder"+str(random.randint(0,9999999999))+"-"+str(random.randint(0,99999999))+"-"+str(random.randint(0,999999999))
l=0

def getOTCSTicket():
    global currentTicket
    userpass = {'username':'Admin', 'password':'#######'}
    response = requests.post("http://corp2-otcs-1/otcs20/cs.exe/api/v1/auth/", userpass)
    jsonResponse = response.json()
    currentTicket ={'OTCSTicket':jsonResponse["ticket"]}

def generateRandomName():
    return "NewFolder"+str(random.randint(0,9999999999))+"-"+str(random.randint(0,99999999))+"-"+str(random.randint(0,999999999))
    

def updateOTCSTicket(responseHeader):
    currentTicket ={'OTCSTicket':responseHeader['OTCSTicket']}

def createOTCSFolder(parentID,Name,authTicket):
    obj_details={}
    obj_details['name']=Name
    obj_details['parent_id']=parentID
    obj_details['type']=0
    body = {'body':json.dumps(obj_details)}
    response = requests.post('http://corp2-otcs-1/otcs20/cs.exe/api/v2/nodes',headers=authTicket, data=body)
    jsonResponse = response.json()
    updateOTCSTicket(response.headers)
    #print(response.json())
    #print("Created Folder with data: " + str(jsonResponse["results"]['data']['properties']['id']))
    return jsonResponse["results"]['data']['properties']['id']

def createManyFolders():
    l=0
    while l < 65000:
        createdID = createOTCSFolder(parentID,generateRandomName(),currentTicket)
        print(str(createdID) + ": NodeID created on thread: {}".format(threading.current_thread().name))
        l=l+1

if __name__ =="__main__":
    getOTCSTicket()
    # creating thread
    t1 = threading.Thread(target=createManyFolders)
    t2 = threading.Thread(target=createManyFolders)
    t3 = threading.Thread(target=createManyFolders)
    t4 = threading.Thread(target=createManyFolders)
 
    # starting thread 1
    t1.start()
    t2.start()
    t3.start()
    t4.start()

 
    # wait until thread 1 is completely executed
    t1.join()
    t2.join()
    t3.join()
    t4.join()
 
    # both threads completely executed
    print("Done!")

