# coding=utf-8
from selenium import webdriver


class Web:

    def __init__(self):
        """
        打开chrome浏览器
        """
        self.driver = None
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def baidu(self):
        """
        百度疫情
        :return:
        """
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("疫情")
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        self.driver.find_element_by_xpath('//*[@id="1"]/div/div/div[1]/p/a').click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def getyiqing(self):
        ele = self.driver.find_element_by_xpath('//*[@id="ptab-0"]/div[2]/table')
        text = ele.get_attribute('innerText')
        return text









