from django.db import models

# Create your models here.
status_choices = (
    ('disponible', 'disponible'),
    ('Indisponible', 'Indisponible'),
    ('En panne', 'En Panne')
)

class Terminal(models.Model):
    terminal_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    terminal_image = models.ImageField(upload_to='photos/terminals', blank=True)
    kwatt = models.CharField(max_length=50, unique=True)
    connector = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status_choices, blank=True)
    price = models.IntegerField(blank=True)
    is_available = models. BooleanField(default=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.terminal_name