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
    def __init__(self, presenter):
        super().__init__()
        self.title("MVP Example")

        self.presenter = presenter

        self.label = tk.Label(self, text="Value:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Update", command=self.update_data)
        self.button.pack()

    def update_data(self):
        data = int(self.entry.get())
        self.presenter.update_data(data)

class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_data(self, data):
        self.model.data = data
        self.view.label.config(text="Value: " + str(self.model.data))

if __name__ == "__main__":
    model = Model()
    presenter = Presenter(model, None)
    view = View(presenter)
    presenter.view = view
    view.geometry("300x150")
    view.mainloop()
