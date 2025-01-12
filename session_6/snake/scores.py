import typing

from .score import Score


class Scores :
    """Contains instances of scores."""

    def __init__(self, max_scores : int, scores : list[Score]) -> None :
        """Define the scores."""
        self._max_scores=max_scores
        scores.sort(reverse=True)
        self._scores=scores[:max_scores]
 

    @classmethod
    def default(cls, max_scores : int ) -> "Scores" :
        """Classmethod."""
        return cls(max_scores, [Score (score=10, name="Joe"), Score(score=8, name="Jack"), Score(score=1,name="Averell"), Score(score=6, name="William")])

    def __iter__(self) -> typing.Iterator[Score]:
        """Iterate on the list of scores."""
        return iter(self._scores)


    @property
    def liste_scores(self) -> list[Score] :
        """Return the list of the Scores."""
        return self._scores

    def add_score(self, score: Score) -> None:
        """Add a score and sort the list."""
        self.liste_scores.append(score)
        self.liste_scores.sort(reverse=True)
        if len(self.liste_scores) > self._max_scores:
            self.liste_scores.pop()  # Garder uniquement les meilleurs scores


    def is_highscore(self, score_player : int) -> bool :
        """Define the case highscore."""
        flag=False # not a highscore
        if len(self.liste_scores)<self._max_scores :
            self.add_score(Score(name="B", score = score_player ))
            flag=True
        else :
            for score_other in self._scores :
                if score_player > score_other.score and flag is False :
                    self.add_score(Score(name="A", score=score_player))
                    flag=True
        return flag










