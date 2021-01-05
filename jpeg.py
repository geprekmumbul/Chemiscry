from PIL import Image, ImageDraw, ImageFont

# Font yang digunakan
fontname = "font.ttf"
fontsize =100
font = ImageFont.truetype(fontname, fontsize)

def print_text(teks):
    # Setting ukuran
    nama = teks
    width = len(nama[0]) * 55
    height = len(nama) * 100

    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    for i in range(len(nama)):
        nama[i] = nama[i].translate(sub)


    # Text to image
    img = Image.new('RGB', (width, height), "white")
    d = ImageDraw.Draw(img)

    for i in range(len(nama)):
        d.text((0, 100* i), nama[i], "black", font=font)
    d.rectangle((0, 0, width, height))

    # Lokasi save gambar
    img.save("C:/Users/Admin/Desktop/Alkana/image.jpeg")

