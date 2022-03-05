from io import BytesIO

from PIL import Image


def image_convert(read_image=None,
                  format_type: str = 'webp',
                  fname: str = "convert"):
    if read_image:
        with Image.open(read_image) as im:
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
