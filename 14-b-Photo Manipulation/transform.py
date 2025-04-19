from image import Image
import numpy as np
import os
import argparse
from tqdm import tqdm

def brighten(image, factor):
    """
    Adjusts the brightness of an image
    factor: a value > 0, how much you want to brighten the image by
           (< 1 = darken, > 1 = brighten)
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Vectorized operation for better performance
    new_im.array = np.clip(image.array * factor, 0, 1)
    
    return new_im

def adjust_contrast(image, factor, mid=0.5):
    """
    Adjusts the contrast of an image
    factor: a value > 0, how much you want to adjust the contrast by
           (< 1 = decrease contrast, > 1 = increase contrast)
    mid: the midpoint of contrast adjustment (default 0.5)
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Apply contrast adjustment formula: (pixel - mid) * factor + mid
    new_im.array = np.clip((image.array - mid) * factor + mid, 0, 1)
    
    return new_im

def blur(image, kernel_size):
    """
    Blurs an image using a box blur algorithm
    kernel_size: the size of the neighborhood to sample from (odd number)
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Ensure kernel_size is odd
    if kernel_size % 2 == 0:
        kernel_size += 1
    
    # Calculate the half-width of the kernel
    neighbor_range = kernel_size // 2
    
    # Apply blur for each pixel and channel
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # Calculate average of neighboring pixels
                total = 0
                count = 0
                
                # Loop through the neighborhood
                for x_i in range(max(0, x - neighbor_range), min(x_pixels, x + neighbor_range + 1)):
                    for y_i in range(max(0, y - neighbor_range), min(y_pixels, y + neighbor_range + 1)):
                        total += image.array[x_i, y_i, c]
                        count += 1
                
                # Set the pixel value to the average
                new_im.array[x, y, c] = total / count
    
    return new_im

def gaussian_blur(image, sigma=1.0):
    """
    Applies Gaussian blur to an image
    sigma: standard deviation of the Gaussian kernel (controls blur intensity)
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Calculate kernel size based on sigma (ensure it's odd)
    kernel_size = max(3, int(6 * sigma))
    if kernel_size % 2 == 0:
        kernel_size += 1
    
    # Create 1D Gaussian kernel
    k = (kernel_size - 1) // 2
    x = np.arange(-k, k + 1)
    kernel_1d = np.exp(-0.5 * (x / sigma) ** 2)
    kernel_1d = kernel_1d / np.sum(kernel_1d)  # Normalize
    
    # Create temporary image for two-pass algorithm
    temp_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # First pass (horizontal)
    for y in range(y_pixels):
        for x in range(x_pixels):
            for c in range(num_channels):
                val = 0
                for i in range(kernel_size):
                    x_i = x + i - k
                    if 0 <= x_i < x_pixels:
                        val += image.array[x_i, y, c] * kernel_1d[i]
                temp_im.array[x, y, c] = val
    
    # Second pass (vertical)
    for y in range(y_pixels):
        for x in range(x_pixels):
            for c in range(num_channels):
                val = 0
                for i in range(kernel_size):
                    y_i = y + i - k
                    if 0 <= y_i < y_pixels:
                        val += temp_im.array[x, y_i, c] * kernel_1d[i]
                new_im.array[x, y, c] = val
    
    return new_im

def apply_kernel(image, kernel):
    """
    Applies a kernel to an image for edge detection, sharpening, blurring, etc.
    kernel: a 2D array of values
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Get kernel dimensions
    kernel_height, kernel_width = kernel.shape
    
    # Calculate the half-width and half-height of the kernel
    kernel_h_range = kernel_height // 2
    kernel_w_range = kernel_width // 2
    
    # Apply kernel for each pixel and channel
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # Apply the kernel to the neighborhood
                total = 0
                
                # Loop through the kernel
                for i in range(kernel_height):
                    for j in range(kernel_width):
                        # Calculate the image position
                        x_i = x + i - kernel_h_range
                        y_i = y + j - kernel_w_range
                        
                        # Check if the position is within the image bounds
                        if 0 <= x_i < x_pixels and 0 <= y_i < y_pixels:
                            total += image.array[x_i, y_i, c] * kernel[i, j]
                
                # Set the pixel value
                new_im.array[x, y, c] = np.clip(total, 0, 1)
    
    return new_im

def combine_images(image1, image2):
    """
    Combines two images using the squared sum of squares:
    value = sqrt(value_1^2 + value_2^2)
    """
    # Check if the images have the same dimensions
    if image1.array.shape != image2.array.shape:
        raise ValueError("Images must have the same dimensions")
    
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image1.array.shape
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Combine the images using the formula: sqrt(value_1^2 + value_2^2)
    new_im.array = np.sqrt(np.square(image1.array) + np.square(image2.array))
    # Clip values to ensure they're in the valid range [0, 1]
    new_im.array = np.clip(new_im.array, 0, 1)
    
    return new_im

def sharpen(image, amount=1.0):
    """
    Sharpens an image using an unsharp mask
    amount: strength of the sharpening effect (0.0 to 2.0 recommended)
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # Create a blurred version of the image
    blurred = gaussian_blur(image, sigma=1.0)
    
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Apply unsharp mask: original + amount * (original - blurred)
    new_im.array = np.clip(image.array + amount * (image.array - blurred.array), 0, 1)
    
    return new_im

def grayscale(image):
    """
    Converts an image to grayscale
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # Create a new image with the same dimensions but 1 channel
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=3)
    
    # Convert to grayscale using luminance formula
    # Y = 0.2126*R + 0.7152*G + 0.0722*B
    gray_values = (0.2126 * image.array[:, :, 0] + 
                   0.7152 * image.array[:, :, 1] + 
                   0.0722 * image.array[:, :, 2])
    
    # Set all channels to the grayscale value
    for c in range(3):
        new_im.array[:, :, c] = gray_values
    
    return new_im

def sepia(image, intensity=1.0):
    """
    Applies a sepia tone effect to an image
    intensity: strength of the sepia effect (0.0 to 1.0)
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Convert to grayscale first
    gray_im = grayscale(image)
    
    # Sepia tone matrix
    sepia_matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    
    # Apply sepia transformation
    for x in range(x_pixels):
        for y in range(y_pixels):
            rgb = gray_im.array[x, y, :]
            sepia_rgb = np.dot(sepia_matrix, rgb)
            # Blend with original based on intensity
            new_im.array[x, y, :] = (intensity * sepia_rgb + 
                                     (1 - intensity) * image.array[x, y, :])
    
    # Clip values to ensure they're in the valid range [0, 1]
    new_im.array = np.clip(new_im.array, 0, 1)
    
    return new_im

def rotate(image, angle):
    """
    Rotates an image by the specified angle (in degrees)
    """
    from scipy import ndimage
    
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Rotate each channel
    for c in range(num_channels):
        new_im.array[:, :, c] = ndimage.rotate(image.array[:, :, c], angle, 
                                              reshape=False, mode='constant', cval=0)
    
    # Clip values to ensure they're in the valid range [0, 1]
    new_im.array = np.clip(new_im.array, 0, 1)
    
    return new_im

def flip(image, direction='horizontal'):
    """
    Flips an image horizontally or vertically
    direction: 'horizontal' or 'vertical'
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Flip the image
    if direction.lower() == 'horizontal':
        new_im.array = np.flip(image.array, axis=1)
    elif direction.lower() == 'vertical':
        new_im.array = np.flip(image.array, axis=0)
    else:
        raise ValueError("Direction must be 'horizontal' or 'vertical'")
    
    return new_im

def vignette(image, strength=0.5):
    """
    Applies a vignette effect to an image
    strength: intensity of the vignette effect (0.0 to 1.0)
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Copy the original image
    new_im.array = np.copy(image.array)
    
    # Create a vignette mask
    center_x, center_y = x_pixels / 2, y_pixels / 2
    max_dist = np.sqrt(center_x ** 2 + center_y ** 2)
    
    for x in range(x_pixels):
        for y in range(y_pixels):
            # Calculate distance from center (normalized)
            dist = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) / max_dist
            # Apply vignette effect
            factor = 1 - strength * dist ** 2
            new_im.array[x, y, :] *= factor
    
    return new_im

def histogram_equalization(image):
    """
    Enhances image contrast using histogram equalization
    """
    # Get image dimensions
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # Create a new image with the same dimensions
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    # Apply histogram equalization to each channel
    for c in range(num_channels):
        # Get the channel data
        channel = image.array[:, :, c].flatten()
        
        # Calculate histogram
        hist, bins = np.histogram(channel, bins=256, range=(0, 1))
        
        # Calculate cumulative distribution function
        cdf = hist.cumsum()
        cdf_normalized = cdf / cdf[-1]
        
        # Create lookup table
        lookup_table = np.interp(channel, bins[:-1], cdf_normalized)
        
        # Reshape back to original dimensions
        new_im.array[:, :, c] = lookup_table.reshape(x_pixels, y_pixels)
    
    return new_im

def create_output_dir():
    """Create output directory if it doesn't exist"""
    if not os.path.exists('output'):
        os.makedirs('output')

def batch_process(input_dir, operations, output_prefix='processed_'):
    """
    Process multiple images with a sequence of operations
    input_dir: directory containing input images
    operations: list of (function, args) tuples to apply in sequence
    output_prefix: prefix for output filenames
    """
    # Get list of image files
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    
    if not image_files:
        print(f"No image files found in {input_dir}")
        return
    
    print(f"Found {len(image_files)} images to process")
    
    # Process each image
    for filename in tqdm(image_files, desc="Processing images"):
        try:
            # Load image
            img = Image(filename=filename)
            
            # Apply operations in sequence
            result = img
            for op_func, op_args in operations:
                result = op_func(result, *op_args)
            
            # Save result
            output_name = output_prefix + filename
            result.write_image(output_name)
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

def main():
    """Main function with command-line interface"""
    parser = argparse.ArgumentParser(description='Advanced Image Processing Tool')
    parser.add_argument('--input', '-i', help='Input image file', default='lake.png')
    parser.add_argument('--output', '-o', help='Output image file', default='processed.png')
    parser.add_argument('--brightness', '-b', type=float, help='Brightness factor', default=None)
    parser.add_argument('--contrast', '-c', type=float, help='Contrast factor', default=None)
    parser.add_argument('--blur', type=int, help='Box blur kernel size', default=None)
    parser.add_argument('--gaussian', type=float, help='Gaussian blur sigma', default=None)
    parser.add_argument('--sharpen', type=float, help='Sharpen amount', default=None)
    parser.add_argument('--grayscale', action='store_true', help='Convert to grayscale')
    parser.add_argument('--sepia', type=float, help='Apply sepia tone (intensity)', default=None)
    parser.add_argument('--rotate', type=float, help='Rotate image (degrees)', default=None)
    parser.add_argument('--flip', choices=['horizontal', 'vertical'], help='Flip image', default=None)
    parser.add_argument('--vignette', type=float, help='Apply vignette effect (strength)', default=None)
    parser.add_argument('--equalize', action='store_true', help='Apply histogram equalization')
    parser.add_argument('--edge', action='store_true', help='Apply edge detection')
    parser.add_argument('--batch', action='store_true', help='Process all images in input directory')
    
    args = parser.parse_args()
    
    # Create output directory
    create_output_dir()
    
    if args.batch:
        # Define batch operations based on arguments
        operations = []
        if args.brightness is not None:
            operations.append((brighten, [args.brightness]))
        if args.contrast is not None:
            operations.append((adjust_contrast, [args.contrast]))
        if args.blur is not None:
            operations.append((blur, [args.blur]))
        if args.gaussian is not None:
            operations.append((gaussian_blur, [args.gaussian]))
        if args.sharpen is not None:
            operations.append((sharpen, [args.sharpen]))
        if args.grayscale:
            operations.append((grayscale, []))
        if args.sepia is not None:
            operations.append((sepia, [args.sepia]))
        if args.rotate is not None:
            operations.append((rotate, [args.rotate]))
        if args.flip is not None:
            operations.append((flip, [args.flip]))
        if args.vignette is not None:
            operations.append((vignette, [args.vignette]))
        if args.equalize:
            operations.append((histogram_equalization, []))
        if args.edge:
            sobel_x = np.array([
                [1, 0, -1],
                [2, 0, -2],
                [1, 0, -1]
            ])
            sobel_y = np.array([
                [1, 2, 1],
                [0, 0, 0],
                [-1, -2, -1]
            ])
            operations.append((lambda img: combine_images(
                apply_kernel(img, sobel_x), 
                apply_kernel(img, sobel_y)), []))
        
        # Run batch processing
        batch_process('input', operations)
    else:
        # Process single image
        try:
            # Load image
            img = Image(filename=args.input)
            result = img
            
            # Apply operations based on arguments
            if args.brightness is not None:
                result = brighten(result, args.brightness)
            if args.contrast is not None:
                result = adjust_contrast(result, args.contrast)
            if args.blur is not None:
                result = blur(result, args.blur)
            if args.gaussian is not None:
                result = gaussian_blur(result, args.gaussian)
            if args.sharpen is not None:
                result = sharpen(result, args.sharpen)
            if args.grayscale:
                result = grayscale(result)
            if args.sepia is not None:
                result = sepia(result, args.sepia)
            if args.rotate is not None:
                result = rotate(result, args.rotate)
            if args.flip is not None:
                result = flip(result, args.flip)
            if args.vignette is not None:
                result = vignette(result, args.vignette)
            if args.equalize:
                result = histogram_equalization(result)
            if args.edge:
                sobel_x = np.array([
                    [1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]
                ])
                sobel_y = np.array([
                    [1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]
                ])
                result = combine_images(
                    apply_kernel(result, sobel_x), 
                    apply_kernel(result, sobel_y))
            
            # Save result
            result.write_image(args.output)
            print(f"Image processed and saved as {args.output}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    # If run directly, use the command-line interface
    if len(os.sys.argv) > 1:
        main()
    else:
        # Otherwise, run the demo
        create_output_dir()
        
        # Load images
        try:
            lake = Image(filename='lake.png')
            city = Image(filename='city.png')
            print("Images loaded successfully!")
        except Exception as e:
            print(f"Error loading images: {e}")
            print("Make sure 'lake.png' and 'city.png' are in the 'input' directory.")
            exit(1)
        
        # Example 1: Basic operations
        print("Applying basic operations...")
        brightened_im = brighten(lake, 1.7)
        brightened_im.write_image('brightened.png')
        
        contrast_im = adjust_contrast(lake, 2, 0.5)
        contrast_im.write_image('increased_contrast.png')
        
        blur_im = blur(city, 5)
        blur_im.write_image('blur_k5.png')
        
        # Example 2: Advanced filters
        print("Applying advanced filters...")
        gaussian_im = gaussian_blur(city, 2.0)
        gaussian_im.write_image('gaussian_blur.png')
        
        sharp_im = sharpen(lake, 1.5)
        sharp_im.write_image('sharpened.png')
        
        gray_im = grayscale(lake)
        gray_im.write_image('grayscale.png')
        
        sepia_im = sepia(lake, 0.8)
        sepia_im.write_image('sepia.png')
        
        # Example 3: Transformations
        print("Applying transformations...")
        rotated_im = rotate(city, 45)
        rotated_im.write_image('rotated_45.png')
        
        flipped_im = flip(city, 'horizontal')
        flipped_im.write_image('flipped.png')
        
        # Example 4: Effects
        print("Applying special effects...")
        vignette_im = vignette(lake, 0.7)
        vignette_im.write_image('vignette.png')
        
        equalized_im = histogram_equalization(lake)
        equalized_im.write_image('equalized.png')
        
        # Example 5: Edge detection
        print("Applying edge detection...")
        sobel_x = apply_kernel(city, np.array([
            [1, 0, -1],
            [2, 0, -2],
            [1, 0, -1]
        ]))
        sobel_x.write_image('edge_x.png')
        
        sobel_y = apply_kernel(city, np.array([
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]
        ]))
        sobel_y.write_image('edge_y.png')
        
        sobel_xy = combine_images(sobel_x, sobel_y)
        sobel_xy.write_image('edge_xy.png')
        
        print("All operations completed successfully!")
        print("Output images saved to the 'output' directory.")

