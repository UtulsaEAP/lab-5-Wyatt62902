'''
Name: Wyatt Fulton
Lab Time: Thur 2:00PM
'''
def fibonacci(n):
    flist = [0,1]
    if n == 0:
        output = 0
    elif n < 0:
        output = -1
    else:
        flist = flist*n
        for i in range(2, n, 1):
            flist[i] = flist[i-1]+flist[i-2]
        output = n-1
    return output



if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
    