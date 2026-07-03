from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CART_BADGE = ".shopping_cart_badge"

    def get_cart_items_count(self):
        items = self.page.locator(self.CART_ITEMS).all()
        return len(items)

    def get_cart_item_names(self):
        items = self.page.locator(self.CART_ITEM_NAME).all()
        return [item.text_content() for item in items]

    # usado por tests checkout
    def go_to_checkout(self):
        btn = self.page.locator(self.CHECKOUT_BUTTON)
        btn.wait_for(state="visible", timeout=5000)
        btn.click()

    # alias por compatibilidad
    def click_checkout(self):
        self.go_to_checkout()

    # usado por tests checkout
    def continue_shopping(self):
        btn = self.page.locator(self.CONTINUE_SHOPPING_BUTTON)
        btn.wait_for(state="visible", timeout=5000)
        btn.click()

    # alias por compatibilidad
    def click_continue_shopping(self):
        self.continue_shopping()

    def remove_product(self, product_name):
        btn = self.page.locator(
            f"//div[contains(@class,'cart_item')]"
            f"[.//div[@class='inventory_item_name' and text()='{product_name}']]"
            f"//button"
        )
        btn.wait_for(state="visible", timeout=5000)
        btn.click()