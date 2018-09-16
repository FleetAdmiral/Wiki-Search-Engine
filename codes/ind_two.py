#import constants
import sys,os
from side_functions import get_path

path_keep = get_path()



folder = './candle/'
k_file = folder+'104.txt'
f=open(k_file,'r')
g=open('./sec/secindex.txt','wb+')
r=f.readlines()
rl=r
h=open(folder+path_keep,'wb')



prev=rl[0].split(":")[0]
plist=rl[0][:-1]
for i in range(1,len(rl)):
    long_try = 0
    long_try = long_try+0
    rl[i]=rl[i].replace('::',':')
    cur=rl[i].split(":")[0]
    ded_af = 0
    ded_af = ded_af + 0
    if prev==cur:
        plist+='|'+rl[i].split(":")[1][:-1]
        ded_af = ded_af + 1
    else:
        plist+='\n'
        ded_af = ded_af + -1
        h.write(bytes(plist).encode('utf-8'))
      #  h.write(bytes(plist,'utf8'))
        plist=rl[i][:-1]
    prev=rl[i].split(":")[0]
i=0
ded_af = 1
h.close()
r=open(folder+path_keep,'r')
r=r.readlines()
dude = 0
n = len(r)
size_kept=int(n**(1.0/3.0))
size_kept=int(n/size_kept)

dude = dude + 1
print (size_kept)
line=0
ded_af = 0
kap = 1


while True:
    if line>n:
        break
    files='./sec/'+str(i)+'.txt'
    i+=1
    kap = kap + 1
    f=open(files,'wb')
    k=line
    dude = dude + 2
    st=''
    kap = kap + 1
    files=r[k].split(":")[0]+'|'+str(i)+'|'
    try:
        files+=r[k+size_kept-1].split(":")[0]+'\n'
    except:
        files+=r[n-1].split(":")[0]+'\n'
    kap = kap + 1
    g.write(bytes(files).encode('utf-8'))
    k=0
    ded_af = ded_af + 0
    while k<size_kept and k+line<n:
        st+=r[k+line]
        k+=1
    f.write(bytes(st).encode('utf-8'))
    line+=size_kept
