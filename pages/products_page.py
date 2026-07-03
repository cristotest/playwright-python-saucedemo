from pages.base_page import BasePage


class ProductsPage(BasePage):
    PRODUCT_NAME = ".inventory_item_name"
    PRODUCT_PRICE = ".inventory_item_price"
    SORT_DROPDOWN = ".product_sort_container"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    ADD_TO_CART_BUTTON_TEMPLATE = (
        "//div[contains(@class,'inventory_item')]"
        "[.//div[text()='{}']]//button"
    )

    def add_product_to_cart_by_name(self, product_name):
        button = self.page.locator(
            self.ADD_TO_CART_BUTTON_TEMPLATE.format(product_name)
        )
        button.wait_for(state="visible", timeout=5000)
        button.click()

    
    def add_product_to_cart(self, product_name):
        self.add_product_to_cart_by_name(product_name)

    def get_cart_badge_count(self):
        badge = self.page.locator(self.CART_BADGE)
        return badge.text_content() if badge.is_visible() else "0"

    def go_to_cart(self):
        cart = self.page.locator(self.CART_LINK)
        cart.wait_for(state="visible", timeout=5000)
        cart.click()

    def sort_products(self, sort_order):
        """az, za, lohi, hilo"""
        dropdown = self.page.locator(self.SORT_DROPDOWN)
        dropdown.wait_for(state="visible", timeout=5000)
        dropdown.select_option(sort_order)

    
    def get_product_names(self):
        items = self.page.locator(self.PRODUCT_NAME)
        items.first.wait_for(state="visible", timeout=5000)
        return items.all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(self.PRODUCT_PRICE)
        prices.first.wait_for(state="visible", timeout=5000)
        values = prices.all_text_contents()
        return [float(p.replace("$", "")) for p in values]