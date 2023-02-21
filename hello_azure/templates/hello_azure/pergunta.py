import random as rd


class Pergunta:
    index: int
    p: list = ["" for i in range(10)]
    r: list = ["" for j in range(10)]
    sessions: dict = {}

    def __init__(self):
        self.index = 0
        self.p[0] = "Quanto é noventa e nove menos um?"
        self.r[0] = "99-1=98"
        self.p[1] = "Quanto é cinco vezes treze menos zero?"
        self.r[1] = "5x13-0=65"
        self.p[2] = "Quanto é nove mais catorze mais dois?"
        self.r[2] = "9+14+2=25"
        self.p[3] = "Quanto é onze menos um mais um?"
        self.r[3] = "11-1+1=11"
        self.p[4] = "Quanto é vinte e três vezes dois?"
        self.r[4] = "23x2=46"
        self.p[5] = "Quanto é sete mais oito?"
        self.r[5] = "7+8=15"
        self.p[6] = "Quanto é (doze dividido por três) vezes quatro?"
        self.r[6] = "(12/3)x4=16"
        self.p[7] = "Quanto é onze mais onze menos dez?"
        self.r[7] = "11+11-10=12"
        self.p[8] = "Quanto é dezesseis vezes dois?"
        self.r[8] = "16x2=32"
        self.p[9] = "Quanto é noventa e nove menos um?"
        self.r[9] = "99-1=98"
        return

    def getPergunta(self, session_key, secret):
        self.index = rd.randrange(10)
        self.sessions[session_key + secret] = self.index
        return self.index, self.p[self.index]

    def getResposta(self, n):
        return self.r[n]

    def popSession(self, s):
        ix = self.sessions[s]
        p = self.p[ix]
        r = self.r[ix]
        self.sessions.pop(s)
        return p, r
