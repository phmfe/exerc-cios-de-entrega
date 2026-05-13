def calcular_bonus(salario_base: float, avaliacao: str) -> float:
   
    if salario_base < 0:
        return 0.0
    
  
    avaliacao = avaliacao.capitalize()
    

    if avaliacao == "Excelente":
        percentual = 0.20
    elif avaliacao == "Bom":
        percentual = 0.10
    elif avaliacao == "Regular":
        percentual = 0.02
    else:
        percentual = 0.0  # Para "Ruim" ou qualquer outra coisa
        

    valor_final = salario_base * percentual
    return valor_final


print(f"Bônus Excelente: R$ {calcular_bonus(3000, 'Excelente')}")
print(f"Bônus Bom: R$ {calcular_bonus(2000, 'bom')}")
print(f"Bônus Regular: R$ {calcular_bonus(1000, 'REGULAR')}")
print(f"Bônus Inválido/Ruim: R$ {calcular_bonus(1500, 'Ruim')}")
print(f"Bônus Salário Negativo: R$ {calcular_bonus(-500, 'Excelente')}")
