from page.page import page_data

def login(driver,username,password):
    driver.element_by_id(page_data['username']).send_keys(username)
    driver.element_by_id(page_data['password']).send_keys(password)
    driver.element_by_class_name(page_data['login']).click()

