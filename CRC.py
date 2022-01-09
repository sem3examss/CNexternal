def xor(li1,dli,a,b):
    li2=[]
    for i in range(b):
        if li1[i]==dli[i]:
            li2.append(0)
        else:
            li2.append(1)
    return li2
nli=list(map(int,input("Enter the input:")))
dli=list(map(int,input("Enter the divisor:")))
print("senders data:",nli)
li1=[]
li2=[]
li3=[]
sender=[]
recieve=nli.copy()
for i in range(0,len(dli)-1):
    nli.append(0) 
print("senders data after appending 0's:",nli)
a=len(nli)
b=len(dli)          
li1=nli[0:b]
for i in range(b,a+1):
    if li1[0]==1:
        li1=xor(li1,dli,a,b)
    else:
        li3=[]
        for j in range(b):
            li3.append(0)
        li1=xor(li1,li3,a,b)
    li1=li1[1:]
    if i==a:
        break
    li1.append(nli[i])
for i in range(len(li1)):
    recieve.append(li1[i])
print("Receivers data:",recieve)
