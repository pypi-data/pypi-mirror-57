from .Base import Base

class Slide(Base):
    endpoint='slides'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.name = None
        self.caption = None
        self.dwell = 0
        self.image = None
        self.position = 0
        self.visible = True
        # Relationships
        self.slideshow_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
