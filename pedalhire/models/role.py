import enum

class Role(str, enum.Enum):
    USER = "USER"
    MERCHANT = "MERCHANT"

    def __str__(self):
        return self.value