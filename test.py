import unittest
import app

class TestApp(unittest.TestCase):
    """
    Test suit for app
    """

    def test_can_create_amazon_link(self):
        """
        Test to see if it creates a links correctly if user did not provide 
        url to the book on amazon website
        """
        
         # Test no link provided
        link1 = app.generate_amazon_link('Once upon a time', 'John Smith','')
        
        self.assertEqual(link1, 
        'https://www.amazon.co.uk/s?k=Once+upon+a+time+John+Smith&tag=joanna')
        
        # Test no link provided and '&' symbol in the book title
        link2 = app.generate_amazon_link('Once upon & time', 'John Smith','')
        
        self.assertEqual(link2, 
        'https://www.amazon.co.uk/s?k=Once+upon+and+time+John+Smith&tag=joanna')
        
        # Test no link provided and author's last name is not capital
        link3 = app.generate_amazon_link('Once upon a time', 'John smith','')
        
        self.assertNotEqual(link3, 
        'https://www.amazon.co.uk/s?k=Once+upon+a+time+John+Smith&tag=joanna')
  
    def test_can_edit_amazon_link(self):
        """
        Test to see if it will add ref tag to url provided by the user
        """
        
        # Test direct link to product
        link1 = app.generate_amazon_link('Carrie', 'Stephen King',
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667')
        
        self.assertEqual(link1, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667/?tag=joanna')
        
        # Test link from search
        link2 = app.generate_amazon_link('Carrie', 'Stephen King',
        'https://www.amazon.com/Carrie-Stephen-King/dp/B002C6LIGU/ref=sr_1_9?crid=36RCLYEH6RIZ2&keywords=carrie+stephen+king&qid=1576674670&s=books&sprefix=carrie+step%2Cstripbooks-intl-ship%2C216&sr=1-9')
        
        self.assertEqual(link2, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/B002C6LIGU/ref=sr_1_9?crid=36RCLYEH6RIZ2&keywords=carrie+stephen+king&qid=1576674670&s=books&sprefix=carrie+step%2Cstripbooks-intl-ship%2C216&sr=1-9&tag=joanna')
    
        # Test link with different author and title information
        link3 =  link1 = app.generate_amazon_link('Carrie', 'John Smith',
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667')
        
        self.assertEqual(link3, 
        'https://www.amazon.com/Carrie-Stephen-King/dp/0307743667/?tag=joanna')

    def test_placeholder_link(self):
        '''
        Test if placeholder is inserted in cases when user does not provide a link
        to the cover image
        '''
        
        # Test if link is not provided
        cover1 = app.generate_cover('')
    
        self.assertEqual(cover1, 
        'https://via.placeholder.com/250x350.png?text=No+image+available')
    
        # Test when incorrect link is provided i.e. without extension
        cover2 = app.generate_cover('https://images-na.ssl-images-amazon.com/images/I/71JqAKE52ZL')
        
        self.assertEqual(cover2, 
        'https://via.placeholder.com/250x350.png?text=No+image+available')
        
        # Test when link is provided
        cover3 = app.generate_cover('https://images-na.ssl-images-amazon.com/images/I/71JqAKE52ZL.jpg')
    
        self.assertEqual(cover3, 
        'https://images-na.ssl-images-amazon.com/images/I/71JqAKE52ZL.jpg')
        

if __name__ == '__main__':
    unittest.main()