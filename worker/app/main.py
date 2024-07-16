import cv2
import numpy as np


def _main():
    import sys
    args = sys.argv
    if len(args) == 1:
        print('You need input file input')
        sys.exit(1)

    file_path = args[1]
    print(f'your file path is {file_path}')
    img = cv2.imread(filename=file_path)
    if img is None:
        print('file cannot read. Please enter someting either')
        sys.exit(1)

    print('image open')

    try:
        new_image = pixelize(img)
        _show_original_and_pixelize(img, new_image)
    except Exception:
        pass


def pixelize(image: np.ndarray) -> np.ndarray:
    return image


def _unscale(image: np.ndarray) -> np.ndarray:
    pass


def _qantization(image: np.ndarray) -> np.ndarray:
    pass


def _upscale(image: np.ndarray) -> np.ndarray:
    pass


def _post_processing(image: np.ndarray) -> np.ndarray:
    pass


def _show_original_and_pixelize(pixelize_image: np.ndarray,
                                original_image: np.ndarray) -> None:
    pass


if __name__ == "__main__":
    _main()
