import cv2
import numpy
import mss


def main():
    # Define our capture area
    area = {"left": 937, "top": 73, "width": 47, "height": 47}

    # Now grab that area
    with mss.mss() as sct:
        while True:
            capture = numpy.array(sct.grab(area))

            # Display our capture. Not really necessary but
            # its nice to know what the program sees.
            cv2.imshow("Siege capture", capture)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    main()
