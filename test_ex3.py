def converter_nota_para_conceito(nota: float) -> str:
   
    if nota < 0 or nota > 10:
        return "Nota inválida"
    
    
    if nota >= 9.0:
        conceito = "A"
    elif nota >= 7.0:
        conceito = "B"
    elif nota >= 5.0:
        conceito = "C"
    elif nota >= 3.0:
        conceito = "D"
    else:
        conceito = "F"
        
    return conceito


notas_para_testar = [10.5, 9.5, 8.9, 7.0, 6.0, 4.9, 2.0, -1]

for n in notas_para_testar:
    resultado = converter_nota_para_conceito(n)
    print(f"Nota: {n} -> Conceito: {resultado}")
