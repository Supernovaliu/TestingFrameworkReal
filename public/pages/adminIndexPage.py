from public.common import basepage

class AdminIndexPage(basepage.Page):

    def into_admin_page(self):
        """open login page"""
        self.dr.open('http://localhost/admin/login')

    def input_admin_name(self,values):
        """input administrator name"""
        self.dr.type('name->name',values)

    def input_admin_password(self,values):
        """input administrator password"""
        self.dr.type('name->pass',values)

    def click_submit_button(self):
        """submit"""
        self.dr.click('name->submit')

    def return_title(self):
        """return index title"""
        return self.dr.get_title()