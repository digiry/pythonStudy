#! python
# -*- coding: utf-8 -*-

'''
Created on 2014. 3. 12.

@author: kyujin.kang
'''
from addressBookUI import addressBookUI

def main():
    BookUI = addressBookUI()
    menu_cnt = True
    while menu_cnt != False:
        menu = BookUI.launchMenu()    
        print "selected menu: ", menu
        if (menu <= 0) or (menu == ''):
            menu_cnt = False
            print "Exit..."
        if menu == 1:
            BookUI.inputAddress()
        if menu == 2:
            BookUI.removeAddress()
        if menu == 3:
            BookUI.updateAddress()
        if menu == 4:
            BookUI.searchAddress()
        if menu == 5:
            BookUI.printAll()
        if menu == 6:
            BookUI.clearScreen()
        if menu == 7:
            BookUI.saveFile()
        if menu == 8:
            BookUI.loadFile()

if __name__ == '__main__':
    main()