from django.conf.urls import url
from . import views

"""
assigning a view called post_list to ^$ URL. 
This regular expression will match ^ (a beginning) followed 
by $ (an end) - so only an empty string will match. 
That's correct, because in Django URL resolvers, 
'http://127.0.0.1:8000/' is not a part of the URL. 
This pattern will tell Django that views.post_list is 
the right place to go if someone enters your website at the 
'http://127.0.0.1:8000/' address.

The last part name='post_list' is the name of the URL that 
will be used to identify the view. This can be the 
same as the name of the view but it can also be 
something completely different. 
"""

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]