from django.contrib.auth.models import User
from django.db import models


# UserModel = get_user_model()
#
#
# class ProfileModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
#     about = models.CharField(max_length=255, null=True, blank=True)
#
#     def __repr__(self):
#         return self.user.get_full_name()
#
#     def __str__(self):
#         return self.user.get_full_name()
#
#     class Meta:
#         verbose_name = "profile"
#         verbose_name_plural = "profiles"


class BlogHashtagModel(models.Model):
    title = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog hashtag'
        verbose_name_plural = 'blog hashtags'


class BlogModel(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='blogs',
        null=True, blank=True
    )
    image = models.ImageField(upload_to="blogs")
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()

    hashtags = models.ManyToManyField(BlogHashtagModel, related_name="blogs")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
