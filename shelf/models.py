from django.db import models

class Author(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=50)
    
    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name,
            last_name=self.last_name)
    
class Publisher(models.Model):
    name=models.CharField(max_length=70)

    def __str__(self):
        return self.name

class BookCategory(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    #author=models.ForeignKey(Author)
    categories=models.ManyToManyField(BookCategory)
    
    def __str__(self):
        return self.title

class BookEdition(models.Model):
    """
    Wydanie ksiązki
    """
    book=models.ForeignKey(Book)
    publisher=models.ForeignKey(Publisher)
    isbn=models.CharField(max_length=17)
    
    def __str__(self):
        return"{book.title}, {publisher.name}".format(book=self.book,
        publisher=self.publisher)
    

class BookItem(models.Model):
    """
    Egzamplarz
    """
    edition=models.ForeignKey(BookEdition)
    catalogue_number=models.CharField(max_length=30)
    
    
    def __str__(self):
        return "{edition}".format(edition=self.edition)
    
#tesndfnkjdsnjfs