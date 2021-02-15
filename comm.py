# 通用代码模块
import datetime
import sqlite3

# 获取当前日期压缩字符串
def get_today_str():
    return datetime.datetime.now().strftime('%Y%m%d')


# 获取日期+流水码格式的标识符
# get_pid() 获取项目标识pid，比选T_Projects
def get_pid():
    # 将T_Projects数据表中pid中与当前日期相同的
    conn = sqlite3.connect('./data/lpm_c.db')
    query_sql = "SELECT pid FROM T_Projects WHERE pid LIKE '" + get_today_str() + "%'"
    # print(query_sql)
    cursor = conn.execute(query_sql)
    stream_code = []
    for row in cursor:
        stream_code.append(int(row[0][8:]))
    conn.close()
    # 若流水码为空，则返回序号0001
    if len(stream_code) == 0:
        return "%s%04d"%(get_today_str(),1)
    else:
        return "%s%04d"%(get_today_str(),max(stream_code)+1)

# get_ppid() 攻取项目与产品的销售对照记录标识ppid，比选T_Sale
def get_ppid():
    # 将T_Sale数据表中ppid中与当前日期相同的
    conn = sqlite3.connect('./data/lpm_c.db')
    query_sql = "SELECT ppid FROM T_Sale WHERE ppid LIKE '" + get_today_str() + "%'"
    # print(query_sql)
    cursor = conn.execute(query_sql)
    stream_code = []
    for row in cursor:
        stream_code.append(int(row[0][8:]))
    conn.close()
    # 若流水码为空，则返回序号0001
    if len(stream_code) == 0:
        return "%s%04d" % (get_today_str(), 1)
    else:
        return "%s%04d" % (get_today_str(), max(stream_code) + 1)

