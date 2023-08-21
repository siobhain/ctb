from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Live"))
WORKCATEGORY = ((1, "Manual Work"), (2, "Admin Work"), (3, "Campaign Work"), (4, "Other"))
ROI = (('083', '083'), ('085', '085'), ('086', '086'), ('087', '087'))

class Profile(models.Model):
    # A user profile model to hold firstname, surname, mobile
    # & a default gate code which in future version will be
    # set by a security system via API
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=15, null=False, blank=False)
    surname = models.CharField(max_length=15, null=False, blank=False)
    mobile_prefix = models.CharField(
        choices=ROI, max_length=3, default='---', null=False, blank=False)
    mobile_number = models.CharField(
        max_length=7,
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex='^\d{7}$',
                message='Mobile needs 7 digits please'
            )
        ]
    )
    gate_code = models.CharField(max_length=4, default='1234')

    def __str__(self):
        return self.user.username


class Task(models.Model):
    description = models.CharField(max_length=120, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=120, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    category = models.IntegerField(choices=WORKCATEGORY, default=0, blank=False, null=False)
    completed = models.BooleanField(default=False, blank=False, null=False)
    status = models.IntegerField(choices=STATUS, default=0)
    attached_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='task_likes', blank=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-created_on']  # order by latest (minus)

    def number_of_likes(self):
        return self.likes.count()
