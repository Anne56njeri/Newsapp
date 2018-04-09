import unittest
from app.models import Articles

class Articles(unittest.TestCase):
    def setUp(self):
        self.new_article =Articles(2345,'bbc news','mark','2017','url','topheadlines','urltoimage','here is an article')
def test(self):
    self.asserTrue(isinstace(self.new_article,Articles))
