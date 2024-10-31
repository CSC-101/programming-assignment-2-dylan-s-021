import data

# Write your functions for each part in the space below.

# Part 1
# Create a rectangle given any 2 points in any order
# input: 2 Point parameters to be the top left and bottom right of a rectangle
# output: a Rectangle with input points as top left and bottom right points
def create_rectangle(point1:data.Point, point2:data.Point):
    if point1.x < point2.x and point1.y > point2.y:
        rectangle = data.Rectangle(point1, point2)
        return rectangle
    elif point1.x > point2.x and point1.y < point2.y:
        rectangle = data.Rectangle(point2, point1)
        return rectangle
    elif point1.x < point2.x and point1.y < point2.y:
        temp = point1.y
        point1.y = point2.y
        point2.y = temp
        rectangle = data.Rectangle(point1, point2)
        return rectangle
    elif point1.x > point2.x and point1.y > point2.y:
        temp = point1.y
        point1.y = point2.y
        point2.y = temp
        rectangle = data.Rectangle(point2, point1)
        return rectangle
    else:
        return "Invalid input. Input points in vertical or horizontal line."


# Part 2
# Determine if first 1st input duration is shorter than 2nd input duration
# input: 2 Duration parameters
# output: True if 1st duration is shorter, False otherwise
def shorter_duration_than(duration1:data.Duration, duration2:data.Duration) -> bool:
    if duration1.minutes < duration2.minutes:
        return True
    elif duration1.minutes > duration2.minutes:
        return False
    elif duration1.seconds < duration2.seconds:
        return True
    else:
        return False


# Part 3
# make a list of songs shorter than a given input duration
# input: a list of Songs and a Duration
# output: a list of songs with a shorter duration than the given input duration
def songs_shorter_than(list_of_songs:list[data.Song], duration:data.Duration) -> list[data.Song]:
    short_songs = []
    for i in range(len(list_of_songs)):
        if list_of_songs[i].duration.minutes < duration.minutes:
            short_songs.append(list_of_songs[i])
        elif list_of_songs[i].duration.minutes == duration.minutes and list_of_songs[i].duration.seconds < duration.seconds:
            short_songs.append(list_of_songs[i])
    return short_songs


# Part 4
# the total duration of a "playlist" from a list of songs given a list of indexes
# input: a list of Songs and a list of integers
# output: the total duration of the songs indexed in the list of integers
def running_time(list_of_songs:list[data.Song], playlist_integers:list[int]) -> data.Duration:
    playlist_duration = data.Duration(0,0)
    for i in playlist_integers:
        if i in range(len(list_of_songs) - 1):
            playlist_duration_seconds = playlist_duration.seconds + list_of_songs[i].duration.seconds
            playlist_duration_minutes = playlist_duration.minutes + list_of_songs[i].duration.minutes
            if playlist_duration_seconds >= 60:
                playlist_duration_seconds = playlist_duration_seconds - 60
                playlist_duration_minutes = playlist_duration_minutes + 1
            playlist_duration = data.Duration(playlist_duration_minutes, playlist_duration_seconds)
    return playlist_duration


# Part 5
# determine if a route is valid
# input: a list of city link pairs and a list of cities representing a route
# output: returns True if the route runs through city links and False otherwise
def validate_route(city_links:list[list[str]], route:list[str]) -> bool:
    if len(route) == 0 or len(route) == 1:
        return True
    for i in range(len(route) - 1):
        temp1 = [route[i], route[i + 1]]
        temp2 = [route[i + 1], route[i]]
        if (temp1 or temp2) not in city_links:
            return False
        else:
            return True


# Part 6
# return the index of the beginning of the longest continuous repetition of a given list of integers
# input: list of integers
# output: the index of the beginning of the longest continuous repetition in the input list
def longest_repetition(integers:list[int]) -> int:
    idx = 0
    j = 1
    for i in range(len(integers) - 1): # cycling through list of integers
        if integers[i] == integers[i + 1]: # comparing neighboring integers in list
            idx = i # if neighbors equal, idx equal to left neighbor's index
            j = 1 # restart counter
        else:
            j = j + 1 # if neighbors not equal,
            idx = i - 1 # if neighbors not equal, idx equal to last index
    return idx
