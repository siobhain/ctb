from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Suggest"), (1, "Approved"))
WORKCATEGORY = ((0, "All"), (1, "Manual Work"), (2, "Admin Work"), (3, "Campaign Work"))


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=120, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=120, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    category = models.IntegerField(choices=WORKCATEGORY, default=0, blank=False, null=False)
    completed = models.BooleanField(default=False, blank=False, null=False)
    attached_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='task_likes', blank=True)

    def __str__(self):
        return self.description

class Meta:
    ordering = ['-created_on']  # order by latest


def number_of_likes(self):
    return self.likes.count()
