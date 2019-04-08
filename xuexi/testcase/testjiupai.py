from macaca import WebDriver
import  unittest,time,HTMLTestRunner,BSTestRunner,ddt
from data.config import desired_caps,server_url,login_data
from bussines.login import login


@ddt.ddt
class Jiupai(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver(desired_caps,server_url)
        self.driver.init()
        self.driver.maximize_window()
        self.driver.get('https://sso.jiupaicn.com/sso/action/goLogin?retUrl=http%3A%2F%2Fjphao.jiupaicn.com%2Findex.php%3F')


    def tearDown(self):
        self.driver.quit()

    @ddt.data(*login_data)
    def test_login(self,login_data):
        login(self.driver,login_data['username'],login_data['password'])
        time.sleep(2)
        self.assertEqual(self.driver.element_by_class_name(login_data['class']).text,login_data['text'])
