import tkinter as tk
from tkinter import messagebox
import pyperclip
import os


class TextAreaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Persisted Clipboard")

        self.text_areas_left = []
        self.text_areas_right = []
        self.create_text_areas()
        self.load_contents()

        self.save_all_button = tk.Button(master, text="Save All", command=self.save_all)
        self.save_all_button.grid(row=6, column=0, columnspan=3, pady=10)
        if not os.path.exists("content"):
            os.mkdir("content")

    def create_text_areas(self):
        for i in range(6):
            # Left text areas
            text_area_left = tk.Text(self.master, height=5, width=40)
            text_area_left.grid(row=i, column=0, padx=10, pady=5)
            self.text_areas_left.append(text_area_left)

            save_button_left = tk.Button(
                self.master, text="Save", command=lambda idx=i: self.save(idx, "left")
            )
            save_button_left.grid(row=i, column=1)

            copy_button_left = tk.Button(
                self.master,
                text="Copy to Clipboard",
                command=lambda idx=i: self.copy_to_clipboard(idx, "left"),
            )
            copy_button_left.grid(row=i, column=2)

            # Right text areas
            text_area_right = tk.Text(self.master, height=5, width=40)
            text_area_right.grid(row=i, column=3, padx=10, pady=5)
            self.text_areas_right.append(text_area_right)

            save_button_right = tk.Button(
                self.master, text="Save", command=lambda idx=i: self.save(idx, "right")
            )
            save_button_right.grid(row=i, column=4)

            copy_button_right = tk.Button(
                self.master,
                text="Copy to Clipboard",
                command=lambda idx=i: self.copy_to_clipboard(idx, "right"),
            )
            copy_button_right.grid(row=i, column=5)

    def load_contents(self):
        for i in range(6):
            # Load left text areas
            left_file = f"content/file{i}.txt"
            if os.path.exists(left_file):
                with open(left_file, "r") as file:
                    content = file.read()
                    self.text_areas_left[i].insert(tk.END, content)

            # Load right text areas
            right_file = f"content/file{i + 6}.txt"
            if os.path.exists(right_file):
                with open(right_file, "r") as file:
                    content = file.read()
                    self.text_areas_right[i].insert(tk.END, content)

    def save(self, index, side):
        if side == "left":
            content = self.text_areas_left[index].get("1.0", tk.END).strip()
            filename = f"content/file{index}.txt"
        else:
            content = self.text_areas_right[index].get("1.0", tk.END).strip()
            filename = f"content/file{index + 6}.txt"

        if content:
            with open(filename, "w") as file:
                file.write(content)
            messagebox.showinfo("Success", f"Content saved to {filename}")
        else:
            messagebox.showwarning("Warning", "Text area is empty!")

    def copy_to_clipboard(self, index, side):
        if side == "left":
            content = self.text_areas_left[index].get("1.0", tk.END).strip()
        else:
            content = self.text_areas_right[index].get("1.0", tk.END).strip()

        if content:
            pyperclip.copy(content)
            messagebox.showinfo("Success", "Content copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "Text area is empty!")

    def save_all(self):
        for i in range(6):
            # Save left text areas
            content_left = self.text_areas_left[i].get("1.0", tk.END).strip()
            if content_left:
                with open(f"content/file{i}.txt", "w") as file:
                    file.write(content_left)

            # Save right text areas
            content_right = self.text_areas_right[i].get("1.0", tk.END).strip()
            if content_right:
                with open(f"content/file{i + 6}.txt", "w") as file:
                    file.write(content_right)

        messagebox.showinfo("Success", "All contents saved!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextAreaApp(root)
    root.mainloop()
