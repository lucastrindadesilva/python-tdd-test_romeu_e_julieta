from romeu_e_julieta import RomeuEJulieta

#funcoes
def test_romeu():
    vl_entrada = 3
    rj = RomeuEJulieta(vl_entrada)
    assert rj.romeuEJulieta() == "romeu"

def test_julieta():
    vl_entrada = 5
    rj = RomeuEJulieta(vl_entrada)
    assert rj.romeuEJulieta() == "julieta"

def test_romeu_e_julieta():
    vl_entrada = 15
    rj = RomeuEJulieta(vl_entrada)
    assert rj.romeuEJulieta() == "romeu e julieta"