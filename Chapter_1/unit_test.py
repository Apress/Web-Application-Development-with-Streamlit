from main import calculate_sum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_user_interface():
    driver_path = r"----------\chromedriver.exe"  # Path to chromedriver. Can end with .sh if on (Li/U)nix environments
    options = Options()
    options.add_argument("--headless")  # To not open a real chrome window
    with webdriver.Chrome(driver_path, chrome_options=options) as driver:
        url = "http://127.0.0.1:8501"
        driver.get(url)
        time.sleep(5)
        html = driver.page_source

    assert "Add numbers" in html
    assert "First Number" in html
    assert "Second Number" in html


def test_logic():
    assert calculate_sum(1, 1) == 2
    assert calculate_sum(1, -1) == 0
    assert calculate_sum(1, 9) == 10


if __name__ == "__main__":
    test_logic()
    test_user_interface()
