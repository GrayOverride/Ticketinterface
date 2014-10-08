import urllib2
import json
import sys
import datetime
import secret
from PyQt4 import QtGui


##this part is ugly
currentLanArray = []
allLanArray = []
userEmailsArray = []
userPaymentsArray= []
userTotalArray=[]
unpayed=[]
time = datetime.datetime.time(datetime.datetime.now())
##i told you so


req = urllib2.Request("https://store.wonderlan.se/api/orders?per_page=1000.json",headers={"X-Spree-Token" : secret.key['auth']})
opener = urllib2.build_opener()
f = opener.open(req)
json_object = json.loads(f.read())
for i in json_object['orders']:
    if i['completed_at']>'2000-01':
        userEmailsArray.append(i['email'])
        userPaymentsArray.append(i['payment_state'])
        userTotalArray.append(i['total'])
        allLanArray.append(i)
    if i['completed_at']>'2014-08':
        currentLanArray.append(i)
for k in currentLanArray:
    if k['payment_state']=='balance_due':
        unpayed.append(i)

userpay = len(userPaymentsArray)
ordersAmount = len(allLanArray)
fixedIndex = ordersAmount-1 #for the email list later down the code
currentLan = len(currentLanArray)
unpayedTickets = len(unpayed)


def boot():
    
    print "hello sir"
    print "wonderlan currently have {} bookings and {} are not yet paid".format(currentLan, unpayedTickets)
    start();
def start():
    str = raw_input("$: ")
    if str == "search":
        print "welcome to the search, write exit to leave"
        searchInput();
    if str == "exit":
        print "good night"
        exit();




def search (str):
    for i in json_object['orders']:
        if i['email'] == str:
            print i;
            return;


def searchInput():
    str = raw_input("email search: ");
    search(str)
    if str=="exit":
        start()
    searchInput()
boot()
def exit():
    print "good night"


