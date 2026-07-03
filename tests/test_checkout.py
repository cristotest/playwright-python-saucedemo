import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage


@pytest.mark.regression
class TestCheckout:
    """Tests para la funcionalidad de Checkout"""
    
    def test_start_checkout_button(self, page):
        """TC006: Ingresar a checkout desde el carrito"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.go_to_cart()
        
        cart_page = CartPage(page)
        cart_page.go_to_checkout()
        
        assert "/checkout-step-one.html" in page.url
        print("Ingreso a checkout desde el carrito funciona correctamente")
    
    @pytest.mark.smoke
    def test_checkout_with_valid_data(self, page):
        """TC007: Checkout con datos válidos"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.go_to_cart()
        
        cart_page = CartPage(page)
        cart_page.go_to_checkout()
        
        checkout_page = CheckoutPage(page)
        checkout_page.fill_information("Juan", "Perez", "1234")
        checkout_page.click_continue()
        
        assert "/checkout-step-two.html" in page.url
    
    def test_checkout_without_data(self, page):
        """TC008: Checkout sin datos"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.go_to_cart()
        
        cart_page = CartPage(page)
        cart_page.go_to_checkout()
        
        checkout_page = CheckoutPage(page)
        checkout_page.click_continue()
        
        # Debe quedarse en step-one porque faltan datos
        assert "/checkout-step-one.html" in page.url
        print("Validación sin datos funciona correctamente")
    
    def test_validate_checkout_overview(self, page):
        """TC009: Overview de Compra - Cálculo de totales"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.go_to_cart()
        
        cart_page = CartPage(page)
        cart_page.go_to_checkout()
        
        checkout_page = CheckoutPage(page)
        checkout_page.fill_information("Juan", "Perez", "1234")
        checkout_page.click_continue()
        
        item_total = checkout_page.get_item_total()
        tax = checkout_page.get_tax()
        total = checkout_page.get_total()
        
        # Extract only the numeric part
        item_amount = float(item_total.split("$")[1])
        tax_amount = float(tax.split("$")[1])
        total_amount = float(total.split("$")[1])
        
        expected_total = round(item_amount + tax_amount, 2)
        assert total_amount == expected_total
        print(f"Cálculo correcto - Total: ${total_amount}")
    
    @pytest.mark.smoke
    def test_complete_purchase(self, page):
        """TC010: Completar compra exitosa"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.go_to_cart()
        
        cart_page = CartPage(page)
        cart_page.go_to_checkout()
        
        checkout_page = CheckoutPage(page)
        checkout_page.fill_information("Juan", "Perez", "1234")
        checkout_page.click_continue()
        checkout_page.click_finish()
        
        confirmation_page = ConfirmationPage(page)
        assert confirmation_page.is_order_complete()
    
    def test_continue_shopping_from_cart(self, page):
        """TC012: Volver de Carrito a Productos"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        
        products_page.go_to_cart()
        cart_page = CartPage(page)
        initial_count = cart_page.get_cart_items_count()
        
        cart_page.continue_shopping()
        assert "/inventory.html" in page.url
        
        products_page.go_to_cart()
        final_count = cart_page.get_cart_items_count()
        
        assert initial_count == final_count
        assert final_count == 2
        print(f"Continuar compra funciona - {final_count} productos mantenidos")