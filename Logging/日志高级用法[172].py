# 1. 导包
import logging
import logging.handlers
# 2. 创建日志器对象 / 设置日志级别
# logger = logging.getLogger()      # 默认日志器名称为 root
logger = logging.getLogger("Jay")   # 自定义日志器名称为 Jay
logger.setLevel(level=logging.DEBUG)
# 3. 创建处理器对象: 输出到控制台 + 文件(按时间切割)
ls = logging.StreamHandler()
lf = logging.handlers.TimedRotatingFileHandler(filename="172.log", when="s", backupCount=3)
# 4. 创建格式器对象
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(funcName)s:%(lineno)d] - %(message)s"
formatter = logging.Formatter(fmt=fmt)
# 5. 将格式器添加到处理器
ls.setFormatter(formatter)
lf.setFormatter(formatter)
# 6. 将处理器添加到日志器
logger.addHandler(ls)
logger.addHandler(lf)
# 7. 打印日志
while 1:
    logger.debug("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")