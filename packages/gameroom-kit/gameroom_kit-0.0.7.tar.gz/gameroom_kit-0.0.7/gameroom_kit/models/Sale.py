from .Base import Base

class Sale(Base):
    endpoint='sales'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.amount_offset = 0
        self.status = 0 # enum
        self.status_history = list()
        self.tax_offset = 0
        # Relationships
        self.customer_id = None
        self.store_id = None
        self.user_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
