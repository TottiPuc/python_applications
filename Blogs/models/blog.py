# -*- coding: utf-8 -*-
import uuid, datetime
from models.post import Post
from models.database import Database

class Blog(object):
    def __init__(self,author,title,description,ide=None):
        self.author=author
        self.title=title
        self.description=description
        self.ide=uuid.uuid4().hex if ide is None else ide
        
        

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")    
        date = input("Enter post date(in format DDMMYY), or leave blank for today: ")
        if date == "":
            date = datetime.datetime.now()
        else:
            date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Post(blog_id=self.ide,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()
    
    def get_posts(self):
        return Post.from_blog(self.ide)
    
    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())
        

    def json(self):
        return {'author':self.author,
                'title':self.title,
                'description' : self.description,
                'ide': self.ide
            }
    
    @classmethod
    def from_mongo(cls,ide):
        
        blog_data = Database.find_one(collection='blogs',query={'ide':ide})
        print("este es el blog",blog_data)
        return cls(author=blog_data['author'],
                     title=blog_data['title'],
                     description=blog_data['description'],
                     ide=blog_data['ide'])