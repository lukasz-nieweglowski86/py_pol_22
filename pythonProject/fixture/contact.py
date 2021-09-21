from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
import json


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def select_value(self, element_name, value):
        wd = self.app.wd
        wd.find_element_by_name(element_name).click()
        Select(wd.find_element_by_name(element_name)).select_by_visible_text(value)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # name and address section
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address1)
        # phone number section
        self.change_field_value("home", contact.home_phonenumber)
        self.change_field_value("mobile", contact.mobile_phonenumber)
        self.change_field_value("work", contact.work_phonenumber)
        self.change_field_value("fax", contact.fax)
        # emails section
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # date of birth section
        self.select_value("bday", contact.bday)
        # wd.find_element_by_xpath("//select[@name='bday']/option[text()='" + contact.bday + "']").click()
        self.select_value("bmonth", contact.bmonth)
        # wd.find_element_by_xpath("//select[@name='bmonth']/option[text()='" + contact.bmonth + "']").click()
        self.change_field_value("byear", contact.byear)
        # date of anniversary section
        self.select_value("aday", contact.aday)
        # wd.find_element_by_xpath("//select[@name='aday']/option[text()='" + contact.aday + "']").click()
        self.select_value("amonth", contact.amonth)
        # wd.find_element_by_xpath("//select[@name='amonth']/option[text()='" + contact.amonth + "']").click()
        self.change_field_value("ayear", contact.ayear)
        # secondary address and notes section
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def add(self, contact):
        wd = self.app.wd
        # initiate adding new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        f = open("target.json")
        target = json.load(f)
        if not (wd.current_url.endswith(target["baseUrl"] + "edit.php") and
                len(wd.find_elements_by_link_text("add next")) > 0):
            wd.find_element_by_link_text("home page").click()
        f.close()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                contact_firstname = element.find_element_by_xpath(".//td[3]").text
                contact_lastname = element.find_element_by_xpath(".//td[2]").text
                contact_address = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=contact_firstname, lastname=contact_lastname, id=id,
                                                  address1=contact_address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        contact_firstname = wd.find_element_by_name("firstname").get_attribute("value")
        contact_lastname = wd.find_element_by_name("lastname").get_attribute("value")
        contact_address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phonenumber = wd.find_element_by_name("home").get_attribute("value")
        mobile_phonenumber = wd.find_element_by_name("mobile").get_attribute("value")
        work_phonenumber = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=contact_firstname, lastname=contact_lastname, id=id, address1=contact_address,
                       email1=email1, email2=email2, email3=email3, home_phonenumber=home_phonenumber,
                       mobile_phonenumber=mobile_phonenumber, work_phonenumber=work_phonenumber, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phonenumber = re.search("H: (.*)", text).group(1)
        mobile_phonenumber = re.search("M: (.*)", text).group(1)
        work_phonenumber = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phonenumber=home_phonenumber, mobile_phonenumber=mobile_phonenumber,
                       work_phonenumber=work_phonenumber, phone2=phone2)
