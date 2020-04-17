import enum

class Role(str, enum.Enum):
    PROCESSOR = "PROCESSOR"
    PRODUCER = "PRODUCER"

    def __str__(self):
        return self.value
