from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object para la página de checkout en SauceDemo (Información y Overview)"""
    
    # Selectores - Paso 1 (Información)
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"
    ERROR_MESSAGE = "[data-test='error']"
    
    # Selectores - Paso 2 (Overview)
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"
    FINISH_BUTTON = "#finish"
    
    def __init__(self, page):
        super().__init__(page)
    
    def fill_information(self, first_name: str, last_name: str, zip_code: str):
        """Llena el formulario de información del checkout"""
        print(f"Llenando información: {first_name} {last_name}")
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.ZIP_CODE, zip_code)
        print("Información completada")
    
    def click_continue(self):
        """Navegar al overview del checkout"""
        print("Continuando a overview...")
        self.click(self.CONTINUE_BUTTON)
        print("En checkout overview")
    
    def get_error_message(self) -> str:
        """Se visualiza mensaje de error si falta información en el formulario"""
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def get_item_total(self) -> str:
        """Regresa el subtotal de los items en checkout overview"""
        return self.get_text(self.ITEM_TOTAL)
    
    def get_tax(self) -> str:
        """Regresa el monto del impuesto desde el overview del checkout"""
        return self.get_text(self.TAX)
    
    def get_total(self) -> str:
        """Regresa el monto total desde el overview del checkout"""
        return self.get_text(self.TOTAL)
    
    def click_finish(self):
        """Click botón de finalizar compra en checkout overview"""
        print("Finalizando compra...")
        self.click(self.FINISH_BUTTON)
        print("Compra finalizada")