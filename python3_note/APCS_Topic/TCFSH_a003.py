## Credit Pass Word
## TCFSH a003
def kk(x):
    return ord(x)
try:
    while True :
        nbs =list(map(kk,list(input())))
        ew=''
        for i in range(6):
            k=abs(nbs[i+1]-nbs[i])
            ew=ew + str(k)
        print(ew)
except EOFError :
    pass 
