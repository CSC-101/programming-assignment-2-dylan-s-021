import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        point1 = data.Point(3,2)
        point2 = data.Point(1,4)
        expected = data.Rectangle(point2, point1)
        actual = hw2.create_rectangle(point1, point2)
        self.assertEqual(expected, actual)

    def test_create_rectangle_2(self):
        point1 = data.Point(1,2)
        point2 = data.Point(3,4)
        expected = data.Rectangle(data.Point(1,4), data.Point(3,2))
        actual = hw2.create_rectangle(point1, point2)
        self.assertEqual(expected, actual)

    def test_create_rectangle_3(self):
        point1 = data.Point(1, 2)
        point2 = data.Point(1, 4)
        expected = "Invalid input. Input points in vertical or horizontal line."
        actual = hw2.create_rectangle(point1, point2)
        self.assertEqual(expected, actual)


    # Part 2
    def test_shorter_duration_than_1(self):
        duration1 = data.Duration(2,30)
        duration2 = data.Duration(3, 45)
        expected = True
        actual = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, actual)

    def test_shorter_duration_than_2(self):
        duration1 = data.Duration(2,30)
        duration2 = data.Duration(2, 45)
        expected = True
        actual = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, actual)


    # Part 3
    def test_songs_shorter_than_1(self):
        list_of_songs = [data.Song("Artist1", "Title1", data.Duration(3,15)),
                         data.Song("Artist2", "Title2", data.Duration(2,50)),
                         data.Song("Artist3", "Title3", data.Duration(4,25))]
        duration = data.Duration(3,30)
        expected = [data.Song("Artist1", "Title1", data.Duration(3,15)),
                    data.Song("Artist2", "Title2", data.Duration(2,50))]
        actual = hw2.songs_shorter_than(list_of_songs,duration)
        self.assertEqual(expected, actual)

    def test_songs_shorter_than_2(self):
        list_of_songs = [data.Song("Artist1", "Title1", data.Duration(3,30)),
                         data.Song("Artist2", "Title2", data.Duration(2,50)),
                         data.Song("Artist3", "Title3", data.Duration(4,25))]
        duration = data.Duration(3,30)
        expected = [data.Song("Artist2", "Title2", data.Duration(2,50))]
        actual = hw2.songs_shorter_than(list_of_songs,duration)
        self.assertEqual(expected, actual)


    # Part 4
    def test_running_time_1(self):
        list_of_songs = [data.Song("Decemberists", "June Hymn", data.Duration(4,30)),
                         data.Song("Broken Bells", "October", data.Duration(3,40)),
                         data.Song("Kansas", "Dust in the Wind", data.Duration(3,29)),
                         data.Song("Local Natives", "Airplanes", data.Duration(3,58))]
        playlist_integers = [0, 2, 1, 3, 0]
        expected = data.Duration(20,7)
        actual = hw2.running_time(list_of_songs, playlist_integers)
        self.assertEqual(expected, actual)

    def test_running_time_2(self):
        list_of_songs = [data.Song("Decemberists", "June Hymn", data.Duration(4,30)),
                         data.Song("Broken Bells", "October", data.Duration(3,40)),
                         data.Song("Kansas", "Dust in the Wind", data.Duration(3,29)),
                         data.Song("Local Natives", "Airplanes", data.Duration(3,58))]
        playlist_integers = [0, 2, 1, 4, 0]
        expected = data.Duration(16,9)
        actual = hw2.running_time(list_of_songs, playlist_integers)
        self.assertEqual(expected, actual)


    # Part 5
    def test_validate_route_1(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = True
        actual = hw2.validate_route(city_links, route)
        self.assertEqual(expected, actual)

    def test_validate_route_2(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        route = ['san luis obispo', 'atascadero']
        expected = False
        actual = hw2.validate_route(city_links, route)
        self.assertEqual(expected, actual)

    def test_validate_route_3(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        route = ['atascadero', 'santa margarita', 'san luis obispo']
        expected = True
        actual = hw2.validate_route(city_links, route)
        self.assertEqual(expected, actual)

    def test_validate_route_4(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        route = []
        expected = True
        actual = hw2.validate_route(city_links, route)
        self.assertEqual(expected, actual)

    def test_validate_route_5(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        route = ['san luis obispo']
        expected = True
        actual = hw2.validate_route(city_links, route)
        self.assertEqual(expected, actual)


    # Part 6
    def test_longest_repetition_1(self):
        integers = [1, 1, 2, 2, 1, 1, 1, 3]
        expected = 4
        actual = hw2.longest_repetition(integers)
        self.assertEqual(expected, actual)

    def test_longest_repetition_2(self):
        integers = [1, 1, 2, 2, 2, 1, 1, 3]
        expected = 2
        actual = hw2.longest_repetition(integers)
        self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()
