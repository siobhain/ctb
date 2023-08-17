from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Live"))
WORKCATEGORY = ((1, "Manual Work"), (2, "Admin Work"), (3, "Campaign Work"), (4, "Other"))
ROI = (('087', '087'), ('086', '086'), ('085', '085'), ('083', '083'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # firstname = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
    # surname = models.CharField(max_length=15, validators=[MinLengthValidator(2)])
    firstname = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    mobile_prefix = models.CharField(choices=ROI, max_length=3)
    mobile_number = models.CharField(max_length=7, default='1234567', validators=[RegexValidator(regex='^\d{7}$', message='7 digits please')])
    gate_code = models.CharField(max_length=4, default='1234')


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
