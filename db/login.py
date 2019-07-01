import pymysql
 
db = pymysql.connect("localhost","root","12345","bs" )
cursor = db.cursor()

def login(userId,password):
    sql_login="select * from user where userCount = '%s'" %(userId)
    cursor.execute(sql_login)
    i = cursor.fetchall()
    if(len(i)>0):
        res = i[0]
        if(res[0] == password):
            return {
                'code'         : 200,
                'userId'       : res[0],
                'userAge'      : res[1],
                'userSex'      : res[2],
                'userJob'      : res[3]
            }
        else:
            return{
                'code' : 404,   #密码错误
                'info' : '密码错误'
            }

    else: 
        return {
            'code' : 401 ,    #账号不存在
            'info' : '账号不存在'
        }
    db.close()

