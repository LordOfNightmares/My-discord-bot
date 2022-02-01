from PIL import Image


def convert(image_path: str,
            color_vals: str = 'RGBA',
            form: str = 'webp'):
    im = Image.open(image_path)#.convert(color_vals)  # .transpose(Image.ROTATE_90)
    # im.show()
    im.save(image_path.rsplit('.', 1)[0] + "." + form, form)


path = r"C:\Users\TruePc\Desktop\dump\self\WP_20220124_14_50_44_Pro.jpg"
convert(path)
