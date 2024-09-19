import datetime
import pytz


def transfer_gmt_time(gmt_time):

    # 将GMT时间转换为datetime对象
    gmt_datetime = datetime.datetime.strptime(gmt_time, '%a, %d %b %Y %H:%M:%S %Z')

    # 获取本地时区
    local_tz = pytz.timezone('Asia/Shanghai')

    # 将datetime对象转换为指定格式的字符串
    local_time = gmt_datetime.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time = datetime.datetime.strptime(str(local_time), '%Y-%m-%d %H:%M:%S%z')
    time_str = time.strftime('%Y%m%d%H%M')
    return time_str