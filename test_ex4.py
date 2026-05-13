def calcular_bonus(salario_base: float, avaliacao: str) -> float:
    """
    Calcula o bônus anual com base no salário e desempenho.
    """
    # Regra de guarda para salários negativos
    if salario_base < 0:
        return 0.0

    # Mapeamento de percentuais
    percentuais = {
        "Excelente": 0.20,
        "Bom": 0.10,
        "Regular": 0.02
    }

    # Busca o percentual no dicionário; se não encontrar, o padrão é 0.0
    percentual = percentuais.get(avaliacao, 0.0)
    
    return salario_base * percentual

# Para rodar os testes:
if __name__ == "__main__":
    unittest.main()
