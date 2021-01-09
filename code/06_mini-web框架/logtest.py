import logging

#  同时将log日志输出到控制台和文件

# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)       # log等级总开关

# 创建一个handler，用于导入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile,mode = 'a')
fh.setLevel(logging.DEBUG)

# 创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# 定义handler输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s(line:%(lineno)d] - %(levelname)")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将logging添加到logger里面