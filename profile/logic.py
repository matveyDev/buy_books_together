from django.contrib.auth import get_user_model

def age_is_valid(age):
    return age != ''     

def photo_is_valid(photo):
    return photo != None

def username_is_valid(username, pk):
    Users = get_user_model().objects.all()
    current_user = Users.get(pk=pk)

    if current_user.username == username:
        return True
        
    return not Users.filter(username=username)