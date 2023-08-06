import logging

import click
from PIL import Image

logging.basicConfig(format='%(asctime)s: %(message)s')


@click.command()
@click.option('-i', '--input', 'in_file', type=click.File('rb'), help="Input, Filename", required=True)
@click.option('-o', '--output', 'out_file', type=click.Path(), help="Output, Filename", required=True)
@click.option('-b', '--box', 'box', type=(int, int, int, int), help="Box to crop", required=True)
@click.option('-q', '--quality', 'quality', type=click.IntRange(1, 100), help="Quality (1-100)", default=100)
def crop(in_file, out_file, box, quality):
    img = Image.open(in_file)
    # crop
    # box = [0, 500, 3280, 2464]
    img = img.crop(box)
    # save
    img.save(out_file, quality=quality)


if __name__ == '__main__':
    crop()
