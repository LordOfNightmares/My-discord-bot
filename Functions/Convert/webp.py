from PIL import Image


def convert(image_path: str,
            color_vals: str = 'RGBA',
            form: str = 'webp'):
    im = Image.open(image_path).convert(color_vals)  # .transpose(Image.ROTATE_90)
    # im.show()
    im.save(image_path.rsplit('.', 1)[0] + "." + form, form)


convert(r"C:\Users\TruePc\Desktop\Cute-Dream-Asian-Girl-4K-Ultra-HD-Mobile-Wallpaper-283x503(Photo)(auto_scale)(Level3)(tta)(height 2160)(16bit).png")

