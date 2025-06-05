from abc import ABC


class Arma():
    def __init__(self,Nome: str, DannoArma: int):
        self.Nome = Nome
        self.DannoArma = DannoArma

    def __str__(self):
        return f"{self.Nome}, {self.DannoArma}"