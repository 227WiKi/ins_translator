import os
from pathlib import *

name = input("name of the member:")
filename=[]
outlist=[]
def cname(i):
    if i == "kanae":
        return "__shiro227"
    if i == "sally":
        return "sallyamaki"
def checkfile(f):
    global filename
    filename=[]
    for i in f:
        if os.path.splitext(i)[1]  == '.txt':
            filename.insert(0,os.path.splitext(i)[0])
if __name__ == "__main__":
    path = cname(name)
    rp=Path(Path.cwd(),path)
    file_list = os.listdir(path)
    checkfile(file_list)
    for i in filename:
        if Path(rp,i+".jpg").exists():
            with open(Path(Path.cwd(),"album.yml"),"a",encoding='utf-8') as f:
                with open(Path(rp,i+".txt"),"r" ,encoding="utf-8") as t:
                    result = ''
                    for line in t:
                        result += line.strip()
                    f.write("- content: "+result+"\n  image:\n") 
                    f.write("    - https://files.zzzhxxx.top/backup/ins/"+path+"/"+i+".jpg\n")
                    f.write("  date: "+i[0:10]+"\n")
                    f.write("  from: Instagram\n")
                    
        else:
            with open(Path(Path.cwd(),"album.yml"),"a",encoding='utf-8') as f:
                with open(Path(rp,i+".txt"),"r" ,encoding="utf-8") as t:
                    result = ''
                    for line in t:
                        result += line.strip()
                    f.write("- content: "+result+"\n  image:\n") 
                for j in range(1,10):
                    fn=i+"_"+str(j)+".jpg"
                    if Path(rp,fn).exists(): 
                        f.write("    - https://files.zzzhxxx.top/backup/ins/"+path+"/"+fn+"\n")
                f.write("  date: "+i[0:10]+"\n")
                f.write("  from: Instagram\n")
                    