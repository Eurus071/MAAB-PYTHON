import numpy as np

# Task 1: Fahrenheit to Celsius conversion
print("\n" + "=" * 40)
print("TASK 1: Fahrenheit to Celsius Conversion")
print("=" * 40)

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

f_to_c_vectorized = np.vectorize(fahrenheit_to_celsius)

fahrenheit_temps = np.array([32, 68, 100, 212, 77])
print(f"Fahrenheit temperatures: {fahrenheit_temps}")

celsius_temps = f_to_c_vectorized(fahrenheit_temps)
print(f"Celsius temperatures: {celsius_temps}")

print("\nVerification:")
for f, c in zip(fahrenheit_temps, celsius_temps):
    print(f"  {f}°F = {c:.2f}°C")

# Task 2: Custom power function
print("\n" + "=" * 40)
print("TASK 2: Custom Power Function")
print("=" * 40)

def custom_power(base, exponent):
    """Calculate base raised to the power of exponent"""
    return base ** exponent

power_vectorized = np.vectorize(custom_power)

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

print(f"Bases: {bases}")
print(f"Exponents: {exponents}")

results = power_vectorized(bases, exponents)
print(f"Results: {results}")

print("\nVerification:")
for b, e, r in zip(bases, exponents, results):
    print(f"  {b}^{e} = {r}")

# Task 3: System of equations
print("\n" + "=" * 40)
print("TASK 3: System of Linear Equations")
print("=" * 40)

A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])

B = np.array([7, 4, 5])

print(f"System of equations:")
print(f"4x + 5y + 6z = 7")
print(f"3x - y + z = 4")
print(f"2x + y - 2z = 5")

try:
    solution = np.linalg.solve(A, B)
    x, y, z = solution
    
    print(f"\nSolution:")
    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")
    print(f"z = {z:.4f}")
    
    print("\nVerification:")
    print(f"4*{x:.4f} + 5*{y:.4f} + 6*{z:.4f} = {4*x + 5*y + 6*z:.4f} (should be 7)")
    print(f"3*{x:.4f} - {y:.4f} + {z:.4f} = {3*x - y + z:.4f} (should be 4)")
    print(f"2*{x:.4f} + {y:.4f} - 2*{z:.4f} = {2*x + y - 2*z:.4f} (should be 5)")
    
except np.linalg.LinAlgError:
    print("The system of equations has no unique solution.")

# Task 4: Electrical circuit equations
print("\n" + "=" * 40)
print("TASK 4: Electrical Circuit Equations")
print("=" * 40)

A_currents = np.array([[10, -2, 3],
                       [-2, 8, -1],
                       [3, -1, 6]])

B_currents = np.array([12, -5, 15])

print(f"System of equations for currents:")
print(f"10I₁ - 2I₂ + 3I₃ = 12")
print(f"-2I₁ + 8I₂ - I₃ = -5")
print(f"3I₁ - I₂ + 6I₃ = 15")

try:
    currents = np.linalg.solve(A_currents, B_currents)
    I1, I2, I3 = currents
    
    print(f"\nCurrents:")
    print(f"I₁ = {I1:.4f} A")
    print(f"I₂ = {I2:.4f} A")
    print(f"I₃ = {I3:.4f} A")
    
    print("\nVerification:")
    print(f"10*{I1:.4f} - 2*{I2:.4f} + 3*{I3:.4f} = {10*I1 - 2*I2 + 3*I3:.4f} (should be 12)")
    print(f"-2*{I1:.4f} + 8*{I2:.4f} - {I3:.4f} = {-2*I1 + 8*I2 - I3:.4f} (should be -5)")
    print(f"3*{I1:.4f} - {I2:.4f} + 6*{I3:.4f} = {3*I1 - I2 + 6*I3:.4f} (should be 15)")
    
except np.linalg.LinAlgError:
    print("The circuit equations have no unique solution.")


print("\n" + "=" * 60)
print("TASK 5: IMAGE MANIPULATION WITH NUMPY AND PIL")
print("=" * 60)

from PIL import Image
import os

os.makedirs('images', exist_ok=True)

def create_sample_image():
    """Create a sample image if birds.jpg doesn't exist"""

    img_array = np.zeros((300, 400, 3), dtype=np.uint8)
    
    for i in range(300):
        for j in range(400):
            img_array[i, j, 0] = j // 2  
            img_array[i, j, 1] = i // 2  
            img_array[i, j, 2] = 128     
    
    for center_x, center_y in [(100, 100), (200, 150), (300, 80)]:
        for i in range(-20, 21):
            for j in range(-20, 21):
                if i**2 + j**2 <= 400:  
                    x = center_x + i
                    y = center_y + j
                    if 0 <= x < 400 and 0 <= y < 300:
                        img_array[y, x, 0] = 255  
                        img_array[y, x, 1] = 255  
                        img_array[y, x, 2] = 255
    
    img = Image.fromarray(img_array)
    img.save('images/birds.jpg')
    print("Created sample image: images/birds.jpg")
    return img_array

def load_image(image_path):
    """Load image using PIL and convert to numpy array"""
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        print(f"Loaded image: {image_path}")
        print(f"Image shape: {img_array.shape}")
        print(f"Image dtype: {img_array.dtype}")
        return img_array, img.mode
    except FileNotFoundError:
        print(f"Image not found: {image_path}")
        print("Creating sample image...")
        img_array = create_sample_image()
        return img_array, 'RGB'

def save_image(img_array, output_path, mode='RGB'):
    """Save numpy array as image using PIL"""
    img = Image.fromarray(img_array.astype(np.uint8), mode)
    img.save(output_path)
    print(f"Saved image: {output_path}")

def flip_image(img_array):
    """
    Flip image horizontally and vertically using numpy
    
    Args:
        img_array: numpy array representing the image
    
    Returns:
        Flipped image array
    """
    print("\nFlipping image horizontally and vertically...")
    
    horizontal_flip = img_array[:, ::-1, :]
    
    vertical_flip = horizontal_flip[::-1, :, :]
    
    return vertical_flip

def add_random_noise(img_array, intensity=25):
    """
    Add random noise to the image
    
    Args:
        img_array: numpy array representing the image
        intensity: noise intensity (0-255)
    
    Returns:
        Noisy image array
    """
    print(f"\nAdding random noise with intensity {intensity}...")
    
    noise = np.random.randint(-intensity, intensity, img_array.shape)
    
    noisy_img = img_array.astype(np.int16) + noise
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    
    return noisy_img

def brighten_channels(img_array, channel_increase=40, channel_index=0):
    """
    Increase brightness of specific channel
    
    Args:
        img_array: numpy array representing the image
        channel_increase: amount to increase channel brightness
        channel_index: 0 for red, 1 for green, 2 for blue
    
    Returns:
        Brightened image array
    """
    channel_names = ['Red', 'Green', 'Blue']
    print(f"\nBrightening {channel_names[channel_index]} channel by {channel_increase}...")
    
    brightened_img = img_array.copy().astype(np.int16)
    
    brightened_img[:, :, channel_index] += channel_increase
    
    brightened_img = np.clip(brightened_img, 0, 255).astype(np.uint8)
    
    return brightened_img

def apply_mask(img_array, center_x=None, center_y=None, width=100, height=100):
    """
    Apply a black rectangular mask to the image
    
    Args:
        img_array: numpy array representing the image
        center_x: x-coordinate of mask center (default: image center)
        center_y: y-coordinate of mask center (default: image center)
        width: width of mask
        height: height of mask
    
    Returns:
        Masked image array
    """
    print(f"\nApplying {width}x{height} black mask...")
    
    masked_img = img_array.copy()
    
    img_height, img_width = img_array.shape[:2]
    
    if center_x is None:
        center_x = img_width // 2
    if center_y is None:
        center_y = img_height // 2
    
    x_start = max(0, center_x - width // 2)
    x_end = min(img_width, center_x + width // 2)
    y_start = max(0, center_y - height // 2)
    y_end = min(img_height, center_y + height // 2)
    
    masked_img[y_start:y_end, x_start:x_end, :] = 0
    
    print(f"Mask applied from ({x_start}, {y_start}) to ({x_end}, {y_end})")
    
    return masked_img

def display_image_info(img_array, title="Image"):
    """Display basic information about the image array"""
    print(f"\n{title}:")
    print(f"  Shape: {img_array.shape}")
    print(f"  Dtype: {img_array.dtype}")
    print(f"  Min value: {img_array.min()}")
    print(f"  Max value: {img_array.max()}")
    print(f"  Mean value: {img_array.mean():.2f}")

def main_image_manipulation():
    """Main function for image manipulation tasks"""
    
    # 1. Load the image
    img_array, mode = load_image('images/birds.jpg')
    original_img = img_array.copy()
    
    # Display original image info
    display_image_info(img_array, "Original Image")
    
    # 2. Flip the image
    flipped_img = flip_image(img_array)
    display_image_info(flipped_img, "Flipped Image")
    save_image(flipped_img, 'images/flipped_birds.jpg', mode)
    
    # 3. Add random noise
    noisy_img = add_random_noise(img_array, intensity=30)
    display_image_info(noisy_img, "Noisy Image")
    save_image(noisy_img, 'images/noisy_birds.jpg', mode)
    
    # 4. Brighten red channel
    brightened_img = brighten_channels(img_array, channel_increase=40, channel_index=0)
    display_image_info(brightened_img, "Brightened (Red Channel) Image")
    save_image(brightened_img, 'images/brightened_birds.jpg', mode)
    
    # 5. Apply a mask
    masked_img = apply_mask(img_array, width=100, height=100)
    display_image_info(masked_img, "Masked Image")
    save_image(masked_img, 'images/masked_birds.jpg', mode)
    
    # 6. Create a combined transformation (Bonus)
    print("\n" + "=" * 40)
    print("BONUS: Combined Transformations")
    print("=" * 40)
    
    # Apply multiple transformations in sequence
    combined_img = original_img.copy()
    combined_img = flip_image(combined_img)
    combined_img = add_random_noise(combined_img, intensity=20)
    combined_img = brighten_channels(combined_img, channel_increase=30, channel_index=2)  # Blue channel
    combined_img = apply_mask(combined_img, width=150, height=150)
    
    display_image_info(combined_img, "Combined Transformations Image")
    save_image(combined_img, 'images/combined_birds.jpg', mode)
    
    print("\n" + "=" * 60)
    print("ALL IMAGE MANIPULATIONS COMPLETED!")
    print("=" * 60)
    print("\nGenerated Images:")
    print("1. images/flipped_birds.jpg - Horizontally and vertically flipped")
    print("2. images/noisy_birds.jpg - With random noise")
    print("3. images/brightened_birds.jpg - Red channel brightened")
    print("4. images/masked_birds.jpg - With black rectangular mask")
    print("5. images/combined_birds.jpg - All transformations combined")
    
    return {
        'original': original_img,
        'flipped': flipped_img,
        'noisy': noisy_img,
        'brightened': brightened_img,
        'masked': masked_img,
        'combined': combined_img
    }

# Run all tasks
if __name__ == "__main__":
    print("=" * 70)
    print("COMPREHENSIVE NUMPY IMAGE PROCESSING PROJECT")
    print("=" * 70)
    
  
    # Run image manipulation task
    images_dict = main_image_manipulation()
    
    print("\n" + "=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 70)