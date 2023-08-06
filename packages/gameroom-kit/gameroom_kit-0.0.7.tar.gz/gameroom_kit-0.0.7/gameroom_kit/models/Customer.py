from .Base import Base

class Customer(Base):
    endpoint='customers'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.first_name = None
        self.email = None
        self.last_name = None
        self.locked = None
        self.middle_name = None
        self.phone = None
        self.prefix = None
        self.suffix = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
        # Password
        # Apply if there is a password supplied
