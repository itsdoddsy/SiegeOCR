import numpy as np
from PIL import ImageGrab
import cv2

def main():
    while True:

        """
        The X and Y (and X/Y offsets) are accurate for Siege running at
        1920x1080 resolution, on a 16:9 aspect ratio. These numbers may
        need to be changed depending on how you run your game.
        """
        x = 937
        y = 73

        """
        In normal aspect ratios, the bomb timer area is a square. In case
        you're using a different aspect ratio that is stretched, you should
        change these values to be different. i.e:
        x_offset = value1
        y_offset = value2
        """
        x_offset = y_offset = 47

        siege = ImageGrab.grab(bbox=(x, y, x+x_offset, y+y_offset)).convert('L')

        siege_np = np.array(siege)
        cv2.imshow('Window', siege_np)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()