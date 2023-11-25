import tkinter as tk

class Model:
    def __init__(self):
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

class View(tk.Tk):
    def __init__(self, adapter):
        super().__init__()
        self.title("MVA Example")
        self._adapter = adapter
        self.label = tk.Label(self, text="Value:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Update", command=self.update_data)
        self.button.pack()

    def update_data(self):
        data = int(self.entry.get())
        self._adapter.update_data(data)

class Adapter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_data(self, data):
        self.model.data = data
        self.view.label.config(text="Value: " + str(self.model.data))

if __name__ == "__main__":
    model = Model()
    adapter = Adapter(model, None)
    view = View(adapter)
    adapter.view = view
    view.geometry("300x150")
    view.mainloop()
