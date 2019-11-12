import requests
import json
from pprint import pprint

ans={}
#f=open("failed.txt","r")
f=open("new_headings.txt","r")
failed=""
urls=f.read().splitlines()
end_point="http://127.0.0.1:1234/api"
count=0
for url in urls:
    count+=1
    if count<0:
        continue
    try:
        r=requests.get(end_point,data=url,timeout=160)
        print("Request completed")
        if r.status_code!=200:
            print("Error at:"+url)
            failed+=url+"\n"
        else:
            temp = url[url.find("10603") + 6:]
            number = temp[:temp.find("/")]
            ans[number]=(r.content).decode('utf-8')
            print(r.content)
            #break
    except:
        continue

f=open("processed.json","w")
f.write(json.dumps(ans))
f.close()

f=open("failed.txt","w")
f.write(failed)
f.close()
