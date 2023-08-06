from .Base import Base

class User(Base):
    endpoint='users'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.admin = False
        self.avatar = None
        self.email = None
        self.first_name = None
        self.last_name = None
        self.locked = False
        self.time_zone = None
        self.token = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
        # Password
        # Apply if there is a password supplied
