import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.regression
class TestCart:
    """Tests para la funcionalidad del carrito en SauceDemo"""
    
    @pytest.mark.smoke
    def test_view_cart_with_products(self, page):
        """TC004: Ver carrito con productos agregados"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        products_page.go_to_cart()
        
        cart_page = CartPage(page)
        items_count = cart_page.get_cart_items_count()
        assert items_count == 2
        print("Carrito muestra productos correctamente")
    
    def test_remove_product_from_cart(self, page):
        """TC005: Eliminar producto del carrito"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        products_page.go_to_cart()
        
        cart_page = CartPage(page)
        cart_page.remove_product("Sauce Labs Backpack")
        
        items_count = cart_page.get_cart_items_count()
        assert items_count == 1
        print("Producto removido del carrito")