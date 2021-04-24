from tkinter import ttk, messagebox
from tkinter import *
import socketio
import json

sio = socketio.Client()

class Window:

    def __init__(self, window, socket):
        self.socket = socket

        self.window = window
        self.window.title('Chat Application')
        self.window.geometry("375x667")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.list = Listbox(self.window)
        self.list.grid(row = 0, column = 0)

        self.input = Entry(self.window)
        self.input.grid(row=1, column=0)

        self.button = Button(self.window, text="send", command=self.send)
        self.button.grid(row=1, column=1)

        try:
            #  self.socket.connect("http://localhost:3000")
            self.socket.connect("https://chat-python-socket.herokuapp.com/")

            @sio.event
            def new_message(data):
                msg = json.loads(data)
                self.new_message(msg['msg'])

        except Exception as e:
            messagebox.showinfo(message = "No se pudo conectar al servidor", title = "ERROR")
            self.window.destroy()

    def new_message(self, msg):
        self.list.insert(END, msg)

    def send(self):
        self.socket.emit('message', {"msg": self.input.get()})

    def on_close(self):
        self.socket.disconnect()
        self.window.destroy()

if __name__ == '__main__':
    window = Tk()
    applications = Window(window, sio)
    window.mainloop()

