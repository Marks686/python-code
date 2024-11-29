# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(browser: str):
    """
    封装打开浏览器的函数
    :param browser: 具体打开的浏览器 chrome firefox edge
    :return:
    """
    if browser.lower() == 'chrome':
        return webdriver.Chrome()
    elif browser.lower() == 'firefox':
        return webdriver.Firefox()
    elif browser.lower() == 'edge':
        return webdriver.Edge()

    else:
        print("输入的浏览器不合法,请输入 chrome firefox edge")
        return None


class Base(object):
    def __init__(self, browser="chrome"):
        self.driver = open_browser(browser)
        self.driver.maximize_window()

    def open_url(self, url: str):
        """
        打开网页
        :param url:网页的地址,可以输入域名
        :return:
        """
        try:
            # 判断输入的网址是否是 http://或者https://开头,是就直接打开,不是就在前面加上http://
            if url.startswith('http://') or url.startswith('https://'):
                self.driver.get(url)
            else:
                url = "http://" + url
                self.driver.get(url)
        except Exception as e:
            print(f"网页打开失败,失败提示:{e}")
            print(f"输入网址是{url}")

    def find_element(self, locator: tuple, timeout=20):
        """
        单个元素定位,成功返回元素,失败返回False
        :param locator: 定位器
        :param timeout: 超时时间
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

        except Exception as e:
            print(f"元素“{locator}”定位失败{e}")
            return False

    def find_elements(self, locator: tuple, timeout=20):
        """
        多个元素定位,定位成功返回元素列表,失败返回False
        :param locator:定位器
        :param timeout: 超时时间
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            print(f"元素定位失败{e}")
            return False

    def send_keys(self, locator: tuple, text: str, timeout=20):
        """
        定位之后进行输入内容
        :param text: 输入的文本信息
        :param locator: 定位器
        :param timeout: 超时时间
        :return:
        """
        element = self.find_element(locator, timeout)
        if element is not False:
            element.send_keys(str(text))
        else:
            print("元素定位失败了,不能输入信息")

    def click(self, locator: tuple, timeout=20):
        """
        根据输入元素进行点击
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        if element is not False:
            element.click()
        else:
            print("元素定位失败了,不能点击")


    def js_click(self, locator: tuple, timeout=20):
        """
        根据输入元素进行点击,因为其他元素遮挡，使用js的点击方法
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        if element is not False:
            # self.driver.execute_script("arguments[0].click();", element)
            self.driver.execute_script("""
                        var event = new MouseEvent('click', {
                            bubbles: true,
                            cancelable: true,
                            view: window
                        });
                        arguments[0].dispatchEvent(event);
                    """, element)
        else:
            print("元素定位失败了,不能点击")


    def clear(self, locator: tuple, timeout=20):
        """
        根据输入元素进行清空
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        if element is not False:
            element.clear()
        else:
            print("元素定位失败了,不能清空")

    def get_attribute(self,locator,attribute_name):
        """
        获取元素的属性
        """
        element = self.find_element(locator)
        if element is not False:
            return element.get_attribute(attribute_name)
        else:
            print("元素定位失败了,不能清空")

    def is_selected(self, locator: tuple, timeout=20):
        try:
            element = self.find_element(locator, timeout)
        except Exception as e:
            print(f"元素未找到{e}")
        else:
            return element.is_selected()

    def scroll_bar(self, x, y):
        """
        滚动条方法封装
        :param x: 横向移动,x初始为0
        :param y: 纵向移动,y初始为0
        :return:
        """
        js = f"window.scrollTo({x},{y})"
        self.driver.execute_script(js)

    def get_element_text(self, locator: tuple, timeout=20):
        """获取元素的文本信息"""
        element = self.find_element(locator, timeout)
        if element is not False:
            return element.text
        else:
            return None

    def get_text_assert(self, expected, locator: tuple, timeout=20):
        """
        获取文本信息进行断言
        :param expected: 预期结果
        :param locator: 定位器
        :param timeout: 超时时间
        :return: 预期内容和文本相等返回 True  不同返回False
        """
        text_content = self.get_element_text(locator, timeout)
        if text_content is not None:
            if expected == text_content:
                return True
            else:
                return False
        else:
            return False

    def get_text_assert_in(self, expected, locator: tuple, timeout=20):
        """
        获取文本信息进行断言
        :param expected: 预期结果
        :param locator: 定位器
        :param timeout: 超时时间
        :return: 预期内容在获取内容里面返回 True  不同返回False
        """
        text_content = self.get_element_text(locator, timeout)
        if text_content is not None:
            if expected in text_content:
                return True
            else:
                return False
        else:
            return False


    def send_keys_tab(self, locator: tuple, timeout=20):
        """
        键入tab
        """
        element = self.find_element(locator, timeout)
        if element is not False:
            element.send_keys(Keys.TAB)
        else:
            print("元素定位失败了,不能输入信息")

    def refresh(self):
        """页面刷新"""
        self.driver.refresh()

    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    # open_browser('chrome')
    # open_browser("Edge")
    bs = Base('chrome')
    bs.open_url('http://192.168.10.150/dashboard/analysis')

