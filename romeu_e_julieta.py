class RomeuEJulieta():
    #atributos
    vl_entrada = 0

    #metodos
    def romeu(self):
        res = False
        if self.vl_entrada % 3 == 0:
            res = True
        return res

    def julieta(self):
        res = False
        if self.vl_entrada % 5 == 0:
            res = True
        return res

    def romeuEJulieta(self):
        if self.romeu() is True and self.julieta() is True:
            return "romeu e julieta"
        elif self.julieta() is True:
            return "julieta"
        elif self.romeu() is True:
            return "romeu"
        else:
            return "erro"

    #construtor
    def __init__(self, vl_entrada):
        self.vl_entrada = vl_entrada