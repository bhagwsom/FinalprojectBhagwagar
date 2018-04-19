import unittest
import json
import interactive
import api
import scraping

json_file=open('cache_file_name.json', 'r')
json=json.loads(json_file.read())
json_file.close()

class TestArtists(unittest.TestCase):
    def test_get_info(self):
        test1=api.get_artist_info('Conor Maynard')
        #testing artists name
        self.assertEqual(test1[1], 'Conor Maynard' )
        #testing following count
        self.assertEqual(test1[2], 1121938 )
        #testing popularity
        self.assertEqual(test1[3], 73)
        #testing the id in order to make sure the link is correct for scraping
        self.assertEqual(test1[5], "6mU8ucezzms5I2kNH6HNlu")

    def test_info_2(self):
        test2=api.get_artist_info('2 Chainz')
        #testing artist name
        self.assertEqual(test2[1], '2 Chainz' )
        #testing following count
        self.assertEqual(test2[2], 2591084 )
        #testing popularity
        self.assertEqual(test2[3], 87)
        #testing the id in order to make sure the link is correct for scraping
        self.assertEqual(test2[5],"17lzZA2AlOHwCwFALHttmp")

class TestAlbums(unittest.TestCase):
    def test_get_info(self):
        test1=api.get_album_info('Teenage Dream')
        #testing artists name
        self.assertEqual(test1[2], 'Katy Perry' )
        #testing trackcount
        self.assertEqual(test1[3], 19)
        #testing release Date
        self.assertEqual(test1[4],"2012-03-12")
        #testing popularity
        self.assertEqual(test1[5], 81)
        #testing the id in order to make sure the link is correct for scraping
        self.assertEqual(test1[6],"5BvgP623rtvlc0HDcpzquz")

    def test_info_2(self):
        test2=api.get_album_info("Culture II")
        #testing artists name
        self.assertEqual(test2[2], "Migos" )
        #testing trackcount
        self.assertEqual(test2[3], 24)
        #testing release Date
        self.assertEqual(test2[4],"2018-01-26")
        #testing popularity
        self.assertEqual(test2[5], 93)
        #testing the id in order to make sure the link is correct for scraping
        self.assertEqual(test2[6], "7fd7SEK25VS3gJAUgSwL6y")

if __name__ == '__main__':
    unittest.main()
