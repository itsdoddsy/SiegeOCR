# Introduction
SiegeOCR was initially developed as a test project to see if I could successfully extrapolate data from what was being displayed on my screen. After viewing [a video by Michael Reeves](https://www.youtube.com/watch?v=D75ZuaSR8nQ) where he used OCR to view his current health in Fortnite (and have an electronic airsoft gun shoot him if his health dropped), I decided to turn *the initial version of what would become SiegeOCR* into SiegeOCR.

## How it works
Using OpenCV to view our screen, we check that what is displayed matches our comparison data - in the case of SiegeOCR, we check if what is displayed matches [the timer that is displayed when a bomb is being defused.](timer.png)
We calculate the difference between the images using SSIM (Structural Similarity Index), and from this we get a score.