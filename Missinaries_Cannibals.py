left = []
right = ['M','M','M','C','C','C']
flag = 0
def count_M(a):
    M_count = 0
    for i in a:
        if i == 'M':
            M_count +=1
    return M_count
    
def count_C(a):
    C_count = 0
    for i in a:
        if i == 'C':
            C_count +=1
    return C_count

print(left,'-----------------',right)

round_no = 0
while 1:
    print('Select 1 or 2 of them Missionaries and Cannibals (M/C):')
    round_no += 1
    if round_no%2 != 0:
        print('RIGHT TO LEFT')
    else:
        print('LEFT TO RIGHT')
        
    ip = list(input().rstrip().split())
    for i in ip:
        if round_no%2 != 0:
            left.append(str(i))
            if i == 'M':
                right.remove('M')
            elif i == 'C':
                right.remove('C')

        else:
            right.append(str(i))
            if i == 'M':
                left.remove('M')
            elif i == 'C':
                left.remove('C')
                
    print(left,'-----------------',right)
    if len(left) == 6:
        flag =1
        break
    elif count_M(right) < count_C(right) and count_M(right)!= 0 or count_M(left) < count_C(left)and count_M(left) != 0:
        break

if flag == 1:
    print('Bravo')
else:
    print('Eaten by Cannibal')
    
