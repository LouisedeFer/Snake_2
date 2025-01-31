import typing
from pathlib import Path

import yaml
import logging
from .score import Score

logger = logging.getLogger("foo")


class Scores :
    """Contains instances of scores."""

    def __init__(self, max_scores : int, scores : list[Score]) -> None :
        """Define the scores."""
        self._max_scores=max_scores
        self._scores=sorted(scores, reverse = True)[:max_scores]

    @classmethod
    def default(cls, max_scores : int ) -> "Scores" :
        """Classmethod."""
        return cls(max_scores, [Score (score=-1, name="Joe"), Score(score=8, name="Jack"), Score(score=0,name="Averell"), Score(score=6, name="William")])

    @classmethod
    def load(cls,scores_file : Path, max_scores : int) -> "Scores" :
        """Load the file."""
        with scores_file.open("r") as fd : #(file descriptor)
            g=yaml.safe_load(fd)
            logger.info("load the file")
            x=[Score(score=elt["score"], name=elt["name"])for elt in g]
        return cls(max_scores, x)



    def __iter__(self) -> typing.Iterator[Score]:
        """Iterate on the list of scores."""
        return iter(self._scores)


    def is_highscore(self, score_player : int) -> bool :
        """Define the case highscore."""
        return len(self._scores)<self._max_scores or score_player >= self._scores[-1].score

    def add_score(self, score_player: Score) -> None:
        """Add a score and sort the list."""
        if self.is_highscore(score_player.score):
            if len(self._scores)>=self._max_scores :
                self._scores.pop()
            self._scores.append(score_player)
            self._scores.sort(reverse=True)
            logger.info("New score added.")

    def save(self, scores_file : Path) -> None:
        """Save the scores' file given."""
        x=[{"name" : s.name, "score" : s.score} for s in self]
        with scores_file.open("w+") as fd : #(file descriptor), create a file if it doesn't exist
            yaml.safe_dump(x,fd )



















