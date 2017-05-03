def get_pixel_statistics(blue_stars_array, yellow_stars_array):
    count_stars = len(blue_stars_array)
    total_brightness_blue = 0
    total_brightness_yellow = 0
    for i in xrange(len(blue_stars_array)):
        total_brightness_blue += blue_stars_array[i]
        total_brightness_yellow +=  yellow_stars_array[i]
    average_brightness_stars_blue = total_brightness_blue / len(blue_stars_array)
    average_brightness_stars_yellow = total_brightness_yellow / len(yellow_stars_array)
    return {
        "header": "Stars",
        "content":
            "Count stars: " + str(count_stars) + ". " +
            "Average brightness of stars from blue filter photo: " + str(average_brightness_stars_blue) + ". " +
            "Average brightness of stars from yellow filter photo: " + str(average_brightness_stars_yellow) + "."}