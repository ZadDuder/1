import tkinter as tk

def calculate_time():
    try:
        boat_speed = float(speed_boat_entry.get())
        river_speed = float(speed_river_entry.get())
        distance = float(distance_entry.get())
        direction = direction_var.get()
        
        if direction == "downstream":
            effective_speed = boat_speed + river_speed
        elif direction == "upstream":
            effective_speed = boat_speed - river_speed
        else:
            result_label.config(text="Выберите направление")
            return
        
        if effective_speed <= 0:
            result_label.config(text="Лодка не сможет плыть против течения")
            return
        
        time = distance / effective_speed
        result_label.config(text=f"Время: {time:.2f} часов")
    except ValueError:
        result_label.config(text="Введите корректные числа")

root = tk.Tk()
root.title("Расчет времени движения лодки")

tk.Label(root, text="Скорость лодки (км/ч):").grid(row=0, column=0)
speed_boat_entry = tk.Entry(root)
speed_boat_entry.grid(row=0, column=1)

tk.Label(root, text="Скорость реки (км/ч):").grid(row=1, column=0)
speed_river_entry = tk.Entry(root)
speed_river_entry.grid(row=1, column=1)

direction_var = tk.StringVar()
tk.Radiobutton(root, text="По течению", variable=direction_var, value="downstream").grid(row=2, column=0)
tk.Radiobutton(root, text="Против течения", variable=direction_var, value="upstream").grid(row=2, column=1)

tk.Label(root, text="Дистанция (км):").grid(row=3, column=0)
distance_entry = tk.Entry(root)
distance_entry.grid(row=3, column=1)
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_time)
calculate_button.grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="Время: ")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
