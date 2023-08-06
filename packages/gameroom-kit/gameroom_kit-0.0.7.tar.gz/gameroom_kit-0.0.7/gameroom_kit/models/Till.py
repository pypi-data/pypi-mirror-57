from .Base import Base

class Till(Base):
    endpoint='tills'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.archived = False
        self.name = None
        # Relationships
        self.store_id = None
        self.user_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
