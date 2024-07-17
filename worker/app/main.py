from typing import Tuple
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

    new_image = pixelize(img)
    _show_original_and_pixelize(new_image, img)


def pixelize(image: np.ndarray) -> np.ndarray:
    unscale_image = _unscale(image)
    qantization_image = _qantization(unscale_image)
    upscale_image = _upscale(qantization_image)
    post_processing_image = _post_processing(upscale_image)

    return post_processing_image


def _unscale(image: np.ndarray) -> np.ndarray:
    SCALE_FACTOR = 1/3.0

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width = _get_new_size(image=image_rgb, scale_factor=SCALE_FACTOR)
    scaled_image = cv2.resize(src=image_rgb,
                              dsize=(width, height),
                              interpolation=cv2.INTER_CUBIC)

    return scaled_image


def _get_new_size(image: np.ndarray, scale_factor: float) -> Tuple[int, int]:
    heigth, width = image.shape[:2]

    new_heigth = int(heigth * scale_factor)
    new_width = int(width * scale_factor)

    return (new_heigth, new_width)


def _qantization(image: np.ndarray) -> np.ndarray:
    palette = _get_palette(image)
    indicies = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 

    return image


def _get_palette(image: np.ndarray) -> np.ndarray:
    pass


def _upscale(image: np.ndarray) -> np.ndarray:
    SCALE_FACTOR = 3.0
    heigth, width = _get_new_size(image, SCALE_FACTOR)
    upscale_image = cv2.resize(src=image,
                               dsize=(width, heigth),
                               interpolation=cv2.INTER_AREA)

    return upscale_image


def _post_processing(image: np.ndarray) -> np.ndarray:
    return image


def _show_original_and_pixelize(pixelize_image: np.ndarray,
                                original_image: np.ndarray) -> None:
    import matplotlib.pyplot as plt
    fig, (ax1, ax2) = plt.subplots(1, 2, dpi=200)

    ax1.set_title("before pixelizing")
    ax1.imshow(original_image)
    ax1.axis("off")
    print("showing..")

    ax2.set_title("after pizelizing")
    ax2.imshow(pixelize_image)
    ax2.axis("off")

    plt.show()


if __name__ == "__main__":
    _main()
