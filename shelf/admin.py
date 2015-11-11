from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from shelf.models import Author, Publisher, Book, BookCategory, BookEdition, BookItem

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookCategory)
admin.site.register(Publisher)
admin.site.register(BookEdition)
admin.site.register(BookItem)