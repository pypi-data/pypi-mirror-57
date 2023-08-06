from .Base import Base

class Option(Base):
    endpoint='options'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.amount = 0
        self.info = None
        self.name = None
        self.percent = '0.000'
        self.position = 0
        # Relationships
        self.option_group_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
