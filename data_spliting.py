import os
import random
import shutil

# Set the directories
source_dir = 'office'
train_dir = 'train'
test_dir = 'test'
val_dir = 'val'

# Set the split ratios (e.g., 0.8 for 80% train, 10% test, 10% val)
train_ratio = 0.8
test_ratio = 0.1
val_ratio = 0.1

# Create the train, test, and val directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Walk through all subdirectories in the source directory
for root, dirs, files in os.walk(source_dir):
    # Get the relative path
    rel_path = os.path.relpath(root, source_dir)
    # Create the subdirectories in the train, test, and val directories
    train_subdir = os.path.join(train_dir, rel_path)
    test_subdir = os.path.join(test_dir, rel_path)
    val_subdir = os.path.join(val_dir, rel_path)
    os.makedirs(train_subdir, exist_ok=True)
    os.makedirs(test_subdir, exist_ok=True)
    os.makedirs(val_subdir, exist_ok=True)
    # Randomly split the files into train, test, and val
    for file in files:
        r = random.random()
        if r < train_ratio:
            shutil.copy(os.path.join(root, file), train_subdir)
        elif r < train_ratio + test_ratio:
            shutil.copy(os.path.join(root, file), test_subdir)
        else:
            shutil.copy(os.path.join(root, file), val_subdir)


