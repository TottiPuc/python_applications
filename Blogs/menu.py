# -*- coding: utf-8 -*-
from models.database import Database
from models.blog import Blog

class Menu(object):
        
    """ask for the user name
    check if they`ve already got an account
    if not, prompt them to create one"""
    
    def __init__(self):
        self.author=input("Enter your author name: ")
        self.user_blog =None
        if self._user_has_account():
            print("Welcome back {}".format(self.author))
        else:
            self._prompt_user_for_account()
            
            
         
    def _user_has_account(self):
       blog =  Database.find_one(collection='blogs',query={'author':self.author})
       print(blog)
       if blog is not None:
           self.user_blog=Blog.from_mongo(blog['ide'])
           return True
       else:
           return False
    
    
    def _prompt_user_for_account(self):
        title=input("Enter blog title: ")
        description=input("Enter blog description: ")
        blog = Blog(author=self.author,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog=blog
        
    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write =='R':
            self.list_blogs()
            self.view_blog()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("thank you for your visit")
            
    def list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}". format(blog['ide'],blog['title'],blog['author']))
            
    def view_blog(self):
        blog_to_see = input("Enter de ID of the blog you would like to see: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date {}, Title {}\n\n{}".format(post['create_date'], post['title'],post['content']))

        
        