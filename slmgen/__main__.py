try:
    from .slmwindow import main
except Exception as e:
    import sys

    if "QtError" in e.__class__.__name__:
        print(f"{e}...")
        print("To use the GUI, please install either pyqt or pyside2.")
        print("for example:\n\n  $ conda install pyqt\n")
    sys.exit()


if __name__ == "__main__":

    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    main()
