from selenium import webdriver
from selenium.webdriver.common.by import By

class RedBusHomePage:
    def __init__(self,month,year):
        self.month = month
        self.year = year

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.redbus.in/")

    def open_calendar(self):
        self.driver.find_element(By.XPATH, '//div[@class="sc-fjdhpX cvRLz"]').click()

    def get_month_year_and_holidays(self):
        date_year = self.driver.find_element(By.XPATH, '//div[@class="DayNavigator__CalendarHeader-qj8jdz-1 fxvMrr"]')
        ele = date_year.text.split()

        try:
            holidays_in_month = self.driver.find_element(By.XPATH, '//div[@class="holiday_count"]').text
        except:
            holidays_in_month = "0 Holidays"

        if len(ele) == 4:
            ele.pop(0)
            ele.pop(-1)

        elif len(ele) == 5:
            ele.pop(-1)
        elif len(ele) == 6:
            ele.pop(0)
            ele.pop(-1)

        return ele[0], ele[1], holidays_in_month

    def get_weekend_dates(self):
        date_elements = self.driver.find_elements(By.XPATH, '//span[@class="DayTiles__CalendarDaysSpan-sc-1xum02u-1 bwoYtA"]')
        return [date.text for date in date_elements]

    def navigate_to_next_month(self):
        next_month_button = self.driver.find_element(By.XPATH, '//div[@class="DayNavigator__CalendarHeader-qj8jdz-1 fxvMrr"]/div[@class="DayNavigator__IconBlock-qj8jdz-2 iZpveD"][3]')
        next_month_button.click()
