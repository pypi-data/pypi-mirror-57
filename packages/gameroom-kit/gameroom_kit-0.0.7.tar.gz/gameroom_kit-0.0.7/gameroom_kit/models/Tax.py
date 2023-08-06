from .Base import Base

class Tax(Base):
    endpoint='taxes'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.amount = 0
        self.name = None
        self.percent = '0.000'
        self.rank = 0
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
