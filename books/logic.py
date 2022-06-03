def end_goal(current, finish):
    return current >= finish

def get_emails(book):
    emails = []
    queryset_emails = book.buyers.values_list('email')
    for email in queryset_emails:
        emails += email
    
    return emails