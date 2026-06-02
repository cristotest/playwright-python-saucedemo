class LoginPage:

    username_input_selector = "#user-name"
    password_input_selector = "#password"
    login_button_selector = "#login-button"
    error_message_selector = "[data-test='error']"

    error_message_password_required = "Epic sadface: Password is required"
    error_message_username_required = "Epic sadface: Password is required"
    error_message_locked_user = "Epic sadface: Password is required"
    error_message_invalid_password = "Epic sadface: Password is required"

    def __init__(self, page):
        self.page = page
        
    def navigate(self, url):
        self.page.goto(url)
        self.set_username(2)
        
    
    def set_username(self,username:str):
        self.page.selector(self.username_input_selector).fill(username)


    def accept_login(self):
        self.page.selector(self.login_button_selector).click()


    def login(self, username, password):
        self.set_username(username=username)
        self.page.fill(self.password_input, password)
        self.accept_login()
        
    def get_error_message(self):
        return self.page.text_content("[data-test='error']")
