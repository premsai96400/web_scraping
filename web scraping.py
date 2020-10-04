from bs4 import BeautifulSoup as bs
import requests
import pickle

r = requests.get('https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P')
page = r.text
soup=bs(page,'html.parser')
res=soup.find_all('a',{'class':'pl-video-title-link'})
print(res)
kiran = []
w = []
names=[]
for l in res:
     a = l.get('href')
     kiran.append(a)
for i in range(len(kiran)):
    k = ('https://www.youtube.com'+kiran[i])
    w.append(k)
for i in range(len(w)):
    k = requests.get(w[i])
    sai = k.text
    sp = bs(sai,'html.parser')
    kl= sp.find("meta",property ="og:title" )
    #print (kl.get("content", None))
    names.append(kl.get("content", None))
with open('mom.txt','wb') as f:
    pickle.dump(names,f)