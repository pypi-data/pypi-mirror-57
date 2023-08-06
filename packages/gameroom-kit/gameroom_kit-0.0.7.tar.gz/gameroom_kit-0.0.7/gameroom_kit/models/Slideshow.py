from .Base import Base

class Slideshow(Base):
    endpoint='slideshows'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.name = None
        self.position = 0
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
