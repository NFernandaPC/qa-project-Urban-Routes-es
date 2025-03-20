from selenium.webdriver.common.by import By

class Locators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
#prueba 2
    request_taxi_button = (By.CSS_SELECTOR, "button.round")
    comfort_rate_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
#prueba 3
    phone_number_text = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    next_button_phone = (By.XPATH, "//button[@type='submit' and @class='button full' and text()='Siguiente']")
    message_code_input = (By.XPATH, "//input[@id='code']")
    next_button_message_code = (By.XPATH, "//button[@ type='submit' and @class='button full' and text ()='Confirmar']")
#prueba 4
    payment_method = (By.CSS_SELECTOR, "div.pp-button.filled")
    add_credit_card_icon = (By.CSS_SELECTOR, "img.pp-plus")
    card_number_field = (By.ID, 'number')
    card_code_field= (By.XPATH, "//input[@type= 'text' and @name= 'code']")
    add_card_button = (By.XPATH, "//button[@type and text()= 'Agregar']")
    close_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
#prueba 5
    comment_field = (By.XPATH, "//label[@for='comment' and text()='Mensaje para el conductor...']")
    comment_driver_field = (By.ID, 'comment' )
    error_text = (By.XPATH, "//div[@class='error' and tex()= 'Longitud máxima 24']")
#prueba 6
    arrow_reqs = (By.CLASS_NAME, "reqs-arrow")
    slider_mantas = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    slider_mantas_before = (By.XPATH, "//div[@class='switch']/span[@class='slider round']")
#prueba 7
    ice_cream_plus = (By.XPATH, "//html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
    ice_cream_counter = (By.XPATH, "//div[@class='counter-value' and text()='2']")
#prueba 8
    order_taxi_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[4]/button")
    search_taxi = (By.CLASS_NAME, "order-header-content")
    driver_details = (By.CLASS_NAME, "order-header-title")

