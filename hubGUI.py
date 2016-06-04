import tkinter as tk
import hub


class HubGUI:
    def __init__(self, master):
        self.master = master
        self.master.title = 'Copy & Paste GUI'

        # Paste stuff
        self.paste_button = tk.Button(master, text='Save to database', command=self.add_entry)
        self.paste_button.grid(row=0, column=0, sticky=tk.E, padx=2)

        self.save_entry = tk.Entry(master)
        self.save_entry.bind("<Return>", self.add_entry)  # when using bind the 2nd parameter in a method must be 'event'
        self.save_entry.grid(row=0, column=1, sticky=tk.W)

        # Get entry stuff
        self.get_button = tk.Button(master, text='Get from database', command=self.get_entry)
        self.get_button.grid(row=1, column=0, sticky=tk.E, padx=2)

        self.get_name = tk.Entry(master)
        self.get_name.bind("<Return>", self.get_entry)
        self.get_name.grid(row=1, column=1, sticky=tk.W)

        # Remove entry stuff
        self.remove_button = tk.Button(master, text='Remove from database', command=self.remove)
        self.remove_button.grid(row=2, column=0, sticky=tk.E, padx=2)

        self.remove_button_entry = tk.Entry(master)
        self.remove_button_entry.bind("<Return>", self.remove)
        self.remove_button_entry.grid(row=2, column=1, sticky=tk.W)

        # Bottom label
        self.var = tk.StringVar()
        self.var.set('Choose an action')
        self.bottom_label = tk.Label(master, text='Choose an action', textvariable=self.var)
        self.bottom_label.grid(row=4, columnspan=2)

        # List of items in database
        self.list_button = tk.Button(master, text='Copy database', command=self.list)
        self.list_button.grid(row=3, columnspan=2)

    def remove(self, event=None):
        msg = hub.delete_entry(self.remove_button_entry.get())
        self.var.set(msg)

    def add_entry(self, event=None):
        msg = hub.add_entry(self.save_entry.get())
        self.var.set(msg)

    def get_entry(self, event=None):
        msg = hub.get_entry(self.get_name.get())
        self.var.set(msg)

    def list(self):
        msg = hub.list_entries()
        self.var.set(msg)


def start():
    root = tk.Tk()
    HubGUI(root)
    root.tk.mainloop()


