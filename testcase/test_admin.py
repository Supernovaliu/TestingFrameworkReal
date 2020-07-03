from time import sleep
from public.common import mytest
from public.pages import adminIndexPage

class TestAdminIndex(mytest.MyTest):


    def _login(self,userName,userPassword,title):
        login1=adminIndexPage.AdminIndexPage(self.dr)
        login1.into_admin_page()
        login1.input_admin_name(userName)
        login1.input_admin_password(userPassword)
        login1.click_submit_button()
        login1.return_title()
        sleep(2)
        self.assertEqual(title,login1.return_title())
    def test_login(self):
        login1 = adminIndexPage.AdminIndexPage(self.dr)
        login1.into_admin_page()
        login1.input_admin_name('superadmin')
        login1.input_admin_password('123456')
        login1.click_submit_button()
        sleep(2)
        self.assertEqual('backend management system', login1.return_title())
    def test_login1(self):
        login1 = adminIndexPage.AdminIndexPage(self.dr)
        login1.into_admin_page()
        login1.input_admin_name('')
        login1.input_admin_password('')
        login1.click_submit_button()
        sleep(2)
        self.assertEqual('login page', login1.return_title())
    def test_login2(self):
        login1 = adminIndexPage.AdminIndexPage(self.dr)
        login1.into_admin_page()
        login1.input_admin_name('super')
        login1.input_admin_password('123456')
        login1.click_submit_button()
        sleep(2)
        self.assertEqual('login page', login1.return_title())