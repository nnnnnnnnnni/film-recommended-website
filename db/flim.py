import pymysql
 
db = pymysql.connect("localhost","root","12345","bs" )

array_tp1=['动作','冒险','动画','儿童','喜剧','犯罪','纪录片','戏曲','奇幻','黑色电影','恐怖','音乐','悬疑','爱情','科幻','惊悚','战争','西部']
array_tp2=['Action','Adventure','Animation',"Children's",'Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','SciFi','Thriller','War','Western']

def itemcf(userId):
    sql='''select * from bs.movie where movieId in
        (select mls.movieId AS movieId from
            (select movieId from bs.rating 
            where userId in 
                (select ls.user2Id as userId from 
                    (select user2Id from bs.pcc where user1Id ='%s' and user2Id<>user1Id order by pcc limit 5) as ls)
            group by movieId order by avg(rating) desc,count(movieId) desc limit 5 )as mls) 
            ''' %(userId)
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    data= []
    arr=[]
    for i in res:
        arr.append(i)
    index =1
    for i in arr:
        data.append({
            'rank' :index,
            'title':i[1],
            'time' :i[2],
            'url'  :i[3]
        })
        index+=1
    return data

def rmd(userId):
    sql='''select * from movie where movieId in
            (select ls.movieId as movieId from 
                (select movieId from rmd where userId='%d' order by rating desc limit 5 ) as ls) 
            ''' %(int(userId))
    sql2='''select * from bs.movie where movieId in
        (select mls.movieId AS movieId from
            (select movieId from bs.rating 
            where userId in 
                (select ls.user2Id as userId from 
                    (select user2Id from bs.pcc where user1Id ='%s' and user2Id<>user1Id order by pcc limit 5) as ls)
            group by movieId order by avg(rating) desc,count(movieId) desc limit 5 )as mls) 
            ''' %(userId)
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor = db.cursor()
    cursor.execute(sql2)
    res2 = cursor.fetchall()
    data= []
    arr=[]
    for i in res:
        arr.append(i)
    for i in res2:
        arr.append(i)
    index =1
    for i in arr:
        data.append({
            'rank' :index,
            'title':i[1].replace('@','\''),
            'time' :i[2],
            'url'  :i[3]
        })
        index+=1
    return data


def tp(userid,tp):
    for i in tp:
        if(i not in array_tp1):
            tp.remove(i)
    if(len(tp)==3):
        sql='''select * from bs.movie where movieId in
            (select ls.movieId as movieId from 
                (select * from bs.rmd where userId ='%d' and movieId in 
                    (SELECT movieId FROM bs.movie where %s =1 and %s =1 and %s =1 ) order by rating desc limit 10) as ls)
                    ''' %(int(userid),array_tp2[array_tp1.index(tp[0])],array_tp2[array_tp1.index(tp[1])],array_tp2[array_tp1.index(tp[2])])
    if(len(tp)==2):
        sql='''
        select * from bs.movie where movieId in
            (select ls.movieId as movieId from 
                (select * from bs.rmd where userId ='%d' and movieId in 
                    (SELECT movieId FROM bs.movie where %s =1 and %s =1 ) order by rating desc limit 10) as ls)
                    ''' %(int(userid),array_tp2[array_tp1.index(tp[0])],array_tp2[array_tp1.index(tp[1])])
    else:
        sql='''
        select * from bs.movie where movieId in
            (select ls.movieId as movieId from 
                (select * from bs.rmd where userId ='%d' and movieId in 
                    (SELECT movieId FROM bs.movie where %s=1 ) order by rating desc limit 10) as ls)
                    ''' %(int(userid),array_tp2[array_tp1.index(tp[0])])
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    data= []
    arr=[]
    for i in res:
        arr.append(i)
    index =1
    for i in arr:
        data.append({
            'rank' :index,
            'title':i[1].replace('@','\''),
            'time' :i[2],
            'url'  :i[3]
        })
        index+=1
    return data