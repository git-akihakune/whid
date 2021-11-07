#!/usr/bin/env python3

import pyautogui


class whid:
    def __init__(self) -> None:
        import tempfile

        self.WORK_DIR: str = tempfile.mkdtemp()

    @staticmethod
    def takeScreenshot(savingTo: str, screenLength, screenWidth) -> None:
        pyautogui.screenshot(savingTo, region=(0, 0, screenLength, screenWidth))

    def startScreenshotSession(
        self,
        frequency: int = 5,
        duration: int = 3600,
        screenLength: int = 1920,
        screenWidth: int = 1080,
        verbose: bool = False,
    ) -> None:
        """Main function to get screenshots"""
        import time
        from tqdm import tqdm

        if verbose:
            print(f"Working directory: {self.WORK_DIR}")
        _colours.prYellow("Starting screenshot session...")

        # Set program duration:
        if verbose:
            RANGE = tqdm(range(0, duration, frequency))
        else:
            RANGE = range(0, duration, frequency)

        for i in RANGE:
            imagePath = f"{self.WORK_DIR}/{i // frequency}.png"
            whid.takeScreenshot(
                imagePath, screenLength, screenWidth
            )
            RANGE.set_description(f"{i}/{duration}s, {(duration - i) // frequency} left")
            time.sleep(frequency)
        RANGE.close()

        if verbose:
            _colours.prLightPurple(f"Saved screenshots to {self.WORK_DIR}")
            _colours.prGreen("Recording session completed.\n")

    def videoMaking(
        self,
        fps: int = 4,
        videoName: str = "what-i-have-done.mp4",
        saveTo: str = ".",
        verbose: bool = False,
    ) -> None:
        """Create a video from screenshots"""
        import os
        import moviepy.video.io.ImageSequenceClip

        imageFolder = self.WORK_DIR
        videoPath = os.path.join(saveTo, videoName)

        imageFiles = [
            os.path.join(imageFolder, img)
            for img in sorted(os.listdir(imageFolder))
            if img.endswith(".png")
        ]
        video = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
            imageFiles, fps=fps
        )
        video.write_videofile(videoPath)

        if verbose:
            _colours.prGreen(f"Video created at {videoPath}")

    def cleanUp(self) -> None:
        import shutil
        shutil.rmtree(self.WORK_DIR)
        _colours.prPurple(f"Deleted {self.WORK_DIR}")



class _colours:
    """Colourful printing for terminal"""

    @staticmethod
    def prRed(skk):
        print("\033[91m{}\033[00m".format(skk))

    @staticmethod
    def prGreen(skk):
        print("\033[92m{}\033[00m".format(skk))

    @staticmethod
    def prYellow(skk):
        print("\033[93m{}\033[00m".format(skk))

    @staticmethod
    def prLightPurple(skk):
        print("\033[94m{}\033[00m".format(skk))

    @staticmethod
    def prPurple(skk):
        print("\033[95m{}\033[00m".format(skk))

    @staticmethod
    def prCyan(skk):
        print("\033[96m {}\033[00m".format(skk))

    @staticmethod
    def prLightGray(skk):
        print("\033[97m{}\033[00m".format(skk))

    @staticmethod
    def prBlack(skk):
        print("\033[98m {}\033[00m".format(skk))


class TUI:
    def __init__(self, banner: bool = True) -> None:
        if banner:
            self.banner()

    def banner(self):
        """Print 'whid' in ascii art"""
        _colours.prCyan(
            r"""                 
 _ _ _ _____ _____ ____  
| | | |  |  |     |    \ 
| | | |     |-   -|  |  |
|_____|__|__|_____|____/ 
                                   
"""
        )
        _colours.prLightPurple(
            "What have I done? How have I spent my past hour on computer?"
        )
        _colours.prLightGray(f"@akihakune\n")

    def run(
        self,
        screenLength: int = 1920,
        screenWidth: int = 1080,
        duration: int = 3600,
        frequency: int = 5,
        fps: int = 4,
        videoName: str = "what-i-have-done.mp4",
        saveTo: str = ".",
        verbose: bool = False,
        autoCleanUp: bool = True,
    ):
        """Execute all program"""

        capture = whid()

        try:
            capture.startScreenshotSession(
                frequency,
                duration,
                screenLength,
                screenWidth,
                verbose,
            )
        except KeyboardInterrupt:
            _colours.prRed("Record session interrupted.")

            if input("Continue generating video? [y/n] ") in ["y", "Y", "yes", "Yes"]:
                capture.videoMaking(
                    fps, videoName, saveTo, verbose
                )
                _colours.prGreen("Video generated successfully.")

            if autoCleanUp:
                capture.cleanUp()
            exit(0)

        capture.videoMaking(fps, videoName, saveTo, verbose)
        if autoCleanUp:
            capture.cleanUp()

        if verbose:
            from plyer import notification
            notification.notify(
                app_name="whid",
                title="WHID notice",
                message="Recording session completed!",
                timeout=5,
            )