# Python-photo_downloader
## 下載運動筆記中相簿的照片

專題目標：
* 使用webdriver讓網頁自動捲動
* 取得img標籤中的src
* 自動下載照片並存到指定資料夾

(以台北馬拉松-終點前約300公尺(市府路)為練習相簿)

---
1. 解析網頁，發現圖片都在class"photo_img photo-img"的img標籤中
```
<img class="photo_img photo_img" src="http://cdntwrunning.biji.co/XXX.jpg"...
```

2. 使用selenium模組的webdriver來開啟chrome瀏覽器，並使用JS語法來達到自動往下捲動的效果
```
 driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
 ```

 3. 指定儲存資料夾，若資料夾不存在就新建一個資料夾
 ```
 imgs_dir = 'E:\\temp\\' + title
if not os.path.exists(imgs_dir):
    os.mkdir(imgs_dir)
```

4. 以urlopen來開啟圖檔，print出來後發現是二進制格式，所以要透過'wb'方式來覆寫
```
try:
    #以urlopen讀取圖檔
    image = urlopen(img_path)
    #print 出來發現是二進制的型態，所以要用'wb'覆寫
    # print(image.read())
    #透過with open建立圖檔路徑及檔名 
    with open(os.path.join(imgs_dir,filename),wb') as f:
        #再以write方法儲存圖檔                
        f.write(image.read())
        n+=1
        # if n >=50: #測試用，設定最多下載50張
        break
    #除了把哪一張照片無法讀取print出來外，exception print出來方便知道錯誤訊息
except Exception as e:
    print("{} 無法讀取！".format(filename),e)
            
```
