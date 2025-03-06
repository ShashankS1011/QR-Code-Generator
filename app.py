import qrcode
import streamlit as st
from PIL import Image
from io import BytesIO

st.title("QR Code Generator")

# Input field for URL
website_link = st.text_input("Enter URL:")

# Color pickers for QR customization
fill_color = st.color_picker("Choose Foreground Color", "#000000")
back_color = st.color_picker("Choose Background Color", "#FFFFFF")

# Button to generate QR code
if st.button("Generate QR Code"):
    if website_link:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(website_link)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Save QR code in memory
        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        st.image(img, caption="Your QR Code")

        # Provide download link
        st.download_button(
            label="Download QR Code",
            data=img_buffer.getvalue(),
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.error("Please enter a valid URL!")