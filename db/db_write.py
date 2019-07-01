import pymysql
 
db = pymysql.connect("localhost","root","12345","bs" )

 
doc = open('../recommend/ml-100k/movie','r',encoding='UTF-8')
data=[]
for line in doc.readlines():
    arr=[]
    lines=line.strip().split('|')
    for x in lines:
        arr.append(x)
    data.append(arr)
cursor = db.cursor()
for i in data:
    sql = "INSERT INTO movie values('%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' )" % (i[0],i[1].replace('\'','@'),i[2],i[4].replace('\'','@'),i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23])
    cursor.execute(sql)
        # 执行sql语句
    db.commit()
    print(str(i[1])+'写入完成')
 
# 关闭数据库连接
db.close()
