# -*- coding: utf-8 -*-
__author__ = 'ninaeros'

import bsddb
import json

MENU_QUIT = 0
MENU_INPUT = 1
MENU_DELETE = 2
MENU_MODIFY = 3
MENU_VIEW_ALL = 4
MENU_CLEAN_ALL = 5
MENU_SAVE = 6
MENU_LOAD = 7
MENU_WRITE_DB = 8
MENU_READ_DB = 9

class AddressInfo:
    name = ''
    phoneNumber = ''
    address = ''


def printMainMenu():
    """
    print Main Menu list
    """
    print """
1.주소정보를 입력한다.
2.주소정보를 삭제한다.
3.주소정보를 수정한다.
4.전체 주소정보를 출력한다.
5.전체 주소정보를 파일에 저장한다.
6.파일에서 전체 주소정보를 불러온다.
7.전체 주소정보를 DB에 저장한다.
9.DB에서 전체 주소정보를 불러온다.
0.종료한다.
    """


def inputMenu():
    """
    input menu
    """
    selectedmenu = int(raw_input('menu: '))
    return selectedmenu

def isEmptyName(name):
    result = False
    if name == '':
        result = True
    return result

def isDuplicatedName(name, addressInfoList):
    result = False
    for info in addressInfoList:
        if info.name == name:
            result = True
            break
    return result


def inputName(addressInfoList):
    isAvailableName = False
    name = None
    while not isAvailableName:
        name = raw_input('이름: ')
        if ( isEmptyName(name) == True ):
            print '빈 이름이 입력되었습니다.'
        elif ( isDuplicatedName(name, addressInfoList) == True ):
            print '중복된 이름이 입력되었습니다.'
        else:
            # passed all exception cases
            isAvailableName = True
    return name


def inputPhoneNumber():
    phoneNumber = raw_input('전화번호: ')
    return phoneNumber


def inputAddress():
    address = raw_input('주소: ')
    return address


def printAddressInfoHeader():
    print '------------------------------------------------'
    print '| Name     | Phone        | Address            |'
    print '------------------------------------------------'


def printAddressInfoEndLine():
    print '------------------------------------------------'


def _printAddressInfo(person):
    print '|%-10s|%-14s|%-20s|' % (person.name, person.phoneNumber, person.address)


def printAddressInfo(person):
    printAddressInfoHeader()
    _printAddressInfo(person)
    printAddressInfoEndLine()


def inputAddressInfo(addressInfoList):
    person = AddressInfo()
    person.name = inputName(addressInfoList)
    person.phoneNumber = inputPhoneNumber()
    person.address = inputAddress()
    printAddressInfo(person)
    addressInfoList.append(person)


def printAddressInfoList(addressInfoList):
    printAddressInfoHeader()
    for info in addressInfoList:
        _printAddressInfo(info)
    printAddressInfoEndLine()


def findAddressInfo(name, addressInfoList):
    for info in addressInfoList:
        if info.name == name:
            return info
    return None



def removeAddressInfo(addressInfoList):
    isAvailableName = True
    name = raw_input('삭제할 이름: ')
    if ( isEmptyName(name) == True ):
        print '빈 이름이 입력되었습니다.'
        isAvailableName = False
    else:
        person = findAddressInfo(name, addressInfoList)
        if ( person == None ):
            isAvailableName = False

    if isAvailableName:
        printAddressInfo(person)
        isYes = raw_input('삭제하겠습니까? (y/n) ')
        if (isYes == 'y' or isYes == 'Y'):
            addressInfoList.remove(person)
            print '삭제되였습니다.'
        else:
            print '삭제 취소하였습니다.'
    else:
        print '해당 이름의 주소정보를 찾을 수 없습니다.'


def clearAddressBook(addressInfoList):
    addressInfoList = []


def modifyAddressInfo(addressInfoList):
    isAvailableName = True
    name = raw_input('수정할 이름: ')
    if ( isEmptyName(name) == True ):
        print '빈 이름이 입력되었습니다.'
        isAvailableName = False
    else:
        person = findAddressInfo(name, addressInfoList)
        if ( person == None ):
            isAvailableName = False

    if isAvailableName:
        printAddressInfo(person)
        phoneNumber = inputPhoneNumber()
        address = inputAddress()
        isYes = raw_input('수정하겠습니까? (y/n) ')
        if (isYes == 'y' or isYes == 'Y'):
            person.phoneNumber = phoneNumber
            person.address = address
            print '수정되었습니다.'
        else:
            print '수정 취소하였습니다.'
    else:
        print '해당 이름의 주소정보를 찾을 수 없습니다.'

def loadAddressInfoList(addressInfoList):
    loadResult = False
    clearAddressBook(addressInfoList)
    printAddressInfoHeader()
    f = open('addressbook.dat', 'r')
    f.seek(0, 2)
    eof = f.tell()
    f.seek(0)
    while True:
        person = AddressInfo()
        person.name = f.readline().rstrip('\n')
        person.phoneNumber = f.readline().rstrip('\n')
        person.address = f.readline().rstrip('\n')
        addressInfoList.append(person)
        _printAddressInfo(person)
        if eof == f.tell():
            printAddressInfoEndLine()
            print '파일로부터 주소정보를 불러왔습니다.'
            break
    if len(addressInfoList) > 0:
        loadResult = True
    return loadResult

def saveAddresInfoList(addressInfoList):
    '''
    Return : saveResult : boolean : save result
    file record format
    1 line : name
    2 line : phoneNumber
    3 line : address4
    '''
    saveResult = False
    if len(addressInfoList) > 0:
        f = open('addressbook.dat', 'w')
        for info in addressInfoList:
            f.write(info.name + '\n')
            f.write(info.phoneNumber + '\n')
            f.write(info.address + '\n')
        f.close()
        saveResult = True
        print '전체 주소정보가 저장되었습니다.'
    return saveResult


def writeDBAddressInfoList(addressInfoList):
    db = bsddb.btopen('addressBook.db', 'c')
    index = 1
    for info in addressInfoList:
        db['%d'%index] = json.dumps({'name':info.name, 'phoneNumber':info.phoneNumber, 'address':info.address})
        index += 1
    db.sync()
    db.close()
    print '전체 주소정보가 DB에 저장되었습니다.'

def readDBAddressInfoList(addressInfoList):
    clearAddressBook(addressInfoList)
    db = bsddb.btopen('addressBook.db', 'r')
    for num, infoDump in db.iteritems():
        jsonInfo = json.loads(infoDump)
        person = AddressInfo()
        person.name = str(jsonInfo[unicode('name')])
        person.phoneNumber = str(jsonInfo[unicode('phoneNumber')])
        person.address = str(jsonInfo[unicode('address')])
        print '%s 번째 정보 불러왔습니다.' % (num)
        addressInfoList.append(person)
    db.close()
    print '전체 주소정보 DB를 모두 불러왔습니다.'


def main():
    addressInfoList = []
    selectedMenu = -1

    while selectedMenu != 0:
        printMainMenu()
        selectedMenu = inputMenu()
        if selectedMenu == MENU_INPUT:
            inputAddressInfo(addressInfoList)
        elif selectedMenu == MENU_DELETE:
            removeAddressInfo(addressInfoList)
        elif selectedMenu == MENU_MODIFY:
            modifyAddressInfo(addressInfoList)
        elif selectedMenu == MENU_VIEW_ALL:
            printAddressInfoList(addressInfoList)
        elif selectedMenu == MENU_CLEAN_ALL:
            clearAddressBook(addressInfoList)
        elif selectedMenu == MENU_SAVE:
            saveAddresInfoList(addressInfoList)
        elif selectedMenu == MENU_LOAD:
            loadAddressInfoList(addressInfoList)
        elif selectedMenu == MENU_WRITE_DB:
            writeDBAddressInfoList(addressInfoList)
        elif selectedMenu == MENU_READ_DB:
            readDBAddressInfoList(addressInfoList)
        elif selectedMenu == MENU_QUIT:
            print '주소록을 종료합니다.'
            break
        else:
            print '없는 번호를 입력하였습니다.'

if __name__ == '__main__':
    main()