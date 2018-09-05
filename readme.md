# Introduction
SiegeOCR was initially developed as a test project to see if I could successfully extrapolate data from what was being displayed on my screen. After viewing [a video by Michael Reeves](https://www.youtube.com/watch?v=D75ZuaSR8nQ) where he used OCR to view his current health in Fortnite (and have an electronic airsoft gun shoot him if his health dropped), I decided to turn *the initial version of what would become SiegeOCR* into SiegeOCR.

## How it works
Using OpenCV to view our screen, we check that what is displayed matches our comparison data - in the case of SiegeOCR, we check if what is displayed matches [the timer that is displayed when a bomb is being defused.](timer.png)
We calculate the difference between the images using SSIM (Structural Similarity Index), and from this we get a score.

Also, yes, I know. OCR isn't used at all in this program. It just sounded super catchy.

## Installation
It's recommended to create a virtual environment for this program.
Otherwise:

- Uses Python 3 (written with 3.6)
- `pip install -r requirements.txt`
- `python run.py`

If you use a different resolution and aspect ratio that isn't 1920x1080 and 16:9, you will need to change the values of `area` in `run.py`. I used ShareX to do this. If you use that resolution and aspect ratio, you're good to go as is.