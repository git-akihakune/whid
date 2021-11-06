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

        _colours.prYellow("Starting screenshot session...")
        for i in range(0, duration, frequency):
            whid.takeScreenshot(
                f"{self.WORK_DIR}/{i // frequency}.png",
                screenLength,
                screenWidth,
            )
            if verbose:
                print(f"{i}/{duration}s passed, {(duration - i) // frequency} frames left...", end="\r")
            time.sleep(frequency)

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

        image_folder = self.WORK_DIR

        image_files = [
            os.path.join(image_folder, img)
            for img in sorted(os.listdir(image_folder))
            if img.endswith(".png")
        ]
        video = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
            image_files, fps=fps
        )
        video.write_videofile(os.path.join(saveTo, videoName))

        if verbose:
            _colours.prGreen(f"Video created at {videoName}")

    def cleanUp(self) -> None:
        import shutil
        shutil.rmtree(self.WORK_DIR)
        _colours.prPurple(f"Deleted {self.WORK_DIR}")



class _colours:
    """Colourful printing for terminal"""

    @staticmethod
    def prRed(skk):
        print("\033[91m {}\033[00m".format(skk))

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
        capture.startScreenshotSession(
            frequency,
            duration,
            screenLength,
            screenWidth,
            verbose,
        )
        capture.videoMaking(fps, videoName, saveTo, verbose)
        if autoCleanUp:
            capture.cleanUp()
