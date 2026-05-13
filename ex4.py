import unittest

class TestCalculoBonus(unittest.TestCase):

    def test_bonus_bom(self):
        # 10% de 3000 = 300.0
        self.assertEqual(calcular_bonus(3000.0, "Bom"), 300.0)

    def test_bonus_excelente(self):
        # 20% de 5000 = 1000.0
        self.assertEqual(calcular_bonus(5000.0, "Excelente"), 1000.0)

    def test_bonus_regular(self):
        # 2% de 2000 = 40.0
        self.assertEqual(calcular_bonus(2000.0, "Regular"), 40.0)

    def test_salario_negativo(self):
        # Salário negativo deve retornar 0.0
        self.assertEqual(calcular_bonus(-1000.0, "Excelente"), 0.0)

    def test_avaliacao_invalida(self):
        # Avaliações fora do padrão retornam 0.0
        self.assertEqual(calcular_bonus(3000.0, "Mais ou Menos"), 0.0)
        self.assertEqual(calcular_bonus(3000.0, "Ruim"), 0.0)
