import qrcode
import cv2
import os
from PIL import Image

def create_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code as an image file
    img.save(filename)
    print(f"✅ QR Code saved as '{filename}'")

    # Open and show the saved image
    saved_img = Image.open(filename)
    saved_img.show()

def decode_qr_code(filename):
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found. Please check the filename or path.")
        return

    img = cv2.imread(filename)
    if img is None:
        print(f"❌ Unable to read image from '{filename}'. Make sure it's a valid image file.")
        return

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if bbox is not None and data:
        print(f"✅ Decoded data: {data}")
    else:
        print("❌ No QR Code found or could not decode.")

if __name__ == "__main__":
    while True:
        choice = input("\nSelect an option:\n1. Generate QR Code\n2. Decode QR Code\n3. Exit\nEnter choice (1/2/3): ")

        if choice == '1':
            data = input("Enter the data to encode: ")
            filename = input("Enter filename to save (example: mycode.png): ")
            # Automatically add .png if the user forgets
            if not (filename.endswith('.png') or filename.endswith('.jpg')):
                filename += '.png'
            create_qr_code(data, filename)

        elif choice == '2':
            filename = input("Enter QR Code image filename to decode: ")
            decode_qr_code(filename)

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid input. Please choose 1, 2, or 3.")
