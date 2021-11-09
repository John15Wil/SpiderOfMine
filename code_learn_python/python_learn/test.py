a="zhenglong"
def test1():
    print("a")
    print(a)

def test2():
    f=open("/Users/long/Desktop/test.txt","r")
    # f.write("zhenglong nice body \n")
    # f.write("zhenglong nice body \n")
    # f.write("zhenglong nice body \n")

    read = f.readline()
    print("1"+read)

    read = f.readline()
    print("2"+read)
    f.close()

def testError():
    try:
        f = open('test.txt', 'r')
        print(f.read())
    except Exception:
        print('文件没有找到,请检查文件名称是否正确')

testError()