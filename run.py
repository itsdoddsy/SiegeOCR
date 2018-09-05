import cv2
import numpy
import mss
from skimage.measure import compare_ssim as ssim


def main():
    # Define our capture area
    area = {"left": 937, "top": 73, "width": 47, "height": 47}

    # Open our timer picture to compare to
    timer = cv2.imread('timer.png')
    # Convert it to a greyscale image
    timer = cv2.cvtColor(timer, cv2.COLOR_BGR2GRAY)

    # Now grab that area for the duration of the program
    with mss.mss() as sct:
        while True:
            capture = numpy.array(sct.grab(area))
            # Convert it to a greyscale image
            capture = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)

            # Display our capture. Not really necessary but
            # its nice to know what the program sees.
            cv2.imshow("Siege capture", capture)
            print("SSIM: {:.2f}".format(ssim(capture, timer)))

            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    main()
