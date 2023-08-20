from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Live"))
WORKCATEGORY = ((1, "Manual Work"), (2, "Admin Work"), (3, "Campaign Work"), (4, "Other"))
ROI = (('087', '087'), ('086', '086'), ('085', '085'), ('083', '083'))

class Profile(models.Model):
    # A user profile model to hold firstname, surname, mobile
    # & a default gate code which in future version will be
    # set by a security system via API
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    mobile_prefix = models.CharField(choices=ROI, max_length=3)
    mobile_number = models.CharField(max_length=7, default='1234567', validators=[RegexValidator(regex='^\d{7}$', message='7 digits please')])
    gate_code = models.CharField(max_length=4, default='1234')

    def __str__(self):
        return self.user.username

    # Adapted from CI Boutique Ado : create_or_update_user_profile
    # A signal handler function that creates/updates Profile instance whenever
    # there is a save (new or update) on a User instance

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.profile.save()


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
