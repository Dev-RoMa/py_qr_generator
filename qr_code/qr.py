import qrcode

# Get the website URL from the user
user_input = input("Enter the website URL: ")

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(user_input)
qr.make(fit=True)

# Create an image from the QR code instance
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_img.save("user_qrcode.png")
print("QR code saved as 'user_qrcode.png'")
