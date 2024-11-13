# 获取/关闭浏览器驱动的类
from selenium import webdriver


class DriverUtils:
    __driver = None

    # 获取浏览器驱动
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    # 关闭浏览器驱动
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None