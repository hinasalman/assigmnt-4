import numpy as np
import os
from PIL import Image as PILImage

class Image:
    def __init__(self, x_pixels=0, y_pixels=0, num_channels=0, filename=''):
        # you need to input either filename OR x_pixels, y_pixels, and num_channels
        self.input_path = 'input/'
        self.output_path = 'output/'
        
        # Create directories if they don't exist
        if not os.path.exists(self.input_path):
            os.makedirs(self.input_path)
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
            
        if x_pixels and y_pixels and num_channels:
            self.x_pixels = x_pixels
            self.y_pixels = y_pixels
            self.num_channels = num_channels
            self.array = np.zeros((x_pixels, y_pixels, num_channels))
        elif filename:
            try:
                self.array = self.read_image(filename)
                self.x_pixels, self.y_pixels, self.num_channels = self.array.shape
                print(f"Image '{filename}' loaded with dimensions: {self.x_pixels}x{self.y_pixels}x{self.num_channels}")
            except Exception as e:
                print(f"Error loading image '{filename}': {e}")
                raise
        else:
            raise ValueError("You need to input either a filename OR specify the dimensions of the image")

    def read_image(self, filename, gamma=2.2):
        '''
        read image using PIL, return 3D numpy array organized along Y, X, channel
        values are float, gamma is decoded
        '''
        try:
            full_path = os.path.join(self.input_path, filename)
            if not os.path.exists(full_path):
                raise FileNotFoundError(f"Image file not found: {full_path}")
                
            # Open the image using PIL
            img = PILImage.open(full_path)
            
            # Convert to RGB mode if it's not already
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Convert to numpy array
            img_array = np.array(img).astype(np.float64)
            
            # Normalize to [0, 1]
            img_array = img_array / 255.0
            
            # Apply gamma correction
            if gamma != 1.0:
                img_array = img_array ** gamma
                
            return img_array
            
        except Exception as e:
            print(f"Error reading image {filename}: {e}")
            raise

    def write_image(self, output_file_name, gamma=2.2):
        '''
        3D numpy array (Y, X, channel) of values between 0 and 1 -> write to image file
        '''
        try:
            # Ensure output directory exists
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path)
                
            # Clip values to ensure they're in the valid range [0, 1]
            im = np.clip(self.array, 0, 1)
            
            # Apply gamma correction
            if gamma != 1.0:
                im = im ** (1/gamma)
            
            # Scale to [0, 255] and convert to 8-bit
            im_8bit = (im * 255).astype(np.uint8)
            
            # Create PIL image
            img = PILImage.fromarray(im_8bit)
            
            # Save the image
            output_path = os.path.join(self.output_path, output_file_name)
            img.save(output_path)
            
            print(f"Image successfully saved to {output_path}")
        except Exception as e:
            print(f"Error writing image {output_file_name}: {e}")
            raise
            
    def show(self):
        """
        Display the image using PIL
        """
        try:
            # Clip values to ensure they're in the valid range [0, 1]
            im = np.clip(self.array, 0, 1)
            
            # Apply gamma correction for display
            im = im ** (1/2.2)
            
            # Scale to [0, 255] and convert to 8-bit
            im_8bit = (im * 255).astype(np.uint8)
            
            # Create PIL image and display it
            img = PILImage.fromarray(im_8bit)
            img.show()
        except Exception as e:
            print(f"Error displaying image: {e}")
            raise
            
    def resize(self, new_width, new_height, method='bilinear'):
        """
        Resize the image to new dimensions
        method: 'nearest', 'bilinear', 'bicubic', or 'lanczos'
        """
        try:
            # Clip values to ensure they're in the valid range [0, 1]
            im = np.clip(self.array, 0, 1)
            
            # Apply gamma correction for processing
            im = im ** (1/2.2)
            
            # Convert to PIL Image for resizing
            im_8bit = (im * 255).astype(np.uint8)
            img = PILImage.fromarray(im_8bit)
            
            # Resize using the specified method
            resample_method = {
                'nearest': PILImage.NEAREST,
                'bilinear': PILImage.BILINEAR,
                'bicubic': PILImage.BICUBIC,
                'lanczos': PILImage.LANCZOS
            }.get(method.lower(), PILImage.BILINEAR)
            
            resized_img = img.resize((new_width, new_height), resample_method)
            
            # Convert back to numpy array
            resized_array = np.array(resized_img).astype(np.float64) / 255.0
            
            # Apply gamma correction
            resized_array = resized_array ** 2.2
            
            # Create a new image with the resized dimensions
            new_im = Image(x_pixels=new_width, y_pixels=new_height, num_channels=self.num_channels)
            new_im.array = resized_array
            
            return new_im
        except Exception as e:
            print(f"Error resizing image: {e}")
            raise
            
    def crop(self, x_start, y_start, width, height):
        """
        Crop the image to the specified region
        """
        try:
            # Check if the crop region is valid
            if (x_start < 0 or y_start < 0 or 
                x_start + width > self.x_pixels or 
                y_start + height > self.y_pixels):
                raise ValueError("Crop region is outside image boundaries")
            
            # Create a new image with the cropped dimensions
            new_im = Image(x_pixels=width, y_pixels=height, num_channels=self.num_channels)
            
            # Copy the cropped region
            new_im.array = self.array[x_start:x_start+width, y_start:y_start+height, :].copy()
            
            return new_im
        except Exception as e:
            print(f"Error cropping image: {e}")
            raise

