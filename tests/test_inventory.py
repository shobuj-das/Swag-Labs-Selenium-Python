import pytest

from pages.inventory_page import Inventory
from pages.login_page import LoginPage

@pytest.mark.order(1)
def test_sort_price_high_to_low(driver):
    login_page = LoginPage(driver)
    inventory_page = Inventory(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_price_low_to_high()
    assert inventory_page.validate_price_low_to_high(), "Price not sorted low to high"

@pytest.mark.order(2)
def test_sort_alpha_a_to_z(driver):
    # login_page = LoginPage(driver)
    inventory_page = Inventory(driver)

    # login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_alpha_a_to_z()
    assert inventory_page.validate_product_sort_A_to_Z(), "Product not sorted alphabetically"

@pytest.mark.order(3)
def test_add_item_to_cart(driver):
    inventory_page = Inventory(driver)
    product_name_list =["Sauce Labs Backpack"]

    inventory_page.add_product_to_cart(product_name_list)
    assert inventory_page.validate_cart_badge()== 1, "Item not added to cart"


@pytest.mark.order(4)
def test_add_multiple_item_to_cart(driver):
    inventory_page = Inventory(driver)
    product_name_list = ["Sauce Labs Fleece Jacket",
                         "Sauce Labs Onesie",
                         "Sauce Labs Bike Light",
                         "Test.allTheThings() T-Shirt (Red)"]

    inventory_page.add_product_to_cart(product_name_list)
    assert inventory_page.validate_cart_badge()== 4, "Item not added to cart"