def convertir_arabico_romano(num_arabico):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    valor_romano = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    num_romano = ''
    i = 0

    while num_arabico > 0:
        for _ in range(num_arabico // numeros[i]):
            num_romano += valor_romano[i]
            num_arabico -= numeros[i]
        
        i += 1
  
    return num_romano

# ==============================

arabico = int(input('Ingrese un número arábico menor a 4000:'))

while arabico <= 0 or arabico >= 4000:
    arabico = int(input('El número que ingreso es incorrecto, ingrese de nuevo: '))

print(f'El número en romanos es: {convertir_arabico_romano(arabico)}')