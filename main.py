from selenium.webdriver.support.expected_conditions import presence_of_element_located
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from locators import Locators

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.Locators = Locators
        #PRUEBA 1
    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(Locators.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(Locators.to_field)).send_keys(to_address)
    def get_from(self):
        return self.driver.find_element(*Locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*Locators.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.request_taxi_button))

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

      #PRUEBA 2
    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.comfort_rate_icon))

    def click_on_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()

        assert presence_of_element_located(Locators.comfort_rate_icon)

       #PRUEBA 3
    def get_phone_number_text(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
        Locators.phone_number_text))

    def click_on_phone_number_text(self):
        self.get_phone_number_text().click()

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
        Locators.phone_number_field))

    def set_phone_number_field(self, phone):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
        Locators.phone_number_field)).send_keys(phone)

    def get_next_button_phone(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
        Locators.next_button_phone))

    def click_next_button_phone(self):
        self.get_next_button_phone().click()

    def get_message_code_input(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
        Locators.message_code_input))

    def click_on_message_code_input(self):
        self.get_message_code_input().click()

    def set_send_code(self, code):
        self.get_message_code_input().send_keys(code)

    def get_next_button_message_code(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
        Locators.next_button_message_code))

    def click_on_next_button_message_code(self):
        self.get_next_button_message_code().click()

        #PRUEBA 4
    def get_payment_method(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.payment_method))

    def click_on_payment_method(self):
        self.get_payment_method().click()

    def get_add_credit_card(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.add_credit_card_icon))

    def click_on_add_credit_card(self):
        self.get_add_credit_card().click()

    def get_card_number_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.card_number_field))

    def click_card_number_text(self):
        self.get_card_number_field().click()

    def set_card_number(self,nc):
        self.get_card_number_field().send_keys(nc)

    def tab_card_number_field(self):
        self.get_card_number_field().send_keys(Keys.TAB)

    def get_card_code(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.card_code_field))

    def click_on_card_code_field(self):
        self.get_card_code().click()

    def set_card_code(self,cc):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.card_code_field)).send_keys(cc)

    def tab_card_cvv_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(Locators.card_code_field)).send_keys(Keys.TAB)

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.add_card_button))

    def click_on_add_card_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.add_card_button)).click()

    def get_close_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.close_button))

    def click_close_button(self):
        self.get_close_button().click()

        #PRUEBA 5
    def get_comment_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(Locators.comment_field))

    def click_on_comment_field(self):
        self.get_comment_field().click()

    def get_comment_driver_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(Locators.comment_driver_field))

    def set_comment_driver_field(self, comment):
        self.get_comment_driver_field().send_keys(comment)

    def get_error_text(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(Locators.error_text))

      #PRUEBA 6
    def get_arrow_reqs(self):
        return WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(Locators.arrow_reqs))

    def click_on_arrow_reqs(self):
        self.get_arrow_reqs().click()
        self.get_arrow_reqs().click()

    def get_slider_span(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(Locators.slider_mantas))

    def click_on_slider_span(self):
        self.get_slider_span().click()

        #PRUEBA 7
    def get_ice_cream_plus_icon(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(Locators.ice_cream_plus))

    def click_on_ice_cream_plus_icon(self):
        self.get_ice_cream_plus_icon().click()

    def get_ice_cream_counter_2(self):
        return WebDriverWait(self.driver,3).until(
            EC.visibility_of_element_located(Locators.ice_cream_counter)).text

    #PRUEBA 8

    def get_order_taxi(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(Locators.order_taxi_button))

    def click_order_taxi_button(self):
        self.get_order_taxi().click()

    def get_modal_search_taxi(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.search_taxi)).text

    #PRUEBA 9
    def wait_driver_details(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(Locators.driver_details)).text



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_icon()

        comfort_rate = routes_page.get_comfort_rate_icon().text
        comfort_text = 'Comfort'

        assert comfort_rate in comfort_text

    def test_phone_number(self):
        self.test_select_comfort_rate()
        routes_page = UrbanRoutesPage(self.driver)
        phone = data.phone_number
        routes_page.click_on_phone_number_text()
        routes_page.set_phone_number_field(phone)
        routes_page.click_next_button_phone()
        assert presence_of_element_located(Locators.phone_number_field)

    def test_phone_code_confirmation(self):
        self.test_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        code = retrieve_phone_code(self.driver)
        routes_page.set_send_code(code)
        routes_page.click_on_next_button_message_code()

        assert presence_of_element_located(Locators.message_code_input)

    def test_add_card_in_payment_method(self):
        self.test_phone_code_confirmation()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_payment_method()
        routes_page.click_on_add_credit_card()
        number_card = data.card_number
        cvv = data.code_number
        routes_page.click_card_number_text()
        routes_page.set_card_number(number_card)
        routes_page.click_on_card_code_field()
        routes_page.set_card_code(cvv)
        routes_page.tab_card_cvv_field()
        assert presence_of_element_located(Locators.add_card_button)
        routes_page.click_on_add_card_button()
        assert presence_of_element_located(Locators.close_button)
        routes_page.click_close_button()

    def test_comment_driver(self):
        self.test_add_card_in_payment_method()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_comment_field()
        comment = data.message_for_driver
        routes_page.set_comment_driver_field(comment)
        assert presence_of_element_located(Locators.error_text)

    def test_slider_manta(self):
        self.test_comment_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_arrow_reqs()
        routes_page.click_on_slider_span()
        slider_before = Locators.slider_mantas_before
        assert presence_of_element_located(slider_before)

    def test_ice_cream_plus_icon(self):
        self.test_slider_manta()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_ice_cream_plus_icon()
        routes_page.click_on_ice_cream_plus_icon()
        assert routes_page.get_ice_cream_counter_2() == '2'

    def test_modal_search_taxi(self):
        self.test_ice_cream_plus_icon()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi_button()
        routes_page.get_modal_search_taxi()
        text = 'Buscar automóvil'

        assert text in routes_page.get_modal_search_taxi()

    def test_driver_details(self):
        self.test_modal_search_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(22)
        routes_page.wait_driver_details()
        details = 'El conductor llegará en'

        assert details in routes_page.wait_driver_details()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()