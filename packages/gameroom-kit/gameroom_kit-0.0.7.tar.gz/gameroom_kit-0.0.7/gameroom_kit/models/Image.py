from .Base import Base

class Image(Base):
    endpoint='images'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.caption = None
        self.image = None
        self.position = 0
        # Relationships
        self.imageable_id = None
        self.imageable_type = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
