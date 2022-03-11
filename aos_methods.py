from selenium import webdriver  # import selenium to the file
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(executable_path='../../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# ----------------------------------------------------------
def setUp():
    print(f'Launch {locators.app} App')
    print('--------------------~*~--------------------')
    # Print test start day and time
    print(f'The test Started at: {datetime.datetime.now()}')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Advantage Online Shopping website
    driver.get(locators.aos_url)
    # Check that  URL and the home page title are displayed
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print(f'Yey! {locators.app} was launched Successfully!')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(2)
    else:
        print(f'{locators.app}  did not launch. Check your code for error!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# Create account
def create_user():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'create-new-account').click()
    sleep(2)
    # validate we are on 'Create account'
    assert driver.title == locators.aos_add_user_title
    print(f'Account Details...')
    sleep(.50)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
    sleep(.50)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(.50)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
    sleep(.50)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
    sleep(.50)
    print(f'--- Personal Details...')
    sleep(.50)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.firstname)
    sleep(.50)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.lastname)
    sleep(.50)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(.50)
    print(f'--- Address...')
    sleep(.50)
    # select an options 'Canada'
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(.50)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(.50)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(.50)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(.50)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postcode)
    sleep(.50)
    # check 'I agree'
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(.50)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(1)
    print(
        f'New user with \nUsername:\t{locators.username}\nPassword:\t{locators.password} is registered!')


def logout():
    # validate we are on 'Create account'
    assert driver.title == locators.aos_add_user_title
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label:nth-of-type(3)').click()
    sleep(2)
    # validate logout successful
    if driver.current_url == locators.aos_url:
        print(f'Logout successful at {datetime.datetime.now()}!')


# login to AOS
def login():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(2)
    print(f'Login Form is displayed: {driver.find_element(By.CLASS_NAME, "login").is_displayed()}')
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(2)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)