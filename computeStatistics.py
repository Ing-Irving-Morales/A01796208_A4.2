# pylint: disable=invalid-name
# pylint: disable=broad-exception-caught
'''
Docstring for computeStatistics
'''

import sys
import time

#Calcula el promedio
def cal_mean(data):
    '''
    Docstring for cal_mean
    '''
    return sum(data) / len(data)

#Calcula la mediana
def cal_median(data):
    '''
    Docstring for cal_median
    '''
    n = len(data)
    sorted_data = sorted(data)
    mid = n // 2

    if n % 2 == 1:
        return sorted_data[mid]

    return (sorted_data[mid - 1] + sorted_data[mid]) / 2

#Calcula la moda
def cal_mode(data):
    '''
    Docstring for cal_mode
    '''
    freq = {}
    for num in data:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_count = 0
    modes = 0

    #Se busca la frecuencia máxima
    for count in freq.values():
        max_count = max(max_count, count)

    #Se busca el primer número con esa frecuencia
    for num, count in freq.items():
        if count == max_count:
            modes = num
            break

    return modes

#Calcula la varianza
def cal_variance(data, mean_i):
    '''
    Docstring for cal_variance
    '''
    temp = sum((x - mean_i) ** 2 for x in data)
    return temp / (len(data) - 1)

#Calcula la desviación estandar
def cal_std_dev(variance_i):
    '''
    Docstring for cal_std_dev
    '''
    return variance_i ** 0.5

#Programa principal

if len(sys.argv) != 2:
    print("El formato de solicitud es incorrecto, " \
    "deberia ser: python *Nombre del script*.py *Archivo a leer*.txt")
    sys.exit(1)

else:
    input_file = sys.argv[1]
    start_time = time.time()

    OUTPUT_FILE = "StatisticsResults.txt"
    num_data = []

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                raw_num = line.strip()

                #Saltar líneas vacías
                if not raw_num:
                    continue

                try:
                    number = int(raw_num)
                    num_data.append(number)

                except ValueError:
                    print(f"Error: Dato inválido en línea {line_num}: '{raw_num}'")

    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        sys.exit(1)

    except Exception as e:
        print(f"Error inesperado leyendo el archivo: {e}")
        sys.exit(1)

    # Cálculos
    mean = cal_mean(num_data)
    median = cal_median(num_data)
    mode = cal_mode(num_data)
    variance = cal_variance(num_data, mean)
    std_dev = cal_std_dev(variance)

    end_time = time.time()
    elapsed_time = end_time - start_time

    #Se le da formato a la salida
    result = []
    result.append("Estadísticas Descriptivas\n")
    result.append(f"Promedio:               {mean:.6f}")
    result.append(f"Mediana:                {median:.6f}")
    result.append(f"Moda:                   {mode:.6f}")
    result.append(f"Desviación Estandar:    {std_dev:.6f}")
    result.append(f"Varianza:               {variance:.6f}\n")
    result.append(f"Tiempo de ejecucción: {elapsed_time:.6f} segundos")

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
