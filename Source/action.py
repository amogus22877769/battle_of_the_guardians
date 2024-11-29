class Action:
    def __init__(self, kind: str, value: tuple[int, int]) -> None:
        self.kind = kind
        self.value = value