import logging

fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(funcName)s:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.INFO, format=fmt)

logging.debug("这是一条调试信息")
logging.info("这是一条普通信息")
logging.warning("这是一条警告信息")
logging.error("这是一条错误信息")
logging.critical("这是一条严重错误信息")
