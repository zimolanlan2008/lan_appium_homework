from page.app import App


class TestContact:
    def setup(self):
        self.app = App()

    def test_contact(self):
        self.app.goto_main().goto_contactlist().goto_addmemberlist().goto_manualadd().adding("lantesta1","13300000031","惠康家园")

    def test_1(self):
        self.app.app_start().goto_main().goto_contactlist().goto_addmemberlist().goto_manualadd().adding("lantesta1","13300000031","惠康家园")