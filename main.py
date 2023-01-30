import cv2
import numpy as np

available_numbers = "1234"


def PreProcessImage(plain_image):
    return cv2.cvtColor(plain_image, cv2.COLOR_BGR2GRAY)


def GenerateNumbersTemplates():
    numbers = {}

    numbers_path = "images/numbers/"
    template_extension = ".jpg"

    for n in available_numbers:
        template_path = numbers_path + n + template_extension
        number_image = cv2.imread(template_path)
        number_image = PreProcessImage(number_image)
        numbers[n] = number_image

    images_together = np.concatenate((numbers["1"], numbers["2"], numbers["3"], numbers["4"]), axis=1)
    cv2.imshow("Templates", images_together)
    cv2.waitKey()

    return numbers


def ReadNumbersFromImage(target_image, numbers_images):
    result = []
    positions = []

    for number in available_numbers:
        template = numbers_images[number]
        w, h = template.shape[::-1]

        matched_image = cv2.matchTemplate(target_image, template, cv2.TM_CCOEFF)
        threshold = 0.8

        loc = np.where(matched_image >= threshold)
        # contours = cv2.findContours()
        for pt in zip(*loc[::-1]):
            x_value = pt[0]
            cv2.rectangle(img=target_image, pt1=pt, pt2=(pt[0] + w, pt[1] + h), color=(0, 0, 255), thickness=2)
            positions += (number, x_value)

    cv2.imshow("Templates", matched_image)
    cv2.waitKey()

    # print(positions)
    # positions.sort(key=lambda a: a[0])
    return result


if __name__ == '__main__':
    targets_directory = "images/dataset/"
    targets_names = ["img_1"]
    # targets_names = ["img_1", "img_2", "img_3"]
    target_extension = ".jpg"

    all_numbers = GenerateNumbersTemplates()
    for image_name in targets_names:
        path = targets_directory + image_name + target_extension
        image = cv2.imread(path, 1)

        image = PreProcessImage(image)

        clustered_numbers = ReadNumbersFromImage(image, all_numbers)
        print(len(clustered_numbers))
        for number in clustered_numbers:
            print(number)
        print()
