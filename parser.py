
from ftplib import FTP
from dateutil import parser
import os
from time import sleep
ftp = FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()
ftp.cwd('pubmed/updatefiles')

gz = [x for x in ftp.nlst() if x.endswith('.gz')]

for index, all in enumerate(gz):
    timestamp = ftp.voidcmd(f"MDTM {all}")[4:].strip()
    hour = str(parser.parse(timestamp))
    dae = hour.split()
    print(f"{index} {all} {dae[0]} {dae[1]}")

num = int(input("Select a start-point? "))
end = int(input("Select an ed-point? "))
if num == int(num):
    if end == int(end):
        newgz = gz[num:end+1]
#        with open('results.txt', 'w') as wb:
        for x in newgz:
               # wb.write(f"{are}\n")
            with open(f'gz/{x}', 'wb') as fp:
                ftp.retrbinary(f'RETR {x}', fp.write)
#        wb.close()
ftp.quit()
sleep(2)
os.chdir('gz')
os.system('gzip -d *.gz*')
job = "for i in $(dir); do $(grep 'ArticleId IdType=\"doi\"' $i | awk -F\">\" '{print $2}' | awk -F\"<\" '{print $1}' > $(basename -s .xml $i).txt); done"
os.system(job)
os.system('rm -rf *.xml*')
