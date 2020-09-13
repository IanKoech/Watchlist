import unittest
from app.models import Movie
Movie=movie.Movie

class MovieTest(unittest.TestCase):
    """
    Test class to test the behaviour of the movie class
    """
    def setUp(self):
        """
        Set up method that runs before every test
        """
        #Set-up method instantiates Movie class to make self.new_movie an object
       self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

if __name__=="__main__":
    unittest.main()