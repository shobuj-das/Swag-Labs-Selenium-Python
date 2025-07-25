from tkinter.tix import Select

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class Inventory(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    # ---- inventory page locators
    product_1_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_button = (By.CLASS_NAME, "shopping_cart_link")
    product_name = "Sauce Labs Fleece Jacket"
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name ")
    add_to_cart_xpath = "(//button[@class='btn btn_primary btn_small btn_inventory '])"
    product_sort_locator = (By.CLASS_NAME, "product_sort_container")
    inventory_item_price = (By.XPATH, "//div[@class='inventory_item_price']")
    inventory_item = (By.CLASS_NAME, "inventory_item")

    def sort_by_value(self, value):
        select = Select(self.get_element(self.product_sort_locator))
        select.select_by_value(value)

    def sort_price_low_to_high(self):
        self.sort_by_value("lohi")

    def get_price_list(self):
        price_list = []
        price_element = self.get_elements(self.inventory_item_price)
        for price in price_element:
            temp = price.text
            temp = temp.replace("$", "")
            price_list.append(temp)
        return price_list

    def validate_price_low_to_high(self):
        price_list = self.get_price_list()
        print("price(low-high): ", price_list)
        flag = True  # assume the price list is in high to low order
        for i in range(len(price_list) - 1):
            if float(price_list[i]) <= float(price_list[i + 1]):
                continue
            else:
                flag = False
                break
        return flag



    def sort_alpha_a_to_z(self):
        self.sort_by_value("az")

    def get_products_name(self):
        product_name = []
        product_element = self.get_elements(self.inventory_item_name)
        for product in product_element:
            product_name.append(product.text)
        return product_name

    def validate_product_sort_A_to_Z(self):
        product_name = self.get_products_name()
        print("Name(A-Z): ", product_name)
        flag = True  # assuming that products are sorted in a to z
        for i in range(len(product_name) - 1):
            if product_name[i].lower() <= product_name[i + 1].lower():
                continue
            else:
                flag = False
                break

        return flag

    def add_product_to_cart(self, product_list):
        product_element = self.get_elements(self.inventory_item)
        for title in product_list:
            for element in product_element:
                if title == element.find_element(By.CLASS_NAME, "inventory_item_name").text.strip():
                    element.find_element(By.TAG_NAME, "button").click()
                    break

    def validate_cart_badge(self):
        return int(self.get_text(self.cart_badge))