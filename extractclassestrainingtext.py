# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 23:58:14 2015

@author: nausheenfatma
"""

from readproperties import read_property

f=open(read_property('trainingfilepath'),"r")
fi_1=open(read_property('FineInputFiles')+'LOC_training.txt',"w")
fi_2=open(read_property('FineInputFiles')+'HUM_training.txt',"w")
fi_3=open(read_property('FineInputFiles')+'NUM_training.txt',"w")
fi_4=open(read_property('FineInputFiles')+'ABBR_training.txt',"w")
fi_5=open(read_property('FineInputFiles')+'ENTY_training.txt',"w")
fi_6=open(read_property('FineInputFiles')+'DESC_training.txt',"w")
classes=[]
lines=f.readlines()
f.close()
i=0
for line in lines:
    i=i+1
    line=line.rstrip('\n')
    if not (line=="\n"):
        classes.append((line.split()[0]).split(":")[0])
        label=(line.split()[0]).split(":")[0]
        if label=="LOC":
            fi_1.write(str(i)+" ")
            fi_1.write(line+"\n")
            print line
        if label=="HUM":
            fi_2.write(str(i)+" ")
            fi_2.write(line+"\n")
            print line
        if label=="NUM":
            fi_3.write(str(i)+" ")
            fi_3.write(line+"\n")
            print line
        if label=="ABBR":
            fi_4.write(str(i)+" ")
            fi_4.write(line+"\n")
            print line
        if label=="ENTY":
            fi_5.write(str(i)+" ")
            fi_5.write(line+"\n")
            print line
        if label=="DESC":
            fi_6.write(str(i)+" ")
            fi_6.write(line+"\n")
            print line
            
fi_1.close()
fi_2.close()
fi_3.close()
fi_4.close()
fi_5.close()
fi_6.close()
#print set(classes)
