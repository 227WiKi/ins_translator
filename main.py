import os
from pathlib import *

filename=[]
outlist=[]
member=["kanae","sally","moe","uta","mao","rino","satsuki"]
kanae_pic=["https://files.227wiki.eu.org/d/Backup/Instagram/__shiro227/2022-07-19_14-22-01_UTC_1.jpg","https://files.227wiki.eu.org/d/Backup/Instagram/__shiro227/2021-10-23_12-00-35_UTC.jpg"]
sally_pic=["https://files.227wiki.eu.org/d/Backup/Instagram/sallyamaki/2023-05-29_04-01-46_UTC.jpg","https://files.227wiki.eu.org/d/Backup/Instagram/sallyamaki/2023-03-22_07-23-26_UTC_1.jpg"]
moe_pic=["https://files.227wiki.eu.org/d/Backup/Instagram/moepiyo227/2023-02-24_14-47-10_UTC.jpg","https://files.227wiki.eu.org/d/Backup/Instagram/moepiyo227/2023-07-14_13-36-32_UTC.jpg"]
uta_pic=["https://files.227wiki.eu.org/d/Backup/Instagram/kawase_uta/2022-03-07_07-16-26_UTC_3.jpg","https://files.227wiki.eu.org/d/Backup/Instagram/kawase_uta/2022-08-23_10-18-31_UTC_2.jpg"]
mao_pic=["https://files.227wiki.eu.org/d/Backup/Instagram/asaoka_mao__/2023-08-27_11-02-11_UTC_7.jpg","https://files.227wiki.eu.org/d/Backup/Instagram/asaoka_mao__/2023-10-31_08-47-24_UTC_4.jpg"]
rino_pic=["https://files.227wiki.eu.org/d/Backup/Instagram/cure_rinochi/2023-09-16_12-37-57_UTC_1.jpg","https://files.227wiki.eu.org/d/Backup/Instagram/cure_rinochi/2023-08-12_10-27-08_UTC_2.jpg"]
satsuki_pic=["https://files.227wiki.eu.org/d/Backup/Instagram/shiina_satsuki227/2023-11-11_15-08-28_UTC_1.jpg","https://files.227wiki.eu.org/d/Backup/Instagram/shiina_satsuki227/2023-04-13_04-40-16_UTC_1.jpg"]
def cname(i):
    if i == "kanae":
        return "__shiro227"
    if i == "sally":
        return "sallyamaki"
    if i == "moe":
        return "moepiyo227"
    if i == "uta":
        return "kawase_uta"
    if i == "mao":
        return "asaoka_mao__"
    if i == "rino":
        return "cure_rinochi"
    if i == "satsuki":
        return "shiina_satsuki227"
def head(i):
    if i == "kanae":
        return "  cover: "+kanae_pic[0]+"\n  top_background: "+kanae_pic[1]+"\n  description: 白泽加奈惠\n"
    if i == "sally":
        return "  cover: "+sally_pic[0]+"\n  top_background: "+sally_pic[1]+"\n  description: 天城莎莉\n"
    if i == "moe":
        return "  cover: "+moe_pic[0]+"\n  top_background: "+moe_pic[1]+"\n  description: 凉花萌\n"
    if i == "uta":
        return "  cover: "+uta_pic[0]+"\n  top_background: "+uta_pic[1]+"\n  description: 河瀬詩\n"
    if i == "mao":
        return "  cover: "+mao_pic[0]+"\n  top_background: "+mao_pic[1]+"\n  description: 麻丘真央\n"
    if i == "rino":
        return "  cover: "+rino_pic[0]+"\n  top_background: "+rino_pic[1]+"\n  description: 望月りの\n"
    if i == "satsuki":
        return "  cover: "+satsuki_pic[0]+"\n  top_background: "+satsuki_pic[1]+"\n  description: 椎名桜月\n"
def checkfile(f):
    global filename
    filename=[]
    for i in f:
        if os.path.splitext(i)[1]  == '.txt':
            filename.insert(0,os.path.splitext(i)[0])
def write_content():
    for i in filename:
        if Path(rp,i+".jpg").exists():
            with open(Path(Path.cwd(),"album.yml"),"a",encoding='utf-8') as f:
                with open(Path(rp,i+".txt"),"r" ,encoding="utf-8") as t:
                    result = ''
                    for line in t:
                        if line[0]=="@":
                            line=line.replace("@","")
                        if line[0]=="*":
                            line=line.replace("*","")
                        if line[0]=="-":
                            line=line.replace("-","——")
                        line=line.replace(":","：")
                        result += line.strip()
                    f.write("    - content: "+result+"\n      image:\n") 
                    f.write("        - https://files.227wiki.eu.org/d/Backup/Instagram/"+path+"/"+i+".jpg\n")
                    f.write("      date: "+i[0:10]+"\n")
                    f.write("      from: Instagram\n")
                    
        else:
            with open(Path(Path.cwd(),"album.yml"),"a",encoding='utf-8') as f:
                with open(Path(rp,i+".txt"),"r" ,encoding="utf-8") as t:
                    result = ''
                    for line in t:
                        if line[0]=="@":
                            line=line.replace("@","")
                        if line[0]=="*":
                            line=line.replace("*","")
                        if line[0]=="-":
                            line=line.replace("-","——")
                        line=line.replace(":","：")
                        result += line.strip()
                    f.write("    - content: "+result+"\n      image:\n") 
                for j in range(1,10):
                    fn=i+"_"+str(j)+".jpg"
                    if Path(rp,fn).exists(): 
                        f.write("        - https://files.227wiki.eu.org/d/Backup/Instagram/"+path+"/"+fn+"\n")
                f.write("      date: "+i[0:10]+"\n")
                f.write("      from: Instagram\n")
if __name__ == "__main__":
    with open(Path(Path.cwd(),"album.yml"),"w",encoding='utf-8') as f: 
        f.seek(0)
        f.write("")
    for i in member:
        path = cname(i)
        rp=Path(Path.cwd(),path)
        file_list = os.listdir(path)
        checkfile(file_list)
        with open(Path(Path.cwd(),"album.yml"),"a",encoding='utf-8') as j:
            j.write("- path_name: /"+path+"/\n")
            j.write(head(i))
            j.write("  type: 1\n")
            j.write("  lazyload: true\n")
            j.write("  btnLazyload: false\n")
            j.write("  url: false\n")
            j.write("  top_link: /ins\n")
            j.write("  top_btn_text: 返回\n")
            j.write("  class_name: Instagram\n")
            j.write("  album_list:\n")
        write_content()




  



        

        
                    