import logging

logging.basicConfig(
    level=logging.DEBUG,  # 控制台打印的日志级别
    filename='flask.log',  # 将日志写入log_new.log文件中
    filemode='w',  ##模式，a追加，w覆盖
    # format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'#完整日志格式
    format='%(asctime)s - %(levelname)s: %(message)s'  # 日志格式
)

logging.debug('abc')