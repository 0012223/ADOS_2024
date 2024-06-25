import cv2
import numpy as np
import os

data_folder = 'data'

letters = ['A', 'B', 'C', 'D', 'E', 'F']

letterClasses = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
}

for letter in letters:
    for num in range (1, 106):
        image_path = os.path.join(data_folder, 'sign_' + letter, str(num) + '.jpg')
        image = cv2.imread(image_path)
        if image is None:
            print(f"Could not read the image: {image_path}")
            continue
        image_blur = cv2.GaussianBlur(image, (5, 5), 0)

        hsv_image = cv2.cvtColor(image_blur, cv2.COLOR_BGR2HSV)

        H_range = (0, 29) 
        S_range = (17, 120)
        V_range = (100, 255)

        lower_bound = np.array([H_range[0], S_range[0], V_range[0]])
        upper_bound = np.array([H_range[1], S_range[1], V_range[1]])

        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            contours = sorted(contours, key=cv2.contourArea, reverse=True) 
            x, y, w, h = cv2.boundingRect(contours[0]) 

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            directory, filename = os.path.split(image_path)

            img_width, img_height = 640, 480
            x_center = (x + w / 2) / img_width
            y_center = (y + h / 2) / img_height
            width = w / img_width
            height = h / img_height

            image_class = letterClasses[letter]

            with open(os.path.join(directory, os.path.splitext(filename)[0] + '.txt'), 'w') as f:
                f.write(f"{image_class} {x_center} {y_center} {width} {height}")

            cv2.imshow("Detected Object " + letter, image)
            cv2.imshow("Mask", mask)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No object found within the specified color range.")