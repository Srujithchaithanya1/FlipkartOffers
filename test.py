from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)





def cal(s1,s2,s3,minp,maxp):
    
    import bs4
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    desired_links=[]
    desired_price=[]
    desired_name=[]
    desired_offer=[]
    df=pd.DataFrame({"Product name":desired_name,"Price":desired_price,"Offer":desired_offer,"Link":desired_links})
    from random import randint
    from time import sleep
    x=[]
    y=[]
    mobile_link='https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=c124cd64-f815-42af-8d91-da7cdf3833a7&as-searchtext=mobiles&page='+str(s3)
    
    page=requests.get(mobile_link)
    bss = BeautifulSoup(page.text,'html.parser')
    possible_links = bss.find_all('a',class_="_1fQZEK")
    possible_prices = bss.find_all('div',class_="_30jeq3 _1_WHN1")
    possible_names = bss.find_all('div',class_="_4rR01T")
    links=[]
    for i in range(len(possible_links)):
        if possible_links[i].has_attr('href'):
            links.append(["http://www.flipkart.com"+possible_links[i].attrs['href'],possible_prices[i].text,possible_names[i].text,possible_links[i]])
    Bank=s1
    C_D=s2
    
    for link in links:

        page=requests.get(link[0])
        soup=BeautifulSoup(page.content,'html.parser')
        bank_offers=soup.find_all('li',class_='_16eBzU col')
        for i in bank_offers:
            if(Bank in i.text and C_D in i.text and int(minp)<=int(link[1][1::].replace(',',''))<=int(maxp)):
                desired_links.append(link[0])
                desired_offer.append(i.text)
                desired_price.append(link[1])
                desired_name.append(link[2])
                # print(link[2],link[1],i.text,link[0],link)
                print('this is link',link[0])
                y.append([link[2],link[1],i.text,link[0]])
        flipkart_offers_csv=df.to_csv('flipkartOffers.csv',index=True)

    sleep(randint(2,10))
    random.shuffle(y)
    return y





@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join',methods=['GET','POST'])
def myform():
    bank=request.form['bank']
    pg=request.form['pg']
    CD=request.form['CD']
    minp=request.form['minp']
    maxp=request.form['maxp']
    op=cal(bank,CD,pg,minp,maxp)
    result={
        "output":op
    }
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)


