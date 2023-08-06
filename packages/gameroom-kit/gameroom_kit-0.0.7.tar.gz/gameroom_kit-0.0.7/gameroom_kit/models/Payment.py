from .Base import Base

class Payment(Base):
    endpoint='payments'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.amount = 0
        self.gateway = None
        self.info = None
        self.reference = None
        # Relationships
        self.payable_id = None
        self.payable_type = None
        self.sale_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
