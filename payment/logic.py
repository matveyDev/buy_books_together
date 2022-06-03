from books.models import BooksForBuy

def get_emails(book_pk):
    book = BooksForBuy.objects.get(pk=book_pk)
    emails = []
    queryset_emails = book.buyers.values_list('email')
    for email in queryset_emails:
        emails += email

    return emails