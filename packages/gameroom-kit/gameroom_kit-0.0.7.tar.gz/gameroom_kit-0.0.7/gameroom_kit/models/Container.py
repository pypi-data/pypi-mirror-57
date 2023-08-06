from .Base import Base

class Container(Base):
    endpoint='containers'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.info = None
        self.name = None
        # Relationships
        self.store_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
