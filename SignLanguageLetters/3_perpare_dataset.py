import os
import numpy as np
import zlib

validation_dataset_ratio = 0.2
test_dataset_ratio = 0.1

data_folder = 'data'
output_folder = 'dataset'

def save_file(image, letter_folder_path, letter_folder, phase):
    file_name, ext = os.path.splitext(image)
    image_path = os.path.join(letter_folder_path, file_name + '.jpg')
    label_path = os.path.join(letter_folder_path, file_name + '.txt')

    hashed_filename = format(zlib.crc32((file_name + letter_folder).encode('utf-8')), '08x')
    new_image_path = os.path.join(output_folder, phase, 'images', hashed_filename + '.jpg')
    new_label_path = os.path.join(output_folder, phase, 'labels', hashed_filename + '.txt')

    os.link(label_path, new_label_path)
    os.link(image_path, new_image_path)

listdir = os.listdir(data_folder)

for letter_folder in listdir:
    letter_folder_path = os.path.join(data_folder, letter_folder)
    if not os.path.isdir(letter_folder_path):
        continue

    images = [image for image in os.listdir(letter_folder_path) if image.endswith('.jpg')]
    np.random.shuffle(images)

    num_images = len(images)
    num_validation_images = int(num_images * validation_dataset_ratio)
    num_test_images = int(num_images * test_dataset_ratio)
    num_train_images = num_images - num_validation_images - num_test_images

    train_images = images[:num_train_images]
    validation_images = images[num_train_images:num_train_images + num_validation_images]
    test_images = images[num_train_images + num_validation_images:]

    os.makedirs(os.path.join(output_folder, 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, os.path.join('train', 'images') ), exist_ok=True)
    os.makedirs(os.path.join(output_folder, os.path.join('train', 'labels') ), exist_ok=True)
    with open(os.path.join(output_folder, 'train', 'labels', 'classes.txt'), 'w') as f:
        for letter in listdir:
            f.write(f"{letter}\n")
    for image in train_images:
        save_file(image, letter_folder_path, letter_folder, 'train')

    os.makedirs(os.path.join(output_folder, 'validation'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, os.path.join('validation', 'images') ), exist_ok=True)
    os.makedirs(os.path.join(output_folder, os.path.join('validation', 'labels') ), exist_ok=True)
    with open(os.path.join(output_folder, 'validation', 'labels', 'classes.txt'), 'w') as f:
        for letter in listdir:
            f.write(f"{letter}\n")
    for image in validation_images:
        save_file(image, letter_folder_path, letter_folder, 'validation')

    os.makedirs(os.path.join(output_folder, 'test'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, os.path.join('test', 'images') ), exist_ok=True)
    os.makedirs(os.path.join(output_folder, os.path.join('test', 'labels') ), exist_ok=True)
    with open(os.path.join(output_folder, 'test', 'labels', 'classes.txt'), 'w') as f:
        for letter in listdir:
            f.write(f"{letter}\n")
    for image in test_images:
        save_file(image, letter_folder_path, letter_folder, 'test')