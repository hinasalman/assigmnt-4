from transform import *  # noqa: F403
from image import Image
import os
import numpy as np

def run_demo():
    """
    Run a comprehensive demo of all image processing features for lake, city, and sky images.
    """
    create_output_dir()  # noqa: F405

    try:
        lake = Image(filename='lake.png')
        city = Image(filename='city.png')
        sky = Image(filename='sky.png')
        print("Images loaded successfully!")
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    demo_dir = os.path.join('output', 'demo')
    if not os.path.exists(demo_dir):
        os.makedirs(demo_dir)

    images = {"lake": lake, "city": city, "sky": sky}

    for name, img in images.items():
        print(f"\n=== Processing {name} ===")

        for factor in [0.5, 1.0, 1.5, 2.0]:
            result = brighten(img, factor)
            result.write_image(f'demo/{name}_brightness_{factor}.png')

        for factor in [0.5, 1.0, 2.0, 3.0]:
            result = adjust_contrast(img, factor)
            result.write_image(f'demo/{name}_contrast_{factor}.png')

        for size in [3, 7, 15]:
            result = blur(img, size)
            result.write_image(f'demo/{name}_box_blur_{size}.png')

        for sigma in [1.0, 2.0, 4.0]:
            result = gaussian_blur(img, sigma)
            result.write_image(f'demo/{name}_gaussian_{sigma}.png')

        sobel_x = apply_kernel(img, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
        sobel_x.write_image(f'demo/{name}_edge_x.png')

        sobel_y = apply_kernel(img, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
        sobel_y.write_image(f'demo/{name}_edge_y.png')

        sobel_xy = combine_images(sobel_x, sobel_y)
        sobel_xy.write_image(f'demo/{name}_edge_combined.png')

        gray = grayscale(img)
        gray.write_image(f'demo/{name}_grayscale.png')

        for intensity in [0.3, 0.6, 1.0]:
            result = sepia(img, intensity)
            result.write_image(f'demo/{name}_sepia_{intensity}.png')

        for amount in [0.5, 1.0, 2.0]:
            result = sharpen(img, amount)
            result.write_image(f'demo/{name}_sharpen_{amount}.png')

        equalized = histogram_equalization(img)
        equalized.write_image(f'demo/{name}_equalized.png')

        for strength in [0.3, 0.6, 0.9]:
            result = vignette(img, strength)
            result.write_image(f'demo/{name}_vignette_{strength}.png')

        for angle in [45, 90, 180]:
            result = rotate(img, angle)
            result.write_image(f'demo/{name}_rotate_{angle}.png')

        flip_h = flip(img, 'horizontal')
        flip_h.write_image(f'demo/{name}_flip_horizontal.png')

        flip_v = flip(img, 'vertical')
        flip_v.write_image(f'demo/{name}_flip_vertical.png')

        # Vintage effect example
        vintage = img
        vintage = adjust_contrast(vintage, 0.8)
        vintage = sepia(vintage, 0.7)
        vintage = vignette(vintage, 0.5)
        vintage.write_image(f'demo/{name}_vintage.png')

        # HDR effect
        hdr = img
        hdr = adjust_contrast(hdr, 1.5)
        hdr = sharpen(hdr, 1.2)
        hdr = brighten(hdr, 1.1)
        hdr.write_image(f'demo/{name}_hdr.png')

if __name__ == "__main__":
    run_demo()
