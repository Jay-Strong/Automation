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

def main() -> str:
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())

# py scrape_text_with_selenium.py