from django.db.models import Q

def get_correct_queryset(query, Model):
    queryset = Model.objects.filter(
        Q(title__icontains=query)
        | Q(description__icontains=query) 
        | Q(category__title__icontains=query)
    )

    return queryset