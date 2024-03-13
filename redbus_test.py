from method import RedBusHomePage

def test_calendar(month,year):
    redbus_home = RedBusHomePage(month , year)
    redbus_home.open_calendar()

    while True:
        current_month, current_year, holidays = redbus_home.get_month_year_and_holidays()
        if current_month == month and current_year == year:
            print(current_month, current_year)
            print(holidays)
            dates = redbus_home.get_weekend_dates()
            print(dates)
            break
        else:
            print(current_month, current_year)
            print(holidays)
            print("----------")
            redbus_home.navigate_to_next_month()


if __name__ == "__main__":
    test_calendar("Jul", "2025")
