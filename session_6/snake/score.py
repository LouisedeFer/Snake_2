class Score :
    """Define the score."""
    MAX_LENGHT = 8


    def __init__(self, score : int, name : str) -> None:
        """Initialize."""
        self._score=score
        self._name=name[:self.MAX_LENGHT]

    @property
    def name(self) -> str :
        """Return the name."""
        return self._name

    @property 
    def score(self) -> int :
        """Return the score."""
        return self._score

    def __lt__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(object, Score) and self._score< other._score

