def calcular_frete(peso_kg: float) -> float:

    valor_frete = 0.0
    
  
    if peso_kg <= 0:
        valor_frete = 0.0
    elif peso_kg <= 1.0:
        valor_frete = 5.0
    elif peso_kg <= 5.0:
        valor_frete = 10.0
    else:
        valor_frete = 18.0
        
    return valor_frete


print(f"Frete peso 0: R$ {calcular_frete(0)}")
print(f"Frete peso -10: R$ {calcular_frete(-10)}")
print(f"Frete peso 1.0kg: R$ {calcular_frete(1.0)}")
print(f"Frete peso 1.01kg: R$ {calcular_frete(1.01)}")
print(f"Frete peso 5.0kg: R$ {calcular_frete(5.0)}")
print(f"Frete peso 5.01kg: R$ {calcular_frete(5.01)}")
