class Libraryitem:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def display(self):
        print("Libraryitem:",self.title)
class Book(Libraryitem):
    def __init__(self,title,pages):
        super().__init__(title,pages)
    def display(self):
        print("Book:", self.title, "-pages:", self.pages)
    def __add__(self, other):
        return self.pages + other.pages
class Magazine(Libraryitem):
    def __init__(self,title,pages):
        super().__init__(title,pages)
    def display(self):
        print("Magazine:", self.title, "-pages:", self.pages)
b1 = Book("python programming", 150)
m1 = Magazine("tech world", 50)
b1.display()
m1.display()
total_pages=b1+m1
print("total pages:", total_pages)