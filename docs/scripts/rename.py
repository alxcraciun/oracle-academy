import os
import shutil

# Define the path to the directory containing the images
path = r"..."

# Loop through all numbers from 1 to 31
for i in range(1, 33):
    # Define the original filename and the new filename
    original_filename = f"Untitled {i}.png"
    new_filename = f"Image-{i + 67}.png"

    # Use the shutil.move() function to rename the file
    shutil.move(os.path.join(path, original_filename), os.path.join(path, new_filename))

print("Done!")