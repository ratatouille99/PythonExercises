def SameParity(n,k):
    t1 = 0
    t2 = 0
    
    if(n<k):
        print('NO')
            
    elif(n / k == 1):
        print('YES') 
        for i in range(n):
            print(1 , ' ')
            
    else: 
        t1 = n - (k-1)
        t2 = n - 2*(k-1)
        
        if(t1 % 2 == 1 and t1 > 0):
            print('YES')
            for i in range(k-1):
                print(1 , ' ')
            print(t1)
            
        elif(t2 % 2 == 0 and t2 > 0):
            print('YES')
            for i in range(k-1):
                print(2 , ' ')
            print(t2)
            
        else:
            print('NO')
                
                
t = int(input())
n = 0
k = 0

while(t != 0):
    
    n = int(input())
    k = int(input())
    SameParity(n,k)
    t -= 1
    
