import typing

from .score import Score  # noqa: D100


class Scores :
    """Contains instances of Score."""

    def __init__(self, max_scores : int, scores : list[Score]) -> None :
        """Define the scores."""
        self._max_scores=max_scores
        scores.sort(reverse=True)
        self._scores=scores[:max_scores]


    @classmethod
    def default(cls, max_scores : int ) -> "Scores" :
        """Classmethod."""
        return cls(max_scores, [Score(name="Joe", score=100), Score(name="Jack", score=80), Score(name="William", score=60), Score(name="Averell", score=50)])  # noqa: E501

    def __iter__(self) -> typing.Iterator[Score]:
        """Iterate on the list of scores."""
        return iter(self._scores)
    
    #def is_highscore(self) :

