import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog, colorchooser, StringVar
from PIL import ImageTk

def generate_qr():
    website_link = url_var.get()
    if not website_link:
        status_label.config(text="Enter a valid URL!")
        return

    fill_color = fill_color_var.get()
    back_color = back_color_var.get()
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    if filename:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(website_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        status_label.config(text="QR Code saved successfully!")

def choose_color(var):
    color = colorchooser.askcolor(title="Select Color")[1]
    if color:
        var.set(color)

# GUI Setup
root = Tk()
root.title("QR Code Generator")

Label(root, text="Enter URL:").grid(row=0, column=0)
url_var = StringVar()
Entry(root, textvariable=url_var, width=40).grid(row=0, column=1)

Label(root, text="Foreground Color:").grid(row=1, column=0)
fill_color_var = StringVar(value="black")
Button(root, text="Choose", command=lambda: choose_color(fill_color_var)).grid(row=1, column=1)

Label(root, text="Background Color:").grid(row=2, column=0)
back_color_var = StringVar(value="white")
Button(root, text="Choose", command=lambda: choose_color(back_color_var)).grid(row=2, column=1)

Button(root, text="Generate QR Code", command=generate_qr).grid(row=3, column=0, columnspan=2, pady=10)

status_label = Label(root, text="", fg="green")
status_label.grid(row=4, column=0, columnspan=2)

root.mainloop()