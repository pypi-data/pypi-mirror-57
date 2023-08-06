from enum import Enum

class UserRole(Enum):
    LECTURER = 1 << 0
    ADMIN = 1 << 1