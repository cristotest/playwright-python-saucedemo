class LoginPage:
    
    username_input_selector = "#user-name"
    password_input_selector = "#password"
    login_button_selector = "#login-button"
    error_message_selector = "[data-test='error']"
    
    error_message_username_required = "Epic sadface: Username is required"
    error_message_password_required = "Epic sadface: Password is required"
    error_message_locked_user = "Epic sadface: Sorry, this user has been locked out."
    error_message_invalid_credentials = "Epic sadface: Username and password do not match any user in this service"
    
    
    def __init__(self, page):
        self.page = page
        
    def navigate(self, url):
        self.page.goto(url)
        
    def set_username(self,username:str):
        self.page.get_by_role("textbox", name="Username").fill(username)
        
    def accept_login(self):
        self.page.get_by_role("button", name="Login").click()
        
    def login(self, username, password):
        self.set_username(username=username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.accept_login()
        
    def get_error_message(self):
        return self.page.text_content("[data-test='error']")
