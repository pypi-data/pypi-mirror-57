from .Base import Base

class Unit_Option(Base):
    endpoint='unit_options'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        # Relationships
        self.option_id = None
        self.unit_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
