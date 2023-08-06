from .Base import Base

class Line(Base):
    endpoint='lines'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.amount = 0
        self.info = None
        self.name = None
        self.quantity = 0
        self.refunded = False
        self.subname = None
        self.tax = 0
        self.tax_percent = None
        # Relationships
        self.sale_id = None
        self.saleable_id = None
        self.saleable_type = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
