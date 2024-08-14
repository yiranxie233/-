import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='./app.log',  # 如果不需要输出到文件，可以省略 filename 参数
                    filemode='w', # 'w' 表示每次运行程序时清空日志文件，'a' 表示追加日志
                    encoding='utf-8')  


if __name__ == "__main__":
    logging.info("程序开始运行")
    a = [0, 1, 2, 3, 4, 5, 6]
    sum = 0
    for i in range(10):
        logging.debug("i = %d" % i)
        try:
            sum = sum + a[i]
            logging.debug("sum = %d" % sum)
        except IndexError as e:
            logging.error("索引越界")
            break
    logging.info("程序运行结束")