class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username


    @username.setter
    def username(self, vakue):
        if not 5 <= len(vakue) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        
        self.__username = vakue


    @property
    def password(self):
        return self.__password


    @password.setter
    def password(self, value):
        if len(value) < 8 or not any(d.isdigit() for d in value) or not any(c.isalpha() and c == c.upper() for c in value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# Test Code

# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
