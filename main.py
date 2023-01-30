import cv2
import numpy as np

available_numbers = "1234"


def PreProcessImage(plain_image):
    return cv2.cvtColor(plain_image, cv2.COLOR_BGR2GRAY)


def GenerateNumbersTemplates():
    numbers = {}

    numbers_path = "images/numbers/"
    template_extension = ".jpg"

    all = list()
    for n in available_numbers:
        template_path = numbers_path + n + template_extension
        number_image = cv2.imread(template_path)
        number_image = PreProcessImage(number_image)
        numbers[n] = number_image
        all.append(number_image)

    # images_together = np.concatenate(all, axis=1)
    # cv2.imshow("Templates", images_together)
    # cv2.waitKey()

    return numbers


def ReadNumbersFromImage(target_image, numbers_images):
    result = []
    positions = []

    for number in available_numbers:
        template = numbers_images[number]
        w, h = template.shape[::-1]
        dt = 10

        matched_image = cv2.matchTemplate(target_image, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.55

        loc = np.where(matched_image >= threshold)
        # contours = cv2.findContours()
        all_points = zip(*loc[::-1])
        for pt in all_points:
            positions.append((pt[0], pt[1], number))


    result = []
    dpixel = 25
    for x, y, number in positions:
        found = False
        for r, ___, ____ in result:
            if abs(x-r) < dpixel:
                found = True
                break

        if not found:
            result.append((x, y, number))

    for x, y, num in result:
        cv2.rectangle(img=target_image,
                      pt1=(x-dt, y - dt),
                      pt2=(x + w + dt, y + h + dt),
                      color=(0, 0, 125),
                      thickness=1)

    str_result = ""
    for _, __, number in result:
        str_result+=str(number)
    print(str_result)

    cv2.imshow("Grey", target_image)
    cv2.waitKey()
    return result


if __name__ == '__main__':
    targets_directory = "images/dataset/"
    # targets_names = ["img_1"]
    targets_names = ["img_1", "img_2", "img_3"]
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
