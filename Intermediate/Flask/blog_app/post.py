import requests

class Post:
    '''Class to handle all posts'''
    
    def __init__(self):
        self.url = 'https://api.npoint.io/8a9a646d51cdf742b827'
        self.response = requests.get(url=self.url)
        self.data = self.response.json()
        
            
    def get_all_posts(self):
        '''Function to return all posts'''
        
        return self.data['posts']
    
    def get_post(self, id):
        '''Function to return a single post'''
        
        # I did 'id-1' since python lists start from index 0
        return self.data['posts'][id-1]
    