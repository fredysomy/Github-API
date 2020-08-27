from flask import Flask, render_template, redirect, url_for, request, flash
from flask import jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import html5lib
app=Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/")
def hello():
    return render_template('docs.html')
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
@app.route('/user/<id>') 
def st(id):
    urll="https://github.com/"+id
    r=requests.get(urll)
    soup=BeautifulSoup(r.content,'html5lib')
    sdd=soup.find("h1" ,class_="vcard-names pl-2 pl-md-0")
    name=sdd.find_all('span')[0].getText()
    u_name=sdd.find_all('span')[1].getText()
    asd=soup.find(class_="flex-order-1 flex-md-order-none mt-2 mt-md-0")
    dd=asd.find(class_="mb-3")
    followers=dd.find_all('a')[0].find('span').getText().strip(' ')
    following=dd.find_all('a')[1].find('span').getText().strip(' ')
    totstars=dd.find_all('a')[2].find('span').getText().strip(' ')
    asd=soup.find(class_="flex-order-1 flex-md-order-none mt-2 mt-md-0")
    
    
    dsdf=soup.find(class_="avatar avatar-user width-full border bg-white")['src']
    repo_num=soup.find(class_="UnderlineNav-body").find('span',class_="Counter").getText()
    rr=""

    las={'Name':name,'Username':u_name,"ProfilePic":dsdf,'Followers':followers,'Following':following,'Total_stars':totstars,"Total-repos":repo_num}
    return(las)
   

    
if __name__ == "__main__":
    app.run()

