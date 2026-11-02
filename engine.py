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
            