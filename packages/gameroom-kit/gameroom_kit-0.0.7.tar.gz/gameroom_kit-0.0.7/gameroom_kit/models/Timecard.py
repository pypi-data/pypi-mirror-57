from .Base import Base

class Timecard(Base):
    endpoint='timecards'
    def __init__(self, **kwargs):
        # Base Attributes
        super().__init__()
        # Default attributes
        self.ended_at = time()
        self.ended_correction = time()
        self.info = None
        self.started_at = time()
        self.started_correction = time()
        self.status = 0 # enum
        # Relationships
        self.user_id = None
        # Supplied attributes
        for key, value in kwargs.items():
            if (hasattr(self, key)): setattr(self, key, value)
