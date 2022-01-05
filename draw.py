from PIL import Image, ImageDraw, ImageFont
import textwrap

def draw_meme(flag_file: str, text: str) -> str:
    """Draws meme and returns file where it saved it
    """
    bg = Image.open('template.png')
    flag = Image.open(flag_file)
    maxwidth = 81
    maxheight = 60
    flag.thumbnail((maxwidth, maxheight))
    _, h = flag.size
    flag_rotated = flag.rotate(-45, expand=True)
    bg.paste(flag_rotated, (971 - int(0.707 * h), 102))
    drawI = ImageDraw.Draw(bg)
    text_lines = textwrap.fill(text, 50).split('\n')
    x0 = 279
    y0 = 438
    hl = 40
    font = ImageFont.truetype('roboto.ttf', 28)
    for i, line in enumerate(text_lines):
        drawI.text((x0, y0 + i * hl), line, font=font)
    fn = f'tmp/ready-{flag_file[4:]}'
    bg = bg.convert('RGB')
    bg.save(fn)
    return fn

