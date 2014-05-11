# -*- coding: cp949 -*-

'''
Created on 2014. 3. 12.

@author: kyujin.kang
'''

class addressInfo:
    '''
    classdocs
    '''


    def __init__(self, name=None, phone=None, address=None):
        '''
        Constructor
        '''
        self.name = name
        self.phone = phone
        self.address = address
    
#     def __eq__(self, info):
#         if self.name == info.name:
#             return True
#         else:
#             return False
#     
#     def __hash__(self):
#         return self.name

    @property
    def name(self):
        print 'You are getting name'
        return self._name

    @property
    def phone(self):
        print 'You are getting phone'
        return self._phone

    @property
    def address(self):
        return self._address

    @name.setter
    def name(self, value):
        self._name = value

    @phone.setter
    def phone(self, value):
        self._phone = value

    @address.setter
    def address(self, value):
        self._address = value

    @name.deleter
    def name(self):
        del self._name

    @phone.deleter
    def phone(self):
        del self._phone

    @address.deleter
    def address(self):
        del self._address

#     name = property(get_name, set_name, del_name, "name's docstring")
#     phone = property(get_phone, set_phone, del_phone, "phone's docstring")
#     address = property(get_address, set_address, del_address, "address's docstring")


def test_main():
    info_a = addressInfo()
    
    info_a.name = '강규진'
    info_a.phone = '010-3713-3345'
    info_a.address = '경기도 수원시 권선동 대원신동아 512동 1006호'
    
    info_b = addressInfo(name='이수연',phone='010-7142-3213',address='경기도 수원시 권선동 대원신동아 512동 1006호')
    
    info_c = info_a
    
    print "이름:", info_a.name, " 휴대폰번호:", info_a.phone, " 주소:", info_a.address
    print "이름:", info_b.name, " 휴대폰번호:", info_b.phone, " 주소:", info_b.address
    print "이름:", info_c.name, " 휴대폰번호:", info_c.phone, " 주소:", info_c.address


if __name__ == '__main__':
    test_main()