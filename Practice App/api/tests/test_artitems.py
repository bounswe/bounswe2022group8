import unittest
from ..tests import view_artitems 
import xmlrunner

class TestArtItem(unittest.TestCase):
    # preparing to test
    def setUp(self):
        # setting up for the test
        print("TestArtItem:setUp_:begin")

        # do something
        print("TestArtItem:setUp_:end")

    def tearDown(self):
        # cleaning up after the test
        print("TestArtItem:setUp_:begin")
        # do something
        print("TestArtItem:setUp_:end")

    if __name__=='__main__':
        # create a runner t osee the output test reports
        runner = xmlrunner.XMLTestRunner(output='./reports/xml')
        unittest.main(testRunner=runner)