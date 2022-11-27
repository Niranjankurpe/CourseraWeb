import time

from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver


    # enter on search bar
    # driver.find_element(By.XPATH, "//input[@placeholder='What do you want to learn?']").send_keys("web development")
    sendkay = (By.XPATH, "//input[@placeholder='What do you want to learn?']")
    def sendname(self):
        return self.driver.find_element(*HomePage.sendkay)

    # select web development option
    # driver.find_element(By.XPATH, "//span[normalize-space()='web development']").click()
    select = (By.XPATH, "//span[normalize-space()='web development']")
    def clickWD(self):
        return self.driver.find_element(*HomePage.select)


    # click on Begginer
    # driver.find_element(By.XPATH, "//span[contains(text(),'Beginner')]").click()
    Begginer = (By.XPATH, "//span[contains(text(),'Beginner')]")
    def clickBginer(self):
        return self.driver.find_element(*HomePage.Begginer)


    # click on "show more " language
    # driver.find_element(By.XPATH, "(//span[@class='cds-2 cds-button-label'])[11]").click()
    showmore = (By.XPATH, "(//span[contains(text(),'Show more')])[4]")
    def clickshowm(self):
        return self.driver.find_element(*HomePage.showmore)


    # click on english language
    # driver.find_element(By.XPATH, "//span[contains(text(),'English')]").click()
    language = (By.XPATH, "//span[contains(text(),'English')]")
    def clickeng(self):
        return self.driver.find_element(*HomePage.language)


    # click on apply
    # driver.find_element(By.XPATH, "//span[normalize-space()='Apply']").click()
    apply = (By.XPATH, "//span[normalize-space()='Apply']")
    def clickApply(self):
        return self.driver.find_element(*HomePage.apply)


    # show 1st course info
    # firstcourse = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Meta Front-End Developer professional certificate by [object Object]'] div[class='css-ilhc4l']").text
    # print(firstcourse)
    firstcourse = (By.XPATH, "(//div[@class='css-ilhc4l'])[1]")
    def clickfirst(self):
        return self.driver.find_element(*HomePage.firstcourse)


    # show 2nd course info
    # secondcourse = driver.find_element(By.CSS_SELECTOR, "a[aria-label='IBM Full Stack Software Developer professional certificate by [object Object]'] div[class='css-ilhc4l']").text
    # print(secondcourse)
    secondcourse = (By.XPATH, "(//div[@class='css-ilhc4l'])[2]")
    def clicksecond(self):
        return self.driver.find_element(*HomePage.secondcourse)


    #assertion Done for first 2 course name

    First = (By.XPATH, "//h2[normalize-space()='Meta Front-End Developer']")
    def clickfirstast(self):
        return self.driver.find_element(*HomePage.First)

    secend = (By.XPATH, "//h2[normalize-space()='IBM Full Stack Software Developer']")
    def clicknd(self):
        return self.driver.find_element(*HomePage.secend)

