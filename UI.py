import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from PIL import Image
import cv2

class SignLanguageLearningApp(ThemedTk):
    def _init_(self, theme="arc"):
        ThemedTk._init_(self, theme=theme, fonts=True, themebg=True)
        self.title("Aprendizaje de Lengua de Señas")
        self.geometry("800x600")  # Establecer un tamaño personalizado para la ventana

        # Crear dos botones medianos
        button_frame = ttk.Frame(self)
        button_frame.pack(expand=True)

        button_style = ttk.Style()
        button_style.configure("Medium.TButton", font=('Helvetica', 16), padding=10)

        button_one = ttk.Button(button_frame, text="Teoría", style="Medium.TButton", command=self.view_theory)
        button_two = ttk.Button(button_frame, text="Exámenes", style="Medium.TButton", command=self.start_exams)
        button_camera = ttk.Button(button_frame, text="Abrir Cámara", style="Medium.TButton", command=self.open_camera)

        button_one.grid(row=0, column=0, padx=10, pady=20)
        button_two.grid(row=0, column=1, padx=10, pady=20)
        button_camera.grid(row=0, column=2, padx=10, pady=20)

        # Bind screenshot button
        self.bind("<F10>", self.screenshot)
        self.bind("<F9>", self.screenshot_themes)

    def view_theory(self):
        # Aquí puedes poner el código para mostrar la teoría
        pass

    def start_exams(self):
        # Aquí puedes poner el código para iniciar la sección de exámenes
        pass

    def open_camera(self):
        # Abrir la cámara usando OpenCV
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow("Cámara", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def screenshot(self, *args):
        from mss import mss
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        box = {
            "top": self.winfo_y(),
            "left": self.winfo_x(),
            "width": self.winfo_width(),
            "height": self.winfo_height()
        }
        screenshot = mss().grab(box)
        screenshot = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        screenshot.save("screenshots/{}.png".format(ttk.Style(self).theme_use()))

    def screenshot_themes(self, *args):
        from time import sleep
        for theme in THEMES:
            self.set_theme(theme)
            self.update()
            sleep(0.05)
            self.screenshot()

app = SignLanguageLearningApp()
app.mainloop()