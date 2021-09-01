from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Test_firstname", middlename="Test_middlename",
                                lastname="Test_lastname", nickname="Test_nickname", title="Test_title",
                                company="Test_company", address1="Test_address1", home_phonenumber="123123123",
                                mobile_phonenumber="321321321", work_phonenumber="135135135", fax="123456789",
                                email1="test_email1@test.com", email2="test_email2@test.com",
                                email3="test_email3@test.com", homepage="www.google.com", bday="11",
                                bmonth="March", byear="1986", aday="7", amonth="July", ayear="2020",
                                address2="Test_address2", phone2="909808707", notes="Lorem ipsum..."))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="edited", middlename="edited", lastname="edited", nickname="edited", title="edited",
                      company="edited", address1="edited", home_phonenumber="111111111", mobile_phonenumber="222222222",
                      work_phonenumber="333333333", fax="444444444", email1="edited1@test.com",
                      email2="edited2@test.com", email3="edited3@test.com", homepage="www.edited.com",
                      bday="12", bmonth="June", byear="1886", aday="1", amonth="January", ayear="2022",
                      address2="edited2", phone2="555555555", notes="edited")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
