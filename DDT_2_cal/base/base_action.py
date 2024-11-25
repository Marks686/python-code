class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_el(self, feature):
        return self.driver.find_element(*feature)

    # 定位数字按钮
    def find_el_num(self, feature, num):
        return self.driver.find_element(feature[0], feature[1].format(str(num)))
    # simple{}.format(str(num))

    def find_els(self, feature):
        return self.driver.find_elements(*feature)

    def click(self, feature):
        return self.find_el(feature).click()

    def input(self, feature, content):
        return self.find_el(feature).send_keys(content)

    def clear(self, feature):
        return self.find_el(feature).clear()