import sys
import time

#Programa principal

if len(sys.argv) != 2:
        print("El formato de solicitud es incorrecto, deberia ser: python *Nombre del script*.py *Archivo a leer*.txt")
        sys.exit(1)

else:
    input_file = sys.argv[1]
    start_time = time.time()
    
    output_file = "WordCountResults.txt"
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
            '''
            #Variable temporal para cada palabra
            current_word = ""
            
            while True:
                #Se lee carater por caracter
                char = file.read(1)
                
                #Se verifica si es el fin del archivo
                if not char:
                    #Se procesa la última palabra guardad en current_word
                    if len(current_word) > 0:
                        if current_word in words:
                            words[current_word] += 1
                        else:
                            words[current_word] = 1
                    break
                
                #Se buscan los separadores comunes, espacio, salto de línea, tabulador, retroceso, para procesar la palabra actual
                if char == ' ' or char == '\n' or char == '\t' or char == '\r':
                    if len(current_word) > 0:
                        #Se procesa la palabra actual
                        if current_word in words:
                            words[current_word] += 1
                        else:
                            words[current_word] = 1
                        #Se reinicia la variable temporal
                        current_word = ""
                else:
                    #Se crea la palabra si el caracter es válido, si no se manda una advertencia
                    if char.isprintable():
                        current_word += char
                    else:
                        print(f"Advertencia: Caracter inválido detectado e ignorado.")
                        continue
    '''
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

    out_string = "\n".join(result)

    #Mostrar en la terminal
    print(out_string)

    #Se guarda en archivo externo
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(out_string)
        print(f"\nResultados guardados exitosamente en {output_file}")
    except Exception as e:
        print(f"Error escribiendo el archivo de resultados: {e}")