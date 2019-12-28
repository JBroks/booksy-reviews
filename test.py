import unittest
import app


class TestCreateAmazonLink(unittest.TestCase):
    """
    Test to see if it creates a links correctly if user did not provide 
    url to the book on amazon website
    """

    def test_no_link(self):
        
         # Test no link provided
        link = app.generate_amazon_link('Once upon a time', 'John Smith','')
        
        self.assertEqual(link, 
        'https://www.amazon.co.uk/s?k=Once+upon+a+time+John+Smith&tag=joanna')
    
    def test_replace_symbol(self): 
        
        # Test no link provided and '&' symbol in the book title
        link = app.generate_amazon_link('Once upon & time', 'John Smith','')
        
        self.assertEqual(link, 
        'https://www.amazon.co.uk/s?k=Once+upon+and+time+John+Smith&tag=joanna')
    
    def test_name_not_capital(self): 
        
        # Test no link provided and author's last name is not capital
        link = app.generate_amazon_link('Once upon a time', 'John smith','')
        
        self.assertNotEqual(link, 
        'https://www.amazon.co.uk/s?k=Once+upon+a+time+John+Smith&tag=joanna')

class TestAmazonLinkTag(unittest.TestCase): 
    """
        Test to see if it will add ref tag to url provided by the user
    """
    
    def test_direct_amazon_link(self):
        
        # Test direct link to product
        link = app.generate_amazon_link('Carrie', 'Stephen King',
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667')
        
        self.assertEqual(link, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667/?tag=joanna')
    
    def test_amazon_search_link(self):
        
        # Test link from search
        link = app.generate_amazon_link('Carrie', 'Stephen King',
        'https://www.amazon.com/Carrie-Stephen-King/dp/B002C6LIGU/ref=sr_1_9?crid=36RCLYEH6RIZ2&keywords=carrie+stephen+king&qid=1576674670&s=books&sprefix=carrie+step%2Cstripbooks-intl-ship%2C216&sr=1-9')
        
        self.assertEqual(link, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/B002C6LIGU/ref=sr_1_9?crid=36RCLYEH6RIZ2&keywords=carrie+stephen+king&qid=1576674670&s=books&sprefix=carrie+step%2Cstripbooks-intl-ship%2C216&sr=1-9&tag=joanna')
    
    def test_amazon_endswith_backslash(self):
        
        # Test direct link to product with backlash at the end
        link = app.generate_amazon_link('Carrie', 'Stephen King',
        'https://www.amazon.com/Carrie-Stephen-King/dp/B002C6LIGU/')
        
        self.assertEqual(link, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/B002C6LIGU/?tag=joanna')
    
    def test_incorrect_author(self):
        
        # Test link with different author and title information
        # Link provided by user should not be re-create (overwritten)
        link = app.generate_amazon_link('Test', 'John Smith',
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667')
        
        self.assertEqual(link, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667/?tag=joanna')
    
    def test_tag_exists(self):
        
        # Test link that already contains the tag
        link = app.generate_amazon_link('Carrie', 'Stephen King',
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667/?tag=joanna')
        
        self.assertEqual(link, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667/?tag=joanna')

class TestCoverLink(unittest.TestCase): 
    '''
    Test if placeholder is inserted in cases when user does not provide a link
    to the cover image
    '''
        
    def test_placeholder_for_missing_link(self):

        # Test if link is not provided
        cover = app.generate_cover('')
    
        self.assertEqual(cover, 
        'https://via.placeholder.com/250x350.png?text=No+image+available')
    
    def test_missing_extension(self):
        
        # Test when incorrect link is provided i.e. without extension
        cover = app.generate_cover('https://images-na.ssl-images-amazon.com/images/I/71JqAKE52ZL')
        
        self.assertEqual(cover, 
        'https://via.placeholder.com/250x350.png?text=No+image+available')
    
    def test_incorrect_extension(self):
        
        # Test when incorrect extension
        cover = app.generate_cover('https://images-na.ssl-images-amazon.com/images/I/71JqAKE52ZL.txt')
        
        self.assertEqual(cover, 
        'https://via.placeholder.com/250x350.png?text=No+image+available')
    
    def test_link_provided(self):
         
        # Test when link is provided
        cover = app.generate_cover('https://images-na.ssl-images-amazon.com/images/I/71JqAKE52ZL.jpg')
    
        self.assertEqual(cover, 
        'https://images-na.ssl-images-amazon.com/images/I/71JqAKE52ZL.jpg')

if __name__ == '__main__':
    unittest.main()