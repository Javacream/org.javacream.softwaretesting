import unittest

from duckduckgo_page import SearchPage
class DuckduckgoTest(unittest.TestCase):
  def setUp(self):
    self.search_page = SearchPage()
  def tearDown(self):
    self.search_page.close()    

  def test_title_is_DuckDuckGo(self):
    self.assertIn('DuckDuckGo', self.search_page.get_title())

  def test_search(self):
    search = "Javacream"
    self.search_page.make_search(search)

if __name__ == '__main__':
  unittest.main()