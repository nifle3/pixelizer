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
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    unscale_image = _unscale(image)
    qantization_image = _qantization(unscale_image)
    upscale_image = _upscale(qantization_image)
    post_processing_image = _post_processing(upscale_image)

    return post_processing_image


def _unscale(image: np.ndarray) -> np.ndarray:
    SCALE_FACTOR = 1/3.0

    height, width = _get_new_size(image=image, scale_factor=SCALE_FACTOR)
    scaled_image = cv2.resize(src=image,
                              dsize=(width, height),
                              interpolation=cv2.INTER_AREA)

    return scaled_image


def _get_new_size(image: np.ndarray, scale_factor: float) -> Tuple[int, int]:
    heigth, width = image.shape[:2]

    new_heigth = int(heigth * scale_factor)
    new_width = int(width * scale_factor)

    return (new_heigth, new_width)


def _qantization(image: np.ndarray) -> np.ndarray:    
    N_COLORS = 8

    pixels = image.reshape((-1, 3))
    pixels = np.float32(pixels)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

    _, label, centers = cv2.kmeans(pixels, N_COLORS, None, criteria,
                                   10,
                                   cv2.KMEANS_PP_CENTERS)

    centers = np.uint8(centers)
    quantized = centers[label.flatten()]
    quantized = quantized.reshape(image.shape)

    return quantized


def _upscale(image: np.ndarray) -> np.ndarray:
    SCALE_FACTOR = 3.0
    heigth, width = _get_new_size(image, SCALE_FACTOR)
    upscale_image = cv2.resize(src=image,
                               dsize=(width, heigth),
                               interpolation=cv2.INTER_NEAREST)

    return upscale_image


def _post_processing(image: np.ndarray) -> np.ndarray:
    EDGE_STRENGTH = 0.4

    sobel = _sobel_applied(image)
    float_image = np.float32(image)

    for i in range(3):
        float_image[:, :, i] = np.clip(
            float_image[:, :, i] - sobel*EDGE_STRENGTH,
            0,
            255)

    result = np.uint8(float_image)
    return result


def _sobel_applied(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)

    sobel_combained = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

    return sobel_combained


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
