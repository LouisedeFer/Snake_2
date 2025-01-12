class Score :
    """Define the score with a name and a score (int)."""

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

    # Implemente the comparaison operators to use the function sort in the lists
    def __gt__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score > other._score

    def __lt__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score < other._score

    def __eq__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score == other._score

    def __ge__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score >= other._score

    def __le__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score <= other._score

    def __ne__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score != other._score

    def __repr__(self) -> str:
        """Representation."""
        return f"Score(name={self._name}, score={self._score})"