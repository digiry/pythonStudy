# -*- coding: utf-8 -*-
'''
Created on 2014. 3. 13.

@author: soo&kyu
'''
from addressBook import addressBook
from addressInfo import addressInfo
import os

class addressBookUI:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.addressBook = addressBook()

    def printMenu(self):
        print '''\
[1] Input AddressInfo
[2] Remove Address
[3] Update Address
[4] View one Address
[5] View All Address
[6] Clear Screen
[7] Save All Address to file
[8] Load Address info from file
[0] Exit
'''

    def launchMenu(self):
        self.printMenu()
        self.choice_menu = raw_input('CHOICE: ')
        return int(self.choice_menu)

    def printHeader(self):
        print '------------------------------------------------'
        print '| Name     | Phone        | Address            |'
        print '------------------------------------------------'
    
    def printEndline(self):
        print '------------------------------------------------'
        
    def printAddressInfo(self, info):
        print '|%10s|%14s|%20s|' % (info.name, info.phone, info.address)
        

    def inputAddress(self):
        info = addressInfo()
        info.name = raw_input('Name: ')
        info.phone = raw_input('Phone: ')
        info.address = raw_input('Address: ')
        self.addressBook.addAddressInfo(info)
        print 'Added Address'
    
    def removeAddress(self):
        index = raw_input('Index to remove: ')
        self.addressBook.removeAddressInfo(index)
        print 'Removed Address'

    def updateAddress(self):
        index = int(raw_input('Index to update: '))
        info = self.addressBook.getAt(index)
        self.printAddressInfo(info)
        print "update address information"
        update_info = addressInfo()
        update_info.name = raw_input('Name: ')
        update_info.phone = raw_input('Phone: ')
        update_info.address = raw_input('Address: ')
        self.addressBook.updateAddressInfo(index, update_info)
        print 'Updated Address'
    
    def searchAddress(self):
        name = raw_input('name to search')
        info = self.addressBook.searchByName(name)
        self.printAddressInfo(info)
    
    def printAll(self):
        self.printHeader()        
        for info in self.addressBook.addresslist:
            self.printAddressInfo(info)
        self.printEndline()
    
    def clearScreen(self):
        os.system('cls')

    def loadFile(self):
        loadResult = self.addressBook.loadFile()
        if loadResult:
            print "loaded addressBook: file"
        else:
            print "Failed to load addressBook"

    def saveFile(self):
        saveResult = self.addressBook.saveFile()
        if saveResult:
            print "saved addressBook: file"
        else:
            print "Failed to save addressBook"

def test_main():
    BookUI = addressBookUI()
    menu_cnt = True
    while menu_cnt != False:
        menu = BookUI.launchMenu()    
        print "selected menu: ", menu
        if menu <= 0:
            menu_cnt = False
        if menu == 1:
            BookUI.inputAddress()
        if menu == 2:
            BookUI.removeAddress()
        if menu == 3:
            BookUI.updateAddress()
        if menu == 4:
            BookUI.searchAddress('')
        if menu == 5:
            BookUI.printAll()
        if menu == 6:
            BookUI.clearScreen()
        if menu == 7:
            BookUI.saveFile()            

if __name__ == '__main__':
    test_main()