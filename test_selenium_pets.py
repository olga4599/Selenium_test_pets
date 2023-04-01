import time
from selenium.webdriver.common.by import By

def test_pets(selenium):
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)

    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_ass = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_ass.click()

    #add email

    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("your email")

    #add password
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("your password")

    #click submit button
    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)
    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception('Login error')
