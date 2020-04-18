import enum


class ProductStatus(str, enum.Enum):
    AVAILABLE = "Available"
    NOT_AVAILABLE = "Not Available"

    def __str__(self):
        return self.value
