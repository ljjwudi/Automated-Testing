import logging


def setup_logging():
    # 创建Logger对象
    logger = logging.getLogger('interface_test')
    logger.setLevel(logging.DEBUG)

    # 创建文件处理器，将日志写入文件
    file_handler = logging.FileHandler('interface_test.log')
    file_handler.setLevel(logging.DEBUG)

    # 创建控制台处理器，将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到Logger对象
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    data = 'sss'
    logger = setup_logging()
    logger.debug(data)
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
