from .Base import Base

class Store(Base):
    endpoint='tags'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.hours = None
        self.image = None
        self.info = None
        self.name = None
        self.phone = None
        self.warehouse = False
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
