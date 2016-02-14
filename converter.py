from PIL import Image
from PIL import features
import os

def convert(inputFile, outputFile):
    im = Image.open(inputFile).convert("RGB")
    im.save(outputFile, "jpeg")

    print('Converted {} to {}'.format(inputFile, outputFile))

def main():
    for f in os.listdir('.'):
        if f.upper().endswith('.WEBP'):
            outputFile = f[:-5] + '.jpg'

            if os.path.exists(outputFile):
                print('Warning! {} not converted, because {} already exsits'.format(f, outputFile))
            else:
                convert(f, outputFile)

if __name__ == '__main__':
    print ('WEBP:', features.check_module('webp'))
    main()
