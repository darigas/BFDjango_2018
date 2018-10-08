if __name__ == '__main__':
    n = int(input())

    somelist = input().split()
    mymax = max(somelist)
    while (mymax in somelist):
    	somelist.remove(mymax)

    print(max(somelist))