import configparser
import os


def get_database():
    cfg = configparser.ConfigParser()

    path = os.path.dirname(os.path.dirname(__file__)) + '/Config/db.ini'

    cfg.read(path, encoding='utf-8')
    data = dict(cfg.items('database'))
    # 修改端口号为int类型
    data["port"] = int(data["port"])
    return data


if __name__ == '__main__':
    print(get_database())