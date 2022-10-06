# Badminton Autobrooking System
>reference : 
>[tutorial](https://tonidata.medium.com/%E8%87%AA%E5%8B%95%E6%90%B6%E7%A5%A8%E7%A8%8B%E5%BC%8F-%E7%94%A8python%E6%90%B6%E7%86%B1%E8%B3%A3%E5%95%86%E5%93%81-1f542f50c395)、[XPATH](https://www.guru99.com/xpath-selenium.html)、[multithreading](https://www.maxlist.xyz/2020/03/15/python-threading/)、[selenium](https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html)
## Pre-setting

- [Chromedriver 要與電腦的 Chrome 版本相同](https://chromedriver.chromium.org/downloads)

## 流程
1. 設定日期、時段、幾個場 (可能有預約限制?)
2. 晚上 11:59 執行程式並 reload 網頁
3. 開始搶 .... (搶場演算法，如何連搶兩個場)
4. 搶到後回報搶到的場
5. 之後手動取消不要的場

