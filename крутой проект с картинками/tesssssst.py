from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

top_text = str(input("Напишите верхний текст: " ))
bottom_text = str(input("Напишите нижний текст: "))

print(top_text, bottom_text)


print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input())

if image_number == 1:
  file = "Кот в ресторане.png"
elif image_number == 2:
  file = "Кот в очках.png"
else:
  print("тебе сказали '1 или 2'")



image = Image.open(file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=80)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="black")

image.save("new_name.png")