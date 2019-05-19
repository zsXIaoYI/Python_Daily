# -*- coding: utf-8 -*-

import pymysql
import time,datetime
from sshtunnel import SSHTunnelForwarder
import xlwt


vip_conf = {
    "host": "10.13.15.14",
    "username": "vip_r",
    "password": "0EW6XtQdJvs13Su40",
    "db": "mryt_vip",
}
oms_conf = {
    "host": "10.13.15.26",
    "username": "oms_r",
    "password": "0EW6XtQdJvs13Su42",
    "db": "mryt_oms",
}


def write_to_excel(data, file_name, fileds):
    """ 写入Excel文件 """
    # 实例化一个Excel
    wbk = xlwt.Workbook()
    # 添加该Excel的第一个sheet，如有需要可依次添加sheet2等
    sheet1 = wbk.add_sheet('sheet1', cell_overwrite_ok=True)
    # EXCEL新表的第一行  写入字段信息
    for i in range(0, len(fileds)):
        sheet1.write(0, i, fileds[i])

    # for row in range(1, len(data)+1):
    #     for col in range(0, len(fileds)):
    #         sheet1.write(row, col, data[row-1][col])
    for row in range(1, len(data)+1):
        for col in range(0, len(fileds)):
            # print("kay=%s, value=%s" % (fileds[col], data[row-1][fileds[col]]))
            sheet1.write(row, col, to_str(data[row-1][fileds[col]]))
    wbk.save(file_name)


def get_from_vip(sql, *params):
    """ 从vip-center获取数据 """
    with SSHTunnelForwarder(  # ssh的地址，端口，用户名，密码
            ('192.144.169.117', 22),
            ssh_password="25YQko#&R&Z0",
            ssh_username="rd",
            remote_bind_address=(vip_conf["host"], 3306)) as server:
        server.start()
        conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                               port=server.local_bind_port,
                               user=vip_conf["username"],
                               password=vip_conf["password"],
                               db=vip_conf["db"],
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                # .cursor()用来获得python执行Mysql命令的方法
                # select = sql
                cursor.execute(sql, params)
                return cursor.fetchall()        # fetchall()则是接收全部的返回结果行
        except Exception as e:
            print("Reason", e)
        finally:
            conn.close()
            server.stop()


def get_from_oms(sql, params):
    """ 从vip-center获取数据 """
    with SSHTunnelForwarder(  # ssh的地址，端口，用户名，密码
            ('192.144.169.117', 22),
            ssh_password="25YQko#&R&Z0",
            ssh_username="rd",
            remote_bind_address=(oms_conf["host"], 3306)) as server:
        server.start()
        conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                               port=server.local_bind_port,
                               user=oms_conf["username"],
                               password=oms_conf["password"],
                               db=oms_conf["db"],
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as cursor:
                # .cursor()用来获得python执行Mysql命令的方法
                # select = sql
                cursor.execute(sql, params)
                return cursor.fetchall()        # fetchall()则是接收全部的返回结果行
        except Exception as e:
            print("Reason", e)
        finally:
            conn.close()
            server.stop()


def to_str(data):
    """ 格式化datetime """
    if isinstance(data, datetime.datetime):
        return data.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return data


if __name__ == "__main__":
    start_time = int(round(time.time() * 1000))
    sql = "SELECT bi.user_id AS '总监id'," \
            "(CASE bi.real_name WHEN NULL THEN bi.nick_name ELSE bi.real_name END) AS '姓名'," \
            "bi.phone_number '手机号'," \
            "(SELECT real_name FROM t_vip_base_info WHERE user_id = lr.gm_uid) AS '上级'," \
            "(SELECT real_name FROM t_vip_base_info WHERE user_id = bi.invite_user_id) AS '推荐人'," \
            "IFNULL(ttt.count, 0) as '7日新增', " \
            "bi.leader_ctime AS '入驻时间' " \
          "FROM t_vip_base_info bi " \
          "LEFT JOIN t_vip_level_record lr ON lr.user_id = bi.user_id AND lr.LEVEL = 2 " \
          "LEFT JOIN (" \
            "SELECT leader_id,count(leader_id) AS count from (" \
            "SELECT bi1.user_id, bi1.create_time,substring_index(substring_index(la.path,'/',2),'/',-1) " \
            "leader_id, bi2.leader_ctime FROM t_vip_layer la " \
            "LEFT JOIN t_vip_base_info bi1 ON bi1.user_id=la.user_id " \
            "LEFT JOIN t_vip_base_info bi2 ON bi2.user_id=substring_index(substring_index(la.path,'/',2),'/',-1) " \
            "WHERE bi1.is_valid=1 AND bi1.LEVEL=1 " \
            "AND DATE_SUB(CURDATE(),INTERVAL %s DAY)<=bi1.create_time " \
            "AND bi1.create_time<%s  AND bi1.create_time>=%s AND bi1.create_time>=bi2.leader_ctime) tt " \
            "GROUP BY tt.leader_id) ttt on ttt.leader_id = bi.user_id " \
          "WHERE bi.LEVEL = 2 AND bi.is_valid = 1 ORDER BY bi.leader_ctime desc;"
    results = get_from_vip(sql, 31, "2018-12-07", '2018-12-06')
    # for row in results:
    #     uid = row["总监id"]
    #     payment_sql = "select IFNULL(sum(payment),0) as payment, leader_uid " \
    #                   "from t_cps_order " \
    #                   "where pay_time>DATE_SUB(CURDATE(),INTERVAL 31 DAY) and leader_uid != user_id and leader_uid=%s"
    #     payment_result = get_from_oms(payment_sql, uid)
    #     print(uid)
    #     print(payment_result)
    #     row["近30日销售总额"] = payment_result[0]["payment"]
    uid_arr = []
    for row in results:
        uid_arr.append(row["总监id"])
    arg_list = ','.join(['%s']*len(uid_arr))

    payment_sql = "select IFNULL(sum(payment),0) as payment, leader_uid from t_cps_order " \
                  "where pay_time>DATE_SUB(CURDATE(),INTERVAL 31 DAY) and leader_uid != user_id " \
                  "and leader_uid in (%s) GROUP BY leader_uid" % arg_list
    payment_result = get_from_oms(payment_sql, tuple(uid_arr))
    if payment_result is not None:
        for row in results:
            row["近30日销售总额"] = 0
            for row_1 in payment_result:
                if row["总监id"] == row_1["leader_uid"]:
                    row["近30日销售总额"] = row_1["payment"]

    print(results)
    # 列
    # fileds = ['总监id', '姓名', '手机号', '上级', '推荐人', '7日新增', "入驻时间", "近30日销售总额", "销售总额"]
    fileds = ['总监id', '姓名', '手机号', '上级', '推荐人', '7日新增', "入驻时间", "近30日销售总额"]

    # 获取当前时间
    fileName = "咨询顾问数据_" + time.strftime("%Y%m%d") + ".xls"
    write_to_excel(results, fileName, fileds)

    end_time = int(round(time.time() * 1000))
    print("总耗时%sms" % (end_time-start_time))
    pass
