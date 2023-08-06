from enum import Enum


class UserRole(Enum):
    STUDENT = 1 << 0
    LECTURER = 1 << 1
    ADMIN = 1 << 2
