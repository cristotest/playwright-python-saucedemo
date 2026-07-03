import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
class TestProducts:
    """Tests para la funcionalidad de productos en SauceDemo"""
    
    def test_add_single_product(self, page):
        """TC002: Agregar producto al carrito"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        
        # Validar que el badge del carrito muestra "1"
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == "1"
        print("Producto agregado al carrito")
    
    @pytest.mark.smoke
    def test_add_multiple_products(self, page):
        """TC003: Agregar múltiples productos al carrito"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        products_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        products_page.add_product_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        
        # Validar que el badge del carrito muestra "3"
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == "3"
        print("Múltiples productos agregados")
    
    def test_sort_products_a_to_z(self, page):
        """TC013: Ordenar productos de A a Z"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.sort_products("az")
        
        names = products_page.get_product_names()
        assert names == sorted(names), "Products not sorted A-Z"
        print("Productos ordenados A-Z correctamente")
    
    def test_sort_products_z_to_a(self, page):
        """TC014: Ordenar productos de la Z a la A"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.sort_products("za")
        
        names = products_page.get_product_names()
        assert names == sorted(names, reverse=True), "Products no ordenados Z-A"
        print("Productos ordenados Z-A correctamente")
    
    def test_sort_products_price_low_to_high(self, page):
        """TC015: Ordenar productos por precio (de bajo a alto)"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        products_page = ProductsPage(page)
        products_page.sort_products("lohi")
        
        prices = products_page.get_product_prices()
        assert prices == sorted(prices), "Products not sorted by price"
        print("Productos ordenados por precio correctamente")
        