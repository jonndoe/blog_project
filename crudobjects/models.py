from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import uuid

from django.utils import timezone



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


# Create your models here.
class Crudobject(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='crudobjects')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    crudcover = models.ImageField(upload_to='crudcovers/', blank=True) # base img of CRUD object

    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [
            ("special_status", "Can read all crudobjects")
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('crudobject_detail', args=[str(self.id)])


class Comment(models.Model):
    crudobject = models.ForeignKey(
        Crudobject,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('crudobject_list')
