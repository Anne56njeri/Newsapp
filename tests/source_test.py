import unittest
from app.models import Sources

class SOurceTest(unittest.TestCase):
    def setUp(self):
        self.new_source =Sources(1234,'abc news','url','business','us','this is a link')
    def test_instance(self):
        self.asserTrue(isinstace(self.new_source,Sources))    
