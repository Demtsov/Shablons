import tkinter as tk
from tkinter import ttk


class Model:
    def __init__(self):
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


class ViewModel:
    def __init__(self, model):
        self.model = model
        self.data = tk.StringVar()
        self.data.set(str(model.data))

    def update_data(self, value):
        self.model.data = int(value)
        self.data.set(str(self.model.data))


class View(tk.Tk):
    def __init__(self, view_model):
        super().__init__()
        self.title("MVVM Example")

        self.view_model = view_model
        self.label = ttk.Label(self, text="Value:")
        self.label.pack()

        self.entry = ttk.Entry(self, textvariable=self.view_model.data)
        self.entry.pack()

        self.button = ttk.Button(self, text="Update", command=self.update_data)
        self.button.pack()

    def update_data(self):
        self.view_model.update_data(self.view_model.data.get())


if __name__ == "__main__":
    model = Model()
    view_model = ViewModel(model)
    app = View(view_model)
    app.geometry("300x150")
    app.mainloop()
