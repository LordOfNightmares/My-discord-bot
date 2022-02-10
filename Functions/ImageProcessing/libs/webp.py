import re
from io import BytesIO

from PIL import Image

def get_url_images_in_text(text):
    '''finds image urls'''
    return re.findall(r'(https?:\/\/.*\.(?:png|jpg|webp|jiff|jpeg))', text)


def image_convert(image_bytes,
                  format_type: str = 'webp',
                  fname: str = "convert"):
    with Image.open(image_bytes) as im:
        # prepare the stream to save this image into
        final_buffer = BytesIO()
        try:
            # save into the stream, using png format.
            im.save(final_buffer, format_type)
        except Exception as e:
            if 'RGBA' in str(e.__cause__):
                im = im.convert('RGB')
                # save into the stream, using png format.
                im.save(final_buffer, format_type)
            else:
                raise e
                # seek back to the start of the stream
    final_buffer.seek(0)
    return final_buffer, '.'.join((fname, format_type))
