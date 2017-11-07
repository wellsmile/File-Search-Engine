'''
Created on 2017年11月7日

@author: caoxiaocheng
'''
class FileInfo(object):
    def __init__(self, title, date, path, content, author, type):
        self.title = title
        self.date = date
        self.path = path
        self.content = content
        self.author = author
        self.type = type