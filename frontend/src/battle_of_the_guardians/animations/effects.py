from typing import Callable


class _EnumEffects:
    def __init__(self):
        self._effects: dict[str, Callable[[float], float]] = {'linear': lambda x: x}

    def __getattr__(self, item: str) -> Callable[[float], float]:
        return self._effects[item]

    def __getitem__(self, item: str) -> Callable[[float], float]:
        return self._effects[item]


_Effects = _EnumEffects()
