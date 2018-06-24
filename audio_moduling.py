xc=open('output.txt','r')
xc1=xc.read()
xc3=xc1.split('\n')
xc4=[]
i=2
xc4.append(xc3[2])
while(i<len(xc3)-3):
    
    if(xc3[i+1]!=''):
        xc4[-1]=(xc4[-1]+xc3[i+1])
        i=i+1
    else:
        i=i+4
        xc4.append(xc3[i])
language='hi'
from gtts import gTTS
 

import os
 
for j in range(len(xc4)):
    mytext=xc4[j]
    
    myobj = gTTS(text=mytext.decode('utf-8'), lang=language, slow=False)
    myobj.save("welcome %i.mp3"% j)
