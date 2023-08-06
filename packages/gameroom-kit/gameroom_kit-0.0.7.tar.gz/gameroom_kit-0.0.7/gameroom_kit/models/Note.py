from .Base import Base

class Note(Base):
    endpoint='notes'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.info = None
        # Relationships
        self.noteable_id = None
        self.noteable_type = None
        self.user_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
