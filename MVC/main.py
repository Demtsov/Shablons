import tkinter as tk

class Model:
    def __init__(self):
        self._data = 0

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
# В классе модель содержит методы которые работают с значениями
class View(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Value:")
        self.label.pack()
        self._value = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self._value)
        self.entry.pack()
        self.button = tk.Button(self, text="Update", command=self.update_data)
        self.button.pack()

    def update_data(self):
        self.controller.update_data(self._value.get())
#В классе представление происходит настройка графического интерфейса

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

    def update_data(self, data):
        self.model.set_data(data)
        self.view.label.config(text="Value: " + self.model.get_data())
#В классе контроллер происходит взаимодействие представления и модели

def main():
    root = tk.Tk()
    app = Controller(root)
    app.view.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
