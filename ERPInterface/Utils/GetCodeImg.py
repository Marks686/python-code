# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
import base64
from io import BytesIO
from PIL import Image
import pytesseract

class GetImgText(object):


    def open_url_get_src(self):
        """打开页面获取src，也就是base64的编码"""
        options = Options()
        options.headless = True # 如果你想让浏览器在后台运行，可以设置为 True
        # options.add_argument('-private')  # 启用私密浏览模式

        driver = webdriver.Firefox(options=options)
        driver.get("http://192.168.10.150/user/login")
        code = (by.CSS_SELECTOR, 'div[class="ant-col ant-col-10"] img')
        try:
            element = WebDriverWait(driver,10).until(EC.presence_of_element_located(code))
        except Exception as e:
            element = None
            print("元素没有获取到")

        return element.get_attribute("src")

    def get_img_text(self,data):
        """通过base64的编码来拿到识别之后的文本"""
        # 分割 data URL，获取 Base64 编码部分
        header, encoded_data = data.split(',', 1)

        # 解码 Base64 数据
        decoded_data = base64.b64decode(encoded_data)

        # 将解码后的数据转换为图像对象
        image = Image.open(BytesIO(decoded_data))

        text = pytesseract.image_to_string(image)
        return text

    def finally_get_text(self):
        """获取文本的最终方法"""
        return self.get_img_text(self.open_url_get_src()).replace(' ','').replace('-','')

if __name__ == '__main__':
    getimg = GetImgText()
    print(getimg.finally_get_text())