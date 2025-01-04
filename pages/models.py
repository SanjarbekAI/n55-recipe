from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactModel(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
