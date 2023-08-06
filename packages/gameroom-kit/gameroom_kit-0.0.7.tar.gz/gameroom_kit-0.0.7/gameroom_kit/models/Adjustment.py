from .Base import Base

class Adjustment(Base):
    endpoint='adjustments'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.amount = 0
        self.archived = False
        self.info = None
        self.posted = False
        self.reason = 0 # Enum
        # Relationships
        self.source_id = None
        self.destination_id = None
        self.user_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
