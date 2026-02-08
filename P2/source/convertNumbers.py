# pylint: disable=invalid-name
# pylint: disable=broad-exception-caught
'''
    Docstring for convertNumbers
'''

import sys
import time

#Convierte decimal a binario
def dec_to_bin(n):
    '''
    Docstring for dec_to_bin
    La conversión está fijada a 32
    '''
    BASE = 32
    LONG = 2 ** 32

    if n == 0:
        return "0" * BASE

    # Manejo de números negativos
    if n < 0:
        n = n + LONG

    binary_digits = []
    while n > 0:
        modulo = n % 2
        binary_digits.append(str(modulo))
        n = n // 2  # División entera

    # Se generan los dígitos al revés por lo que se invierten
    binary = "".join(reversed(binary_digits))

    while len(binary) < BASE:
        binary = "0" + binary

    return binary

#Convierte decimal a hexadecimal
def dec_to_hex(n):
    '''
    Docstring for dec_to_hex
    La conversion está fijada a 32 bits
    '''
    LONG = 2 ** 32

    if n == 0:
        return "00000000"

    # Manejo de números negativos
    if n < 0:
        n = n + LONG

    hex_map = "0123456789ABCDEF"
    hex_digits = []

    while n > 0:
        modulo = n % 16
        hex_digits.append(hex_map[modulo])
        n = n // 16 # División entera

    # Se generan los dígitos al revés por lo que se invierten
    hexa = "".join(reversed(hex_digits))

    while len(hexa) < 8:
        hexa = "0" + hexa

    return hexa

#Programa principal

if len(sys.argv) != 2:
    print("El formato de solicitud es incorrecto, " \
    "deberia ser: python *Nombre del script*.py *Archivo a leer*.txt")
    sys.exit(1)

else:
    input_file = sys.argv[1]
    start_time = time.time()

    OUTPUT_FILE = "ConvertionResults.txt"
    data = []
    data_bin = []
    data_hex = []

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                raw_num = line.strip()

                #Saltar líneas vacías
                if not raw_num:
                    continue

                try:
                    number = int(raw_num)
                    data.append(number)
                    data_bin.append(dec_to_bin(number))
                    data_hex.append(dec_to_hex(number))

                except ValueError:
                    print(f"Error: Dato inválido en línea {line_num}: '{raw_num}'")

    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        sys.exit(1)

    except Exception as e:
        print(f"Error inesperado leyendo el archivo: {e}")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time

    #Se le da formato a la salida
    result = []
    result.append("Conversión de números\n")
    result.append(f"{'DECIMAL':<15} {'BINARIO':<25} {'HEXADECIMAL':<15}\n")

    for dec, bin_num, hex_num in zip(data,data_bin,data_hex):
        result.append(f"{dec:<15} {bin_num:<25} {hex_num:<15}")

    result.append(f"\nTiempo de ejecucción: {elapsed_time:.6f} segundos")

    OUT_STRING = "\n".join(result)

    #Mostrar en la terminal
    print(OUT_STRING)

    #Se guarda en archivo externo
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
            file.write(OUT_STRING)
        print(f"\nResultados guardados exitosamente en {OUTPUT_FILE}")

    except Exception as e:
        print(f"Error escribiendo el archivo de resultados: {e}")
