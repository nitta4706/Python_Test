from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# スクレイピング(headless)

def scraping(email, password):
    options = Options()
    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(options=options, executable_path=driver_path)

    driver.get("https://www.xserver.ne.jp/login_info.php")
    driver.implicitly_wait(3)

    try:
        # ログイン
        elem = driver.find_element_by_id("memberid")
        elem.clear()
        elem.send_keys("chm72639")
        elem = driver.find_element_by_id("user_password")
        elem.clear()
        elem.send_keys("btqqzotp")

        elem = driver.find_element_by_id("submit-btn")
        elem.click()
        driver.implicitly_wait(3)

        driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div[1]/table/tbody/tr[2]/td[5]/a[1]').click()
        driver.implicitly_wait(3)

        # wait.until(lambda d: len(driver.window_handles) > 1)
        handle = driver.window_handles
        driver.switch_to.window(handle[1])

        try:
            # メールアカウント設定クリック
            driver.find_element_by_xpath('//*[@id="top_menu"]/div[2]/div[1]/ul/li[1]/a').click()
        except NoSuchElementException:
            driver.switch_to_window(handle[0])
            driver.find_element_by_xpath('//*[@id="top_menu"]/div[2]/div[1]/ul/li[1]/a').click()
            driver.implicitly_wait(3)

        # ドメイン選択画面
        driver.find_element_by_xpath('//*[@id="contents"]/table/tbody/tr[3]/td[3]/a').click()
        driver.implicitly_wait(3)
        # メールアカウント追加クリック
        driver.find_element_by_xpath('//*[@id="tab"]/li[2]/a').click()
        driver.implicitly_wait(3)
        print('Nitta1!')
        elem = driver.find_element_by_name('mail_username_front')
        elem.clear()
        elem.send_keys(email)

        elem = driver.find_element_by_id('mail_password')
        elem.clear()
        elem.send_keys(password)

        elem = driver.find_element_by_name('action_user_mail_add_auth')
        elem.click()
        driver.implicitly_wait(3)
        print('Nitta2!')
        elem = driver.find_element_by_name('action_user_mail_add_do')
        elem.click()
        driver.implicitly_wait(3)
        print('Nitta3')

        my_message = 'OK_Google'

    except Exception:
        error_flg = True
        my_message = 'Error'

    return my_message
