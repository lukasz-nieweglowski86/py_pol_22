from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

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

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # click first contact's 'Edit' icon
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
