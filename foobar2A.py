def fibo_sum(n):
    a=0
    b=1 
    sum = 0
    count = 0
    while( sum <= n):
        temp = a 
        a = b 
        b = temp +b
        sum = sum  + a 
        count +=1 
    return count-1



def square_sum(n):
    sum = 0
    num = 1 
    count = 0
    while(sum <= n):
        sum += num 
        num *= 2 
        count +=1 
    return count-1

def solution(total_lambs):
    return fibo_sum(total_lambs) - square_sum(total_lambs)
