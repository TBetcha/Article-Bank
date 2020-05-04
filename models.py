from django.db import models
from django.urls import reverse

#models is where I will model the database

# use char_field with small strings
#can define forgeign and primary keys in here. On delete makes it that if ever delete we delete all references
#  default makes it ok that we have values in here already
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
        default = 1,
    )
    photo = models.ImageField(upload_to="gallary",
    default="drop-bear.png")


    #when someone tries to print the obj they'll print the title
    def __str__(self):
        return self.title

# should add this to every model. I forget why
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])