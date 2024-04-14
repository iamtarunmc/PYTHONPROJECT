import tkinter as tk
from tkinter import ttk, messagebox
class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.contacts = {}
        self.create_widgets()
    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", foreground="blue", background="lightblue")

        self.label_name = ttk.Label(self.master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.name_entry = ttk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone = ttk.Label(self.master, text="Phone:")
        self.label_phone.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.phone_entry = ttk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = ttk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.delete_button = ttk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.search_button = ttk.Button(self.master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.update_button = ttk.Button(self.master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name.strip() == "" or phone.strip() == "":
            messagebox.showerror("Error", "Please enter name and phone number.")
            return
        self.contacts[name] = phone
        messagebox.showinfo("Success", "Contact added successfully.")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def delete_contact(self):
        name = self.name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Please enter a name to delete.")
            return
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def search_contact(self):
        name = self.name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Please enter a name to search.")
            return
        if name in self.contacts:
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {self.contacts[name]}")
        else:
            messagebox.showerror("Error", "Contact not found.")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Please enter a name to update.")
            return
        if name in self.contacts:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
if __name__ == "__main__":
    main()