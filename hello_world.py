import tkinter as tk
from tkinter import messagebox

# Erstellt das Hauptfenster
root = tk.Tk()
root.withdraw()

# zeigt ein kleines Pop-up-Fenster mit der Nachricht an
messagebox.showinfo("Hallo Welt", "Hallo Welt! Klicken sie auf OK zum Beenden.")

# Das Fenster bleibt sichtbar, bis der Benutzer auf Ok klickt
root.destroy()