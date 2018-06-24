import numpy as np
xc=open('black.srt','r')
xd = open('new_srt.srt', 'w')
xc1=xc.read()

xc3=xc1.split('\n')



j=0
xc5=[]
while(j<len(xc3)):
    if(xc3[j].find('-->')>0):
        xc5.append(xc3[j])
    j=j+1
import pandas as pd
xc5=pd.Series(xc5)
c6=[]
for i in range(len(xc5)):
    c6.append(xc5[i].split(' --> '))
c7=np.zeros((len(c6),2))
for i in range(len(c7)):
    for j in range(2):
        c7[i][j]=float((c6[i][j].split(':')[2]).replace(",",""))

np.savetxt( xd, c7)
# print c7
# xd.write(list(c7))
# print c7