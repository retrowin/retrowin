n = int(input())
i = 1
p = 0 
while i<n:
    if i%2!=0:
        i += 1
    else:
        p = (p+i)*1
        i += 1
print(p)
    
        