import cv2, mss, os, numpy as np
from skimage.measure import compare_ssim as ssim


def clear():
    # Don't do operating system check (clear/cls)
    # because Siege only runs natively on Windows
    os.system('cls')

def main():
    # Define our capture area
    area = {"left": 937, "top": 73, "width": 47, "height": 47}

    # Get current directory of the script.
    # Only needed because my IDE doesn't like relative directories.
    # Works fine in a terminal without this, but it works with it too.
    _CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    # Open our timer picture to compare to
    timer = cv2.imread(_CURRENT_DIR + '\\timer.png')
    # Convert it to a greyscale image
    timer = cv2.cvtColor(timer, cv2.COLOR_BGR2GRAY)

    # Now grab that area for the duration of the program
    with mss.mss() as sct:
        while True:
            capture = np.array(sct.grab(area))
            # Convert it to a greyscale image
            capture = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)

            # Display our capture. Not really necessary but
            # its nice to know what the program sees.
            # Disable it by putting a "#" at the start.
            # Just means one less window open!
            cv2.imshow("Siege capture", capture)

            # Output our SSIM result
            print("SSIM: {:.1f}".format(ssim(capture, timer) * 100))
            # Only show one SSIM result so we don't get a spammed console.
            clear()

            # Set a "quit" bind in our OpenCV window.
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    main()
