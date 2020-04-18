import enum


class OrderStatus(str, enum.Enum):
    WAITING_FOR_CONFIRMATION = "Waiting for Confirmation"
    BOOKED = "Booked"
    IN_CART = "In Cart"
    CANCELLED = "Cancelled"

    def __str__(self):
        return self.value
