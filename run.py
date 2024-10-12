from PIL import Image, ImageDraw, ImageFont


def create_sample_image():
    width, height = 800, 1600
    color = (200, 200, 200)
    img = Image.new("RGB", (width, height), color=color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)

    sample_text = "Sample Text"
    text_width, text_height = draw.textsize(sample_text, font=font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), sample_text, fill=(0, 0, 0), font=font)

    return img


def main():
    create_sample_image()


if __name__ == "__main__":
    main()
