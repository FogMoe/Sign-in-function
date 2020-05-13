def text():
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
    with open("jifen.txt", "r") as f:
        data = f.read()
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

    else:
        with open("jifen.txt", "a") as f:
            listA = [userid, '0']
            str1=str(listA)
            out = str1.strip('[]')
            f.write(out + '\n')
    return listA

jf('userid')