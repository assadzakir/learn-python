# Object Oriented Programming

print('=============================================')


#  Special Methods

class Book(object):
    def __init__(self, title, author, pages):
        print('A book has been created')

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title %s' % self.title

    def __len__(self):
        return self.pages

    def __del__(self):
        return 'Book is gone'


b = Book('Python', 'Assad', 505)

print(b)  # "Title Python" because of special method __str__

print(len(b))  # 505 because of __len__ method

# deleting
del b

# print(b.title)  # NameError: name 'b' is not defined
