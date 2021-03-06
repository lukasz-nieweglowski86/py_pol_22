from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address1=None, all_phones_from_home_page=None, home_phonenumber=None, mobile_phonenumber=None,
                 work_phonenumber=None, fax=None, all_emails_from_home_page=None, email1=None, email2=None, email3=None, homepage=None, bday=None,
                 bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address1 = address1
        self.all_phones_from_home_page = all_phones_from_home_page
        self.home_phonenumber = home_phonenumber
        self.mobile_phonenumber = mobile_phonenumber
        self.work_phonenumber = work_phonenumber
        self.fax = fax
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
