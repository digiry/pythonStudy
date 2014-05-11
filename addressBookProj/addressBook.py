# -*- coding: utf-8 -*-
'''
Created on 2014. 3. 12.

@author: soo&kyu
'''
from addressInfo import addressInfo

class addressBook:
    def __init__(self):
        self.addresslist = []
    
    def length(self):
        return len(self.addresslist)
    
    def getAt(self, index):
        return self.addresslist[index]
    
    def searchByName(self, name):
        for i in range(len(self.addresslist)):
            if self.addresslist[i].name == name:
                matchInfo = self.addresslist[i]
        return matchInfo
    
    def addAddressInfo(self, info):
        self.addresslist.append(info)
    
    def removeAddressInfo(self, index):
        if (0 <= index) and (index < self.length()):
            del self.addresslist[index]
        
    def updateAddressInfo(self, index, info):
        if (0 <= index) and (index < self.length()):
            self.addresslist[index] = info

    def clearAddressBook(self):
        del self.addresslist[:]

    def loadFile(self):
        loadResult = False
        self.clearAddressBook()
        f = open('addressbook.dat','r')
        f.seek(0,2)
        eof = f.tell()
        f.seek(0)
        while True:
            info = addressInfo() 
            info.name = f.readline().rstrip('\n')
            info.phone = f.readline().rstrip('\n')
            info.address = f.readline().rstrip('\n')
            self.addAddressInfo(info)
            print 'load info: name=%s phone=%s address=%s' % (info.name,info.phone,info.address)
            if eof == f.tell(): break
        if self.length() > 0: loadResult = True
        return loadResult

    def saveFile(self):
        '''
        Return : saveResult : boolean : save result
        file record format
        1 line : name
        2 line : phone
        3 line : address
        '''
        saveResult = False
        if self.length() > 0:
            f = open('addressbook.dat','w')
            for info in self.addresslist:
                f.write(info.name + '\n')
                f.write(info.phone + '\n')
                f.write(info.address + '\n')
            f.close()
            saveResult = True
        return saveResult

def test_main():
    book = addressBook()
    from addressInfo import addressInfo
    info = addressInfo(name='강규진',phone='010-3713-3345',address='대원신동아')
    
    book.addAddressInfo(info)
    copyInfo = book.getAt(0)
    
    print "name:", copyInfo.name, " phone:", copyInfo.phone, " address:", copyInfo.address

if __name__ == '__main__':
    test_main()