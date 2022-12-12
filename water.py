from bs4 import BeautifulSoup
import requests

#搜尋目標位址
url = "https://water.taiwanstat.com/"
#向位址提出請求
web = requests.get("https://water.taiwanstat.com/")

if web.status_code == 200:
    print("取得網頁內容成功") 
       
    soup = BeautifulSoup(web.text, "lxml")
    
    tag = soup.find_all("h3")
    
    for row in tag:
        print(row.get_text("\n", strip=True))
        print("rebase")
    
            
else:
    print("取得網頁內容失敗")  
