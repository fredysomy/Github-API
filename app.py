from flask import  Flask
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import html5lib
app=Flask(__name__)

@app.route("/")
def hello():
    return "hello world"
@app.route("/repo/<id>")
def hh(id):
    urll="https://github.com/"+id+"?tab=repositories"
    r=requests.get(urll)
    soup=BeautifulSoup(r.content,'html5lib')
    a=soup.find(id="user-repositories-list")
    z=a.find_all('li')
    yo={}
    er=[]
    
    for i in range(0,len(z)):
        s=z[i]
        
        try:
            y=s.find('a')
            x=y['href']
            try:
                ur=[]
                sds=s.find('a',class_="muted-link mr-3").getText()
                

                j=s.find('p').getText()
                name=y.getText()
                url="https://github.com"+x
                k={'name':name.strip(),'description':j.strip(),'url':url,"stars":sds.strip()}
                er=er+[k]
            except:
                ur=[]
                h=y.getText()
                y="https://github.com"+x
                k={'name': h.strip(),'url':y,"stars":sds.strip()}
                er=er+[k]
            
        except:
            print("none")
        
    return jsonify(er)
        
    
if __name__ == "__main__":
    app.run()

