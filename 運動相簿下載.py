import time,os
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen


driver = webdriver.Chrome()
url = 'https://running.biji.co/index.php?q=album&act=photo_list&album_id=41002&cid=7330&start=1576371000&end=1576371600&type=place&subtitle=%E5%8F%B0%E5%8C%97%E9%A6%AC%E6%8B%89%E6%9D%BE-%E7%B5%82%E9%BB%9E%E5%89%8D%E7%B4%84300%E5%85%AC%E5%B0%BA%28%E5%B8%82%E5%BA%9C%E8%B7%AF%29+%2833%2C060%29'

driver.get(url)

#隱性等待一秒
driver.implicitly_wait(1)
soup = BeautifulSoup(driver.page_source,'html.parser')
#取得相簿標題  strip()方法可以用來移除字串頭尾符號，預設為空格或換行符號
title = soup.select('.album-title')[0].text.strip()

for i in range(1):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)



#取得img src內容(即為圖片來源)
all_imgs = soup.find_all('img',{"class":"photo_img photo-img"})

#指定儲存位置
imgs_dir = 'E:\\temp\\' + title
if not os.path.exists(imgs_dir):
    os.mkdir(imgs_dir)

n=0
for img in all_imgs:
    #讀取src內容
    src = img.get('src')
    #讀取.jpg檔
    if src != None and ('.jpg' in src):
        img_path = src
        #取得圖檔名 用split方法拆開src / 後面的字串作為檔名(每張圖的src差別處)
        filename = img_path.split('/')[-1]
        print(img_path)

        #透過try & except 來捕捉錯誤，避免沒有權限或其他原因發生錯誤而程式中斷
        try:
            #以urlopen讀取圖檔
            image = urlopen(img_path)
            #print 出來發現是二進制的型態，所以要用wb覆寫
            # print(image.read())
            #透過open建立圖檔路徑及檔名 
            with open(os.path.join(imgs_dir,filename),'wb') as f:
                #再以write方法儲存圖檔                
                f.write(image.read())
            n+=1
            # if n >=10: #最多下載50張
            break
        
        except Exception as e:
            print("{} 無法讀取！".format(filename),e)
            
print("共下載",n,"張圖片")
driver.quit() #關閉瀏覽器並退出驅動程式
    