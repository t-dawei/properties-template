from selenium import webdriver
 
def spider(url='http://bing.com'):
    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')  
    option.add_argument('--headless')  
    # 注意path，我这里是chromedriver放在/home/apk/chromedriver
    driver = webdriver.Chrome(executable_path=r'D:\chromedriver_win32\chromedriver.exe', options=option)
    driver.get(url)
    print(driver.page_source)
spider()