import argparse
from .utils import TUI
from .__init__ import __version__

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='WHID arguments', prog='python -m whid')
    parser.add_argument('-V', '--version', action='version', version=f'{__version__}')
    parser.add_argument('-l', '--length', default=1920, help="Set screen's length")
    parser.add_argument('-w', '--width', default=1080, help="Set screen's width")
    parser.add_argument('-d', '--duration', default=3600, help="Set total record time, by second")
    parser.add_argument('-f', '--frequency', default=5, help="Set time interval between screenshots, by second")
    parser.add_argument('-F', '--fps', default=4, help="FPS of the final video")
    parser.add_argument('-n', '--name', default='what-i-have-done.mp4', help="Name of the final video")
    parser.add_argument('-s', '--save', default='.', help="Saving directory")
    parser.add_argument('-v', '--verbose', default="True", help="Set verbosity of the program, True/False")
    parser.add_argument('-c', '--clean', default="True", help="Automatically clean up temporary images, True/False")
    args = parser.parse_args()

    # Get arguments
    screenLength = args.length
    screenWidth = args.width
    duration = int(args.duration)
    frequency = int(args.frequency)
    fps = int(args.fps)
    videoName = args.name
    saveTo = args.save
    verbose = (args.verbose in ['True', 'true', '1', 'yes', 'y'])
    autoClean = (args.clean in ['True', 'true', '1', 'yes', 'y'])

    # Run the TUI
    capture = TUI()
    capture.run(screenLength,
        screenWidth,
        duration,
        frequency,
        fps,
        videoName,
        saveTo,
        verbose,
        autoClean,
    )

if __name__ == '__main__':
    main()