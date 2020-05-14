import time, datetime, os

def text():
    '''
    #读取存储积分文件生成列表
    '''
    try:
        file = open('jifen.txt','r')
    except IOError:
        error = []
        return error
    content = file.readlines()
    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]
    file.close()
    return content

def jf(userid):
    '''
    #主函数
    '''
    alreadysign=[userid, '今天已经签到过了哦！']
    with open("jfreset.txt", "r") as fs:
        datars = fs.read()
    with open("jifen.txt", "r") as f:
        data = f.read()
    if userid not in datars:
        if userid in data:
            for i in text():
                if userid in i:
                    with open("jifen.txt", "w") as f:
                            point = str(int(i[i.index(',')+3:-1]) + 1)
                            listA = [userid, point]
                            str1 = str(listA)
                            out = str1.strip('[]')
                            listold=[userid,str(int(out[out.index(',')+3:-1])-1)]
                            strold = str(listold)
                            outold = strold.strip('[]')
                            f.write(data.replace(outold,'') + out + '\n')
                            pass
                    with open("jfreset.txt", "a") as fs:
                        fs.write(userid+'\n')
        else:
            with open("jifen.txt", "a") as f:
                listA = [userid, '1']
                str1=str(listA)
                out = str1.strip('[]')
                f.write(out + '\n')
                with open("jfreset.txt", "a") as fs:
                    fs.write(userid + '\n')
    else:
        return alreadysign
    return listA

def timer(h=0, m=0):
    '''
    计时器 判断是否0点
    '''
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour==h and now.minute==m:
                break
            time.sleep(20)
        jfreset()

def jfreset():
    '''
    #每天0点重置可用签到次数
    '''
    path = 'jfreset.txt'
    print('0点重置签到次数了')
    if os.path.exists(path):
        os.remove(path)
        os.mknod("jfreset.txt")
    else:
        os.mknod("jfreset.txt")
    time.sleep(60)
    pass

jf('userid')
timer()