class Action:
    def __init__(self, kind: str, value: tuple[int, int] = (0, 0)) -> None:
        self.kind = kind
        self.value = value
