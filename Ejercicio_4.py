#Función Palíndromo 
def num_palindromo(num):
   longitud = len(num)
   if longitud % 2 == 0:
     izquierda = num[: longitud // 2]
     derecha = num[longitud // 2:]
   else:
        izquierda = num[:longitud // 2]
        derecha = num[longitud // 2+1:]
        
 
   return izquierda == derecha [::-1]
   
print(num_palindromo(input("Ingrese el número natural: ")))   