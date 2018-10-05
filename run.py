import cv2, mss, os, numpy as np
from skimage.measure import compare_ssim as ssim


def clear():
    # Don't do operating system check (clear/cls)
    # because Siege only runs natively on Windows
    os.system('cls')

def greyscale_img(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def main():
    # Define our capture area
    timer_area = {"left": 937, "top": 73, "width": 47, "height": 47}
    wl_area = {"left": 623, "top": 233, "width": 609, "height": 331}

    # Get current directory of the script.
    # Only needed because my IDE doesn't like relative directories.
    # Works fine in a terminal without this, but it works with it too.
    _CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    # Initialise last output
    last_output = None

    # Open our comparison picture and greyscale it.
    timer_img = greyscale_img(cv2.imread(_CURRENT_DIR + '\\image_checks\\timer.png'))

    # Now grab that area for the duration of the program
    with mss.mss() as sct:
        while True:
            # Also convert it to a greyscale image
            grey_timer_area = greyscale_img(np.array(sct.grab(timer_area)))
            grey_wl_area = greyscale_img(np.array(sct.grab(wl_area)))

            # Display our captures. Not really necessary but
            # its nice to know what the program sees.
            # Disable it by putting a "#" at the start.
            # Just means one less window open!
            cv2.imshow("Text capture", grey_wl_area)

            # Doing some funky magic because the timer area is
            # so small that it's hard to move around without
            # right clicking the top right and hitting "move".

            # This will enable resize controls on the Timer window.
            cv2.namedWindow("Timer capture", cv2.WINDOW_NORMAL)

            # Uncommenting this will make it always open at the
            # specified size. Leave it commented if you want,
            # I'm not the boss of you.
            #cv2.resizeWindow("Timer capture", 200,47)

            cv2.imshow("Timer capture", grey_timer_area)
            
            # Now to calculate our SSIM!
            # We're multiplying it by 100 so it's a bit of a nicer number,
            # rather than a bunch of decimals.
            output = "SSIM: {:.1f}".format(ssim(grey_timer_area, timer_img) * 100)
            if output != last_output:
                # Clear the console for the next SSIM to show.
                clear()
                # Output our SSIM result
                print(output)
            last_output = output

            # Set a "quit" bind in our OpenCV window.
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    main()
