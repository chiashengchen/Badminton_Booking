from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("--incognito")  
ua = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
opts.add_argument("user-agent={}".format(ua))  
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=opts)
# 使用 selenium開啟瀏覽器
driver.get('http://gs.statcounter.com/detect')  
print("finish")