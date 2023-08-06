from .Base import Base

class Charge(Base):
    endpoint='charges'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.amount = 0
        self.posted = False
        # Relationships
        self.chargeable_id = None
        self.chargeable_type = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
