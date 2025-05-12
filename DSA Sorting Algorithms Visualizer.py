import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


'''Global Variables'''
# Generate random list
amount = 15
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

'''Sorting Algorithms'''
def count_sort_visualizer(lst, x):
    # Step 1: Frequency array setup
    max_number = max(lst)
    min_number = min(lst)
    range_size = max_number - min_number + 1
    frequency_array = [0] * range_size
    sorted_lst = [0] * len(lst)

    # Step 2: Count frequencies
    for num in lst:
        frequency_array[num - min_number] += 1

    # Step 3: Cumulative array
    for i in range(1, len(frequency_array)):
        frequency_array[i] += frequency_array[i - 1]

    # Step 4: Sorting (stable, in reverse), with visualization
    for num in reversed(lst):
        index = frequency_array[num - min_number] - 1
        sorted_lst[index] = num
        frequency_array[num - min_number] -= 1

        # Visualize current state
        plt.bar(x, sorted_lst, color='skyblue')
        plt.pause(0.1)
        plt.clf()

    # Final sorted array visualization
    plt.bar(x, sorted_lst, color='green')
    plt.show()

def on_sort_click():
    count_sort_visualizer(lst, x)

def bubble_sort_visualizer(lst, x):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            plt.bar(x, lst, color='orange')
            plt.pause(0.1)
            plt.clf()
    plt.bar(x, lst, color='green')
    plt.show()

def insertion_sort_visualizer(lst, x):
    indexing_length = range(1, len(lst))
    for i in indexing_length:
        value_to_sort = lst[i]
        while lst[i-1] > value_to_sort and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i = i - 1
            plt.bar(x, lst, color='orange')
            plt.pause(0.1)
            plt.clf()
    plt.bar(x, lst, color='green')
    plt.show()

def selection_sort_visualizer(lst, x):
    indexing_length = range(0, len(lst-1))
    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_value]:
                min_value = j

        if min_value != i:
            lst[min_value], lst[i] = lst[i], lst[min_value]
            plt.bar(x, lst, color='orange')
            plt.pause(0.1)
            plt.clf()
    plt.bar(x, lst, color='green')
    plt.show()

'''Tkinter GUI'''
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Dropdown for sorting algorithms
algo_var = tk.StringVar(root)
algo_var.set("Counting Sort")  # default

algorithms = ["Counting Sort", "Bubble Sort", "Insertion Sort", "Selection Sort"]
dropdown = tk.OptionMenu(frame, algo_var, *algorithms)
dropdown.config(font=('Arial', 12))
dropdown.pack(pady=10)

# Title
title_label = tk.Label(frame, text="Choose Sorting Algorithm", font=('Arial', 14))
title_label.pack(pady=5)

# Start Button
def on_sort_click():
    selected_algo = algo_var.get()
    if selected_algo == "Counting Sort":
        count_sort_visualizer(lst.copy(), x)
    elif selected_algo == "Bubble Sort":
        bubble_sort_visualizer(lst.copy(), x)
    elif selected_algo == "Insertion Sort":
        insertion_sort_visualizer(lst.copy(), x)
    elif selected_algo == "Selection Sort":
        selection_sort_visualizer(lst.copy(), x)

start_button = tk.Button(frame, text="Start Sorting", command=on_sort_click, font=('Arial', 12), bg='lightblue')
start_button.pack(pady=10)

# Regenerate list
def regenerate_list():
    global lst
    lst = np.random.randint(0, 100, amount)
    messagebox.showinfo("New List", f"New List Generated:\n{lst}")

regen_button = tk.Button(frame, text="Regenerate List", font=('Arial', 10), command=regenerate_list, bg='lightgray')
regen_button.pack()

root.mainloop()