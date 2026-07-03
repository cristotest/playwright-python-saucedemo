from pages.base_page import BasePage

class ConfirmationPage(BasePage):
    """Page Object para la página de confirmación de compra en SauceDemo"""
    
    # Selectores
    SUCCESS_MESSAGE = ".complete-header"
    SUCCESS_TEXT = ".complete-text"
    BACK_HOME_BUTTON = "#back-to-products"
    PONY_IMAGE = ".pony_express"
    
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/checkout-complete.html"
    
    def get_success_message(self) -> str:
        """Regresa mensaje de éxito de la compra"""
        message = self.get_text(self.SUCCESS_MESSAGE)
        print(f"Mensaje: {message}")
        return message
    
    def get_success_text(self) -> str:
        """Regresa texto de descripción de éxito"""
        text = self.get_text(self.SUCCESS_TEXT)
        return text
    
    def is_order_complete(self) -> bool:
        """Verifica si la orden fue completada exitosamente"""
        message = self.get_success_message()
        is_complete = "Thank you for your order" in message
        print(f"Orden completada: {is_complete}")
        return is_complete
    
    def click_back_home(self):
        """Regresa a la página de productos desde la confirmación de compra"""
        print("Volviendo al inicio...")
        self.click(self.BACK_HOME_BUTTON)
        print("De vuelta en productos")