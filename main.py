import random
import matplotlib.pyplot as plt
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Tomar el pivote como el valor central de la lista
    left = [x for x in arr if x < pivot]  # Crear una lista con los elementos menores al pivote
    middle = [x for x in arr if x == pivot]  # Crear una lista con los elementos iguales al pivote
    right = [x for x in arr if x > pivot]  # Crear una lista con los elementos mayores al pivote

    return quick_sort(left) + middle + quick_sort(right)  # Unir las listas ordenadas

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]: 
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
       
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while (swapped == True and start < end):
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if (swapped == False):
            break

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1



def sort_time(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time2(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time3(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time4(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time5(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time6(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    shell_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time7(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    heap_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time8(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    comb_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

def sort_time9(num_elements):
    arr = [random.randint(1, 100) for _ in range(num_elements)]
    start_time = time.time()
    cocktail_sort(arr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed*100

tiempo1 = 0
tiempo1 = 1
tiempo1 = 2
tiempo1 = 3
tiempo1 = 4
tiempo1 = 5
tiempo1 = 6
tiempo1 = 7
tiempo1 = 8

x_data = []
y_data = []
x_data2 = []
y_data2 = []
x_data3 = []
y_data3 = []
x_data4 = []
y_data4 = []
x_data5 = []
y_data5 = []
x_data6 = []
y_data6 = []
x_data7 = []
y_data7 = []
x_data8 = []
y_data8 = []
x_data9 = []
y_data9 = []

num_elements = 1000
interval = 1000

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [])

line2, = ax.plot([], [])

line3, = ax.plot([], [])
line4, = ax.plot([], [])

line5, = ax.plot([], [])
line6, = ax.plot([], [])
line7, = ax.plot([], [])
line8, = ax.plot([], [])
line9, = ax.plot([], [])

ax.set_xlabel('Margen de tamaño de lista')
ax.set_ylabel('Margen tiempo (segundos)')
ax.set_xlim(0, 20000)
ax.set_ylim(0, 20)


for i in range(100):
    x = 1000 * i
    y = sort_time(100 * i)

    y2 = sort_time2(100 * i)
    y3 = sort_time3(100 * i)
    y4 = sort_time4(100 * i)
    y5 = sort_time5(100 * i)
    y6 = sort_time6(100 * i)
    y7 = sort_time7(100 * i)
    y8 = sort_time8(100 * i)
    y9 = sort_time9(100 * i)

    x_data.append(x)
    y_data.append(y)

    x_data2.append(x)
    y_data2.append(y2)
    x_data3.append(x)
    y_data3.append(y3)
    x_data4.append(x)
    y_data4.append(y4)

    x_data5.append(x)
    y_data5.append(y5)
    x_data6.append(x)
    y_data6.append(y6)
    x_data7.append(x)
    y_data7.append(y7)
    x_data8.append(x)
    y_data8.append(y8)
    x_data9.append(x)
    y_data9.append(y9)

    line.set_data(x_data, y_data)
    
    line2.set_data(x_data2, y_data2)
    line3.set_data(x_data3, y_data3)
    line4.set_data(x_data4, y_data4)
    line5.set_data(x_data5, y_data5)
    line6.set_data(x_data6, y_data6)
    line7.set_data(x_data7, y_data7)
    line8.set_data(x_data8, y_data8)
    line9.set_data(x_data9, y_data9)

    plt.title('COMPARACION DE ALGORITMOS DE ORDENAMIENTO')
    plt.legend()
    plt.draw()
    plt.pause(0.5)



plt.ioff()
plt.show()