from .Base import Base

class Address(Base):
    endpoint='addresses'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.city = None
        self.country = None
        self.name = None
        self.position = 0
        self.state = None
        self.street1 = None
        self.street2 = None
        self.zip = None
        # Relationships
        self.addressable_id = None
        self.addressable_type = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
