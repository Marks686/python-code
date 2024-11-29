# -*- coding:utf-8 -*-

"""
OCR识别
    1.pytesseract库
        0.pip install pytesseract
        1.pytesseract是谷歌开发的，是一个开源的OCR识别工具
        2.需要安装本地的引擎 tesseract-ocr-w64-setup-v5.3.0.20221214.exe
        3.双击安装，选择安装位置，记录好安装的位置，比如：D:\Program Files (x86)\Tesseract-OCR
        4.配置tesseract环境变量，配置系统里面的 Path 添加路径 D:\Program Files (x86)\Tesseract-OCR
        5.对英文和阿拉伯数字识别比较友好

    2.easyocr
        0.pip install easyocr
        1.第三方开发的一个开源的识别库
        2.不需要安装本地的引擎，可以直接使用
        3.识别算法如果说有GPU资源会更快，没有使用CPU进行计算也可以

    3.ddddocr
        0.pip install ddddocr
        1.中国开发的一个ocr库，对于中文文本的识别更加友好
        2.会存在开源的广告信息
        3.不需要安装本地的引擎

    4.ERP项目里面都可以去使用，从识别准确上来讲，推荐pytesseract库和ddddocr

"""



import base64
from io import BytesIO
from PIL import Image
import pytesseract
import easyocr
import ddddocr


class GetImgText(object):
    def __init__(self,data):
        self.data = data

    def get_image_object(self):
        """
        获取image对象
        """
        # 分割 data URL，获取 Base64 编码部分
        header, encoded_data = self.data.split(',', 1)

        # 解码 Base64 数据
        decoded_data = base64.b64decode(encoded_data)

        # 将解码后的数据转换为图像对象
        image = Image.open(BytesIO(decoded_data))
        return image


    def get_img_text(self):
        """
        使用pytesseract进行图文识别
        """
        # 获取图像对象
        image = self.get_image_object()

        text = pytesseract.image_to_string(image)
        text = text.replace(' ','').replace('-','').replace('.','').replace(')','j').replace('|','l').replace('}','j').replace('/','').replace(':','').replace("'",'')

        return text.lower()


    def get_easy_text(self):
        """
        使用easyocr进行识别
        """
        # 将解码的数据转为 PIL 图像对象
        image = self.get_image_object()

        # 创建 EasyOCR Reader 实例
        reader = easyocr.Reader(['en'])
        # 使用 easyocr 进行文本识别
        result = reader.readtext(image)
        print(result)

        return result[0][1].replace(' ','')


    def get_dddd_text(self):
        """
        使用ddddocr进行识别
        """
        # 将图像数据加载到 PIL Image 对象
        image = self.get_image_object()

        # 初始化 ddddocr 对象
        ocr = ddddocr.DdddOcr()

        # 将 PIL 图像对象转换为字节数据
        image_bytes = BytesIO()
        image.save(image_bytes, format='PNG')
        image_bytes = image_bytes.getvalue()

        # 进行 OCR 识别
        result = ocr.classification(image_bytes)
        return result


if __name__ == '__main__':
    data = "data:image/jpg;base64,/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAjAGkDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3aRZ5PtET7ljcBY3iOGAIwTknqOvTpjqeAkk2J5E+0GI/IiB48LvOTwT97PAwDxjsacZxDLKbiaKOPgxhsKccZOc8jJA6DHvkV5L8Q/F3jCWbWPD3hqya1h06zluNS1li6hdqLMVhbPytsZRjkgycbQu8gHrTGaeGKWFmiLbWKSADgkEg8HBxkfj+U5B3htxwARt4wff/AD61wXwpv9Q1T4TaTc3cs1/dzJcb5bqQyF8TuoDFjluOACccYyK6+S5a0gigKxrOSqIFQiNucAZ6LkDpkkf7XGQCSOSdLhRMsm13dV+dCABkgngHJHQDPA571ZjTy4kj3M21QNzHJOO5PrXgeg6PefHPVtY1XWtS1K28LW1wYtPtLeVU+cEkFlO8bgj8nHWTCkKu0dD8OtZ8QWnivW/h54ivptTn08Lcw3wlPmGIlCQzk7j/AKxCB1ALjJwooA9VXzzDOMsH3MIy20HHbkZGM9CR06g95I2MgWTDpwQY2AHPv9MdjjnvxUcCxhY1MyzDl4Sxy23GM579cZ9CM56nzPRvjVpniDWdM0zRNK1u/eZ/9KJtU3QISVDsVbAAYpk4wFbOcjBAPSpXuIZAkMSyK/Qu7DB5JycHjpjjHUccAywzGcF1C+UfusCcn1BBHBB4x/KmWs0svnCZUVo5WQBT/D1Un3wR6/h0EN9dQaRa3F9cXIitII5Lm5LhpGCKuSV5yAPQA+woAlaSO2mmeSeQ7gH2EZCdF4wM8nt3Ocd6mlk8qF5NjvsUttQZZsdgPWvKj8ctHkjtL240DXrXRJ5o0j1G4swYXfc4YZBP3doYbSzEqwwMc+m217Fe/Z5beUNFLCsyFSrLKjDgqwJBxxyCRhh1yDQAQXbXF2VRUNuYg6tn5idxGfTaQAQe/vzi3TJZPKjL7HcDqEGTj6d/5+mafQBDcWy3Cj53jcAhZIzhgD1Gff8AoD1ANcX468SaFB4N8Rafc61p0GqPpdwj2b3EccrSNCQBsJ3ZPGOuQRjPBrtEjZrkzSBflBSMYwVBIzk5IOcA9BiuV1v4W+DfEesT6tq2jfaL6fb5kv2qZN21Qo4VwBwAOBQBzvwT17RX+HOi6G2qWJ1PbPmyM6+aQZpW+5nJ+UZx6c9DXos9l9onctu2hQV3NuQsQQRt64xtzyM8ju2eZ8P/AAu8GeHdVh1bSdIeC+t2cRytcTErkMp+VmwRgkDjpz711ixzM5M0gwkpaPy8jK7cYbPXkn8gfagZ478GLi18M2niLwVrVwLXVrPUXmKGQxmdPLHzRDIdhiItwPusp703wRe/238ePGHiDTQl5YR2kdn58LjY0hMKKR3KnyZDuGQAOp4z3mtfDjwf4m1SW61bQkluchmlUtF5hIA3FoyC33QMMTjGQBuy2r4e8PaX4X01tH0axaytQzSKy/NuZupLHJJHA+bnCgcgUCNIx4MUKqFKncjLGNqAEDb7EqSPz+leT/s4/wDJPNQ/7Csn/oqKvWPMmNrIyKjyBcxkH5ZDtBB68DPHX8ay/DPh3QfCmmXFl4ftlgtfPaWWNJXmPmbQD94sc4VeP0oA0o5Lh4n3BhLC5BxGFEoxn5cseCD1z1HPcVgeMW0P/hD9STxDttND8gQyyfZy7Kj7VRkG07WVyMDacFVOBXU1R+zT3Iuba+FvPZSF0MUkO7zY2H3TzjHJXBHIHvQB84SJ4g8MfDqPVNM8W6PrXhUyQtJpuowxSs8p2EW5jO/BVAhKB1K7WIHAY/QXhrUorzw3pV4LWCwtbq0t5LWBGAWNXjUiIdOV5AwAMYx3xysPwh+H0d1b3Fr4dWUwt5pQ3cr5IzgOjvggkEEHuMEYzXfW48ixiEpC+XGNxICgYHPA4H4cUATbhuC85Iz04/OlqBZXnaNohiIMdxJ+8McY4IIOQcgj+YqegApHRZEZHUMrDBUjII9KKKAGxQxQRCOGNI416KigAfgKURors6ooZsbmA5OOmaKKAHUjosiMjqGRhhlYZBHoaKKAEijWGJIkGERQqgnPAp1FFAET28Uk8U7pmSLOw5PGRg0940k27hkqwZT0IP8An+dFFAChFDlwo3EAFsckDOB+p/OloooAKKKKAP/Z"
    getText = GetImgText(data)
    print(getText.get_img_text())
    print(getText.get_easy_text())
    print(getText.get_dddd_text())

