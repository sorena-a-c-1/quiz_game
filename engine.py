class Question:
    def __init__(self,text: str,options: list[str],correct: str):
        self._text: str = text
        self._options: list[str] =list[options]
        self._correct: str = correct


    @property
    def text(self):
        return self._text

    @property
    def options(self):
        return list(self._options)

    @property
    def correct(self):
        return self._correct

    def is_correct(self,choice):
        return choice.strip().upper() == self._correct

    def correct_text(self):
        return self._options["ABCD".index(self._correct)]


class RoundResult:
    def __init__(self, status:str,points:int):
        self._status: str = status
        self._points: int = points
    @property
    def status(self):
        return self._status
    @property
    def points(self):
        return self._points
    def add_bouns(self, amount:int):
        self._points+=amount
        


ROUNDS=5
class Match:
    def __init__(self,player1,player2,questions):
        if player1 == player2:
            raise ValueError("chang name")
        if len(questions)<round:
            raise ValueError("erro")
        self._players:list:[str]= [player1,player2]
        self._questions: list[Question]=list(questions)
        self._scores: dict[str,int] ={player1: 0,player2: 1}
        self._round: int = 0
        self._answers: dict[str, tuple[str,float]] = {}
    @property
    def players(self):
        return list(self._players)
    @property
    def round(self):
        return(self._round)
    def score_of(self,player:str):
        return self._scores[player]
    def answer_of(self,player:str):
        return self._answers[player]


    def start_round(self):
        self._round += 1
        self._answers = {}
        return self._questions[self._round - 1]

    def submit(self,player:str,choice: str , elapsed : float):
        self._answers[player] = (choice,elapsed)
    def is_over(self):
        """برسی اتمام بازی"""
        return self._round >= ROUNDS

    def winner(self)-> str | None:
        """نمایش برنده . در صورت مساوی هیچکدام برمیگرداند"""
        player1, player2= self._players
        if self._scores[player1] == self._scores[player2]:
            return None
        if self._scores[player1] > self._scores[player2]:
            return player1
        return player2
    