from PIL import Image, ImageDraw, ImageFont


def create_sample_image():
    width, height = 800, 1600
    color = (200, 200, 200)
    img = Image.new("RGB", (width, height), color=color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)

    sample_text = "Sample Text"
    return


def main():
    create_sample_image()


if __name__ == "__main__":
    main()
