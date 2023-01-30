import cv2


def ClusterNumbers(positions, numbers):
    result = []

    return result


def PreProcess(plain_image):
    return cv2.cvtColor(plain_image, cv2.COLOR_BGR2GRAY)


def GenerateNumbersTemplates():
    numbers = {}

    numbers_path = "images/numbers/"
    template_extension = ".jpg"

    for n in "1234":
        template_path = numbers_path + n + template_extension
        number_image = cv2.imread(template_path)
        cv2.imshow(template_path, number_image)
        numbers[n] = number_image

    return numbers


def ReadNumbersFromImage(image, numbers_images):
    result = []

    positions = {}
    for pattern in numbers_images:
        coordinates = []

    result = ClusterNumbers(positions, numbers_images)
    return result


if __name__ == '__main__':
    targets_directory = "images/dataset/"
    targets_names = ["img_1", "img_2", "img_3"]
    target_extension = ".jpg"

    all_numbers = GenerateNumbersTemplates()
    for image_name in targets_names:
        path = targets_directory + image_name + target_extension
        image = cv2.imread(path, 1)
        PreProcess(image)

        clustered_numbers = ReadNumbersFromImage(image, all_numbers)
        print(len(clustered_numbers))
        for number in clustered_numbers:
            print(number)
