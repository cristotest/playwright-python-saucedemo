import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage


@pytest.mark.e2e
@pytest.mark.smoke
class TestE2E:
    """End-to-End Tests - Flujo completo de compra en SauceDemo"""
    
    def test_complete_purchase_flow(self, page):
        """TC011: Completar flujo de compra exitoso desde login hasta confirmación"""
        # Login
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Agregar productos al carrito
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        
        # Ir a carrito y validar cantidad de productos
        products_page.go_to_cart()
        cart_page = CartPage(page)
        assert cart_page.get_cart_items_count() == 2
        
        # Checkout
        cart_page.go_to_checkout()
        checkout_page = CheckoutPage(page)
        checkout_page.fill_information("Cristopher", "Diaz", "66055")
        checkout_page.click_continue()
        checkout_page.click_finish()
        
        # Validar confirmación de compra
        confirmation_page = ConfirmationPage(page)
        assert confirmation_page.is_order_complete()
        print("Flujo E2E completo exitoso")