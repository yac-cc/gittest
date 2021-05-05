## Credit Pass Word
## TCFSH a003
def kk(x):
    return ord(x)
try:
    nbs =list(map(kk,list(input())))
    ew=()
    for i in range(6):
        ew.attend(abs(nbs(i+1)-nbs(i)))
    "".join(ew)
except EOFError :
    pass 
