# -*- coding: utf-8 -*-
from models.database import Database
import uuid, datetime

class Post(object):
    
    def __init__(self,blog_id,title,content,author,date=datetime.datetime.now() ,ide=None):
        self.blog_id=blog_id
        self.title=title
        self.author=author
        self.content=content
        self.create_date=date
        self.ide=uuid.uuid4().hex if ide is None else ide
        
        
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())
    
    def json(self):
        return {'ide':self.ide,
                'blog_id':self.blog_id,
                'author':self.author,
                'content':self.content,
                'title':self.title,
                'create_date':self.create_date
                }
    
    @classmethod
    def from_mongo(cls,ide):
       post_data = Database.find_one(collection='posts',query={'ide':ide})
       return cls(blog_id=post_data['blog_id'],
                  title=post_data['title'],
                  content=post_data['content'],
                  author=post_data['author'],
                  date=post_data['create_date'],
                  ide=post_data['ide'])
    
    
    @staticmethod
    def from_blog(ide):
        return [ post for post in Database.find(collection='posts',query={'blog_id':ide})]