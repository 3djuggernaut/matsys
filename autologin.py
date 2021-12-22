from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import requests

class loginProcess:
    url="http://10.253.0.237/srun_portal_pc?ac_id=1&theme=dx"
    url2="http://aaa.uestc.edu.cn/"
    driver=None
    account="学号"
    passwd="密码"
    account_xpath="/html/body/div[2]/div/div[1]/form/input[8]"
    passwd_xpath="/html/body/div[2]/div/div[1]/form/input[9]"
    loginButton_xpth="/html/body/div[2]/div/div[1]/div/button[1]"

    def __init__(self) -> None:
        opts=Options()
        opts.headless=True
        self.driver=webdriver.Chrome(options=opts)
    
    def press(self,xpath:str):
        ele=self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def inputTxt(self,xpath:str,txt:str):
        ele=self.driver.find_element_by_xpath(xpath)
        ele.send_keys(txt)

    def login(self):
        self.driver.get(self.url)
        time.sleep(10)
        self.inputTxt(self.account_xpath,self.account)
        self.inputTxt(self.passwd_xpath,self.passwd)
        self.press(self.loginButton_xpth)
        self.driver.close()
        return 
        

def test_online():
	try:
		result=requests.get('http://10.253.0.237/cgi-bin/rad_user_info',timeout=3)
		if result.text == "not_online_error":
			return False
		return True
	except:
		return False

if __name__=='__main__':
	old_ip=""
	while True:
		if not test_online():
			l=loginProcess()
			l.login()
		else:
			print("device online!")
		time.sleep(10)  
