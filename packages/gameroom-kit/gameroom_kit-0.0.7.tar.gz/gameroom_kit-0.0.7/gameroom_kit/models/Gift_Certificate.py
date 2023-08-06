from .Base import Base

class Gift_Certificate(Base):
    endpoint='gift_certificates'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.pan = None
        # Relationships
        self.customer_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
