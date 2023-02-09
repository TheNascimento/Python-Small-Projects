__author__ = 'Tiago Luiz'
# Exemplos de manipulação de diferentes tipos de dados.

num_int = 5
num_dec = 2.5
val_str = "Tiago Luiz"

print("O valor é:", num_int)
print("O valor é: %i" %num_int)
print("O valor é: "+str(num_int))

print("\nConcatenando decimal:", num_dec)
print("Concatenando decimal: %.10f" %num_dec)
print("Concatenando decimal: "+str(num_dec))

print("\nConcatenando string:", val_str)
print("Concatenando string: %s" %val_str)
print("Concatenando string: "+val_str)