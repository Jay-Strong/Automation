from driver_config import get_driver

def main() -> str:
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())

# py main.py