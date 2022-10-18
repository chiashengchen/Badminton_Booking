# Badminton Autobrooking System
>reference : 
>[tutorial](https://tonidata.medium.com/%E8%87%AA%E5%8B%95%E6%90%B6%E7%A5%A8%E7%A8%8B%E5%BC%8F-%E7%94%A8python%E6%90%B6%E7%86%B1%E8%B3%A3%E5%95%86%E5%93%81-1f542f50c395)、[XPATH](https://www.guru99.com/xpath-selenium.html)、[multithreading_1](https://www.maxlist.xyz/2020/03/15/python-threading/)、[multithreading_2](https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/)、[selenium_1](https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html)、[selenium_2](https://ithelp.ithome.com.tw/articles/10230717)、[selenium wait for page load](https://www.lambdatest.com/blog/selenium-wait-for-page-to-load/)
## Pre-setting

- [Chromedriver 要與電腦的 Chrome 版本相同](https://chromedriver.chromium.org/downloads)

## 流程
1. 設定日期、時段、幾個場 (可能有預約限制?)
2. 晚上 11:59 執行程式並 reload 網頁
3. 開始搶 .... (搶場演算法，如何連搶兩個場)
4. 搶到後回報搶到的場
5. 之後手動取消不要的場

## TODO
### Add Sport Center
- 中山、林口、大安

### Error Handle
1. 密碼輸入錯誤
2. 等網頁 load
3. 預定日期沒辦法訂 (日期沒到 or 已額滿)
4. 達到預定限制沒辦法訂
### Multi-thread
1. 多個運動中心同時搶

### 工作排程器

### 驗證碼辨識

## To Improve
1. 現在只能分早上、下午、晚上各自預約，不能跨時段
2. Sports center init 各 state (code 重複利用)
3. Center 增加可讀性 -> 切出 time 跟 info (多對多)
4. ScheduledTime -> Appointment
