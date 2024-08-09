def getOTCSTicket():
    global currentTicket
    userpass = {'username':'Admin', 'password':'#######'}
    response = requests.post("http://corp2-otcs-1/otcs20/cs.exe/api/v1/auth/", userpass)
    jsonResponse = response.json()
    currentTicket ={'OTCSTicket':jsonResponse["ticket"]}