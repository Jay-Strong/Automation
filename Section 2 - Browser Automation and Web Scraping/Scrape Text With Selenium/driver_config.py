from selenium import webdriver as wd

def get_driver() -> wd.Chrome:
    options = wd.ChromeOptions() 
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = wd.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver