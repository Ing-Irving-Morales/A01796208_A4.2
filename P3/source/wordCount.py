# pylint: disable=invalid-name
# pylint: disable=broad-exception-caught
'''
    Docstring for wordCount
'''

import sys
import time

#Programa principal

if len(sys.argv) != 2:
    print("El formato de solicitud es incorrecto, " \
    "deberia ser: python *Nombre del script*.py *Archivo a leer*.txt")
    sys.exit(1)

else:
    input_file = sys.argv[1]
    start_time = time.time()

    OUTPUT_FILE = "WordCountResults.txt"
    words = {}

    try:
        with open(input_file, 'r', encoding='utf-8', errors='replace') as file:
            for line_num, line in enumerate(file, 1):
                raw_word = line.strip()

                #Saltar líneas vacías
                if not raw_word:
                    continue

                try:
                    current_word = str(raw_word)

                    if current_word in words:
                        words[current_word] += 1
                    else:
                        words[current_word] = 1
                except ValueError:
                    print(f"Error: Dato inválido en línea {line_num}: '{raw_word}'")

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
    result.append("Contador de Palabras\n")
    result.append(f"{'Palabra':<20}  {'Frecuencia':<10}\n")

    total_words = 0

    for word, count in words.items():
        line = f"{word:<20}  {count:<10}"
        result.append(line)
        total_words = total_words + count

    result.append(f"\nPalabras totales: {total_words}")
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
