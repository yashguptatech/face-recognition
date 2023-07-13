from tkinter import *
import csv
import os
from PIL import ImageTk, Image

def image():
    def btn_clicked():
        name = entry0.get()
        contact_no = entry1.get()
        addhar_card = entry2.get()

        # Open the CSV file in append mode
        with open('Book1.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            # Check if the file is empty and write the headers if necessary
            if file.tell() == 0:
                writer.writerow(['index', 'name', 'Phone no', 'Adhaar'])

            # Get the current number of rows in the CSV file
            with open('Book1.csv', 'r') as csvfile:
                row_count = sum(1 for row in csvfile)

            # Write the data to the CSV file with an incremented index value
            writer.writerow([row_count - 1, name, contact_no, addhar_card])

        print("Data saved to CSV file")

    window = Tk()

    window.geometry("839x494")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=494,
        width=839,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=9, y=5)

    # Load background image from the build folder
    background_img_path = os.path.join("build", "background.png")
    background_img = ImageTk.PhotoImage(Image.open(background_img_path))
    background = canvas.create_image(419, 247, image=background_img)

    entry0_bg = canvas.create_image(430, 150)

    entry0 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0
    )
    entry0.place(x=430, y=150, width=391, height=40)

    # Rest of the code for entry1, entry2, entry3, and button goes here

    window.resizable(True, True)
    window.mainloop()

image()
