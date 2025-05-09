import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os

class CheapmealApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cheapmeal Counter App")

        # Ruta base de los íconos
        self.icon_folder = os.path.join(os.path.dirname(__file__), 'icons')

        # Variables
        self.food_options = {
            "Hamburguesa": "burger.png",
            "Pizza": "pizza.png",
            "Hot Dog": "hotdog.png"
        }
        self.selected_food = tk.StringVar(value="Hamburguesa")
        self.days_target = tk.IntVar(value=7)
        self.last_meal_date = None

        # UI
        ttk.Label(root, text="🍔 Elige tu comida tentación:").pack()
        food_menu = ttk.OptionMenu(root, self.selected_food, *self.food_options.keys(), command=self.update_icon)
        food_menu.pack()

        self.icon_label = ttk.Label(root)
        self.icon_label.pack()
        self.update_icon(self.selected_food.get())

        ttk.Label(root, text="📅 Elige cuántos días esperar:").pack()
        ttk.Combobox(root, textvariable=self.days_target, values=[5, 7, 14, 21, 30]).pack()

        ttk.Button(root, text="🍽️ Registré que comí hoy", command=self.set_last_meal_today).pack(pady=5)
        ttk.Button(root, text="⏱️ Ver progreso", command=self.show_progress).pack()

        self.result_label = ttk.Label(root, text="", font=("Arial", 12), foreground="blue")
        self.result_label.pack(pady=10)

    def update_icon(self, food_name):
        icon_filename = self.food_options.get(food_name)
        icon_path = os.path.join(self.icon_folder, icon_filename)

        if os.path.exists(icon_path):
            image = Image.open(icon_path).resize((80, 80))
            self.photo = ImageTk.PhotoImage(image)
            self.icon_label.config(image=self.photo, text="")
        else:
            self.icon_label.config(image='', text="(Icono no encontrado)")

    def set_last_meal_today(self):
        self.last_meal_date = datetime.now().date()
        messagebox.showinfo("Registrado", f"Tu última {self.selected_food.get()} fue hoy.")
        self.show_progress()

    def show_progress(self):
        if not self.last_meal_date:
            self.result_label.config(text="¡Aún no registraste tu última comida!")
            return

        today = datetime.now().date()
        days_passed = (today - self.last_meal_date).days
        days_left = self.days_target.get() - days_passed

        if days_left <= 0:
            text = f"🎉 ¡Ya puedes comer {self.selected_food.get()} de nuevo!"
        else:
            text = f"⏳ Te faltan {days_left} días para tu próxima {self.selected_food.get()}."

        self.result_label.config(text=text)

# Lanzar app
if __name__ == "__main__":
    root = tk.Tk()
    app = CheapmealApp(root)
    root.mainloop()
