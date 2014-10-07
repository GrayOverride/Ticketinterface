import urllib2
import json
import sys
import secret
from PyQt4 import QtGui
req = urllib2.Request("https://store.wonderlan.se/api/orders?per_page=1000.json",headers={"X-Spree-Token" : secret.key['auth']})
opener = urllib2.build_opener()
f = opener.open(req)
json_object = json.loads(f.read())
currentLanArray = []
allLanArray = []
userEmailsArray = []
userPaymentsArray= []
userTotalArray=[]
for i in json_object['orders']:
    if i['completed_at']>'2000-01':
        userEmailsArray.append(i['email'])
        userPaymentsArray.append(i['payment_state'])
        userTotalArray.append(i['total'])
        allLanArray.append(i)
for i in json_object['orders']:
    if i['completed_at']>'2014-08':
        currentLanArray.append(i)

userpay = len(userPaymentsArray)
ordersAmount = len(allLanArray)
fixedIndex = ordersAmount-1 #for the email list later down the code
currentLan = len(currentLanArray)


#print json_object['orders']

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        super(Main, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.WonderPy = self.addToolBar('Exit')
        self.WonderPy.addAction(exitAction)
        
        
        lbl1 = QtGui.QLabel("Tickets sold for wl-14 autum:", self)
        lbl1.move(15, 40)
        value1 = QtGui.QLabel(str(currentLan),self)
        value1.move(300,40)

        lbl2 = QtGui.QLabel("Tickets sold since the begining of time:", self)
        lbl2.move(15, 70)
        value2 = QtGui.QLabel(str(ordersAmount),self)
        value2.move(300,70)
    
        lbl3 = QtGui.QLabel("Tickets sold since the begining of time:", self)
        lbl3.move(15, 100)
        value3 = QtGui.QLabel(str(ordersAmount),self)
        value3.move(300,100)
        
        self.setGeometry(500, 300, 500, 500)
        self.setWindowTitle('WonderPy')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
