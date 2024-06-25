import os
import cv2

input_dir = 'unprocessed_data'
output_dir = 'data'

os.makedirs(output_dir, exist_ok=True)

for folder_name in os.listdir(input_dir):
    folder_path = os.path.join(input_dir, folder_name)
    
    if not os.path.isdir(folder_path):
        continue
    
    output_folder_path = os.path.join(output_dir, folder_name)
    os.makedirs(output_folder_path, exist_ok=True)
    
    filename_counter = 1
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        
        image = cv2.imread(image_path)
        
        aspect_ratio = image.shape[1] / image.shape[0]
        new_height = 480
        new_width = int(new_height * aspect_ratio)
        resized_image = cv2.resize(image, (new_width, new_height))
        
        crop_width = 640
        crop_height = new_height
        x = (new_width - crop_width) // 2
        y = 0
        
        cropped_image = resized_image[y:y+crop_height, x:x+crop_width]
        
        output_filename = os.path.join(output_folder_path, f'{filename_counter}.jpg')
        cv2.imwrite(output_filename, cropped_image)
        filename_counter += 1