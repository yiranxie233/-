import logging

# 创建日志器
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建文件处理器，输出到文件
file_handler = logging.FileHandler('./app.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 创建控制台处理器，输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

if __name__ == "__main__":
    logger.info("程序开始运行")
    a = [0, 1, 2, 3, 4, 5, 6]
    sum = 0
    for i in range(10):
        logger.debug("i = %d" % i)
        try:
            sum = sum + a[i]
            logger.debug("sum = %d" % sum)
        except IndexError as e:
            logger.error("索引越界")
            break
    logger.info("程序运行结束")
