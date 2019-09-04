from unittest import TestCase, main
from romeu_e_julieta import RomeuEJulieta

class TestRomeuEJulieta(TestCase):
    #metodos de teste
    def test_romeu(self):
        vl_entrada = 3
        rj = RomeuEJulieta(vl_entrada)
        self.assertEqual(rj.romeuEJulieta(), "queijo")

    def test_julieta(self):
        vl_entrada = 5
        rj = RomeuEJulieta(vl_entrada)
        self.assertEqual(rj.romeuEJulieta(), "goiabada")

    def test_romeu_e_julieta(self):
        vl_entrada = 15
        rj = RomeuEJulieta(vl_entrada)
        self.assertEqual(rj.romeuEJulieta(), "romeu e julieta")

main()