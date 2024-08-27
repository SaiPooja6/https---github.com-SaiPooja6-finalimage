"""
This is a boilerplate pipeline 'grayscaleimage'
generated using Kedro 0.19.8
"""
from PIL import Image, ImageDraw, ImageFont
def resize_image(image: Image.Image) -> Image.Image:
    image=image.resize((84, 84))
    return image
def grayscale_image(image:Image.Image)->Image.Image:
    image = image.convert("L")
    return image
def add_text(image:Image.Image)->Image.Image:
    draw = ImageDraw.Draw(image)
    #font = ImageFont.load_default()
    position = (10,160)
    text = "I am a grayscaled image in 84*84 size"   
    font_size = 16
    draw.text(position, text, fill="green")  
    return image 
   
