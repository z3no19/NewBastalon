from abc import ABC


class Arma():
    def __init__(self,Nome: str, DannoArma: int, ArmaID: int):
        self.Nome = Nome
        self.DannoArma = DannoArma
        self.ArmaID = ArmaID

