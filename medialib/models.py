from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

"""
These lines bring in necessary tools from Django's library.

from django.conf import settings: Imports your project's configuration settings. This is used later to refer to the correct User model.

from django.db import models: Imports the module that allows you to define database structures (tables, columns, relationships).

from django.utils import timezone: Imports Django's utility for handling dates and times, ensuring they are timezone-aware (e.g., handling UTC vs. local time)."""

# Create your models here.

"""class Post: Defines the name of the object. In the database, Django will likely create a table named appname_post.

models.Model: This indicates inheritance. By passing models.Model into the class, you are telling Django that this is a special class that should be saved to the database."""
class MediaItem(models.Model):
    # Primary Key (media_id)
    media_id = models.AutoField(primary_key=True)

    # Foreign Key (user_id)
    # We name the field 'user'. Django creates the DB column 'user_id' automatically.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='media_items'
    )

    # Basic Text Fields
    titulo = models.CharField(max_length=255)
    origin = models.CharField(max_length=200, help_text="Autor, banda, estúdio ou realizador")

    # Enums / Choices (media_type & status)
    class MediaType(models.TextChoices):
        GAME = 'GAME', 'Game'
        BOOK = 'LIVRO', 'Livro'
        MUSIC = 'MUSICA', 'Música'
        MOVIE = 'FILME', 'Filme'
        SERIES = 'SERIE', 'Série'
        ANIME = 'ANIME', 'Anime'

    media_type = models.CharField(
        max_length=10,
        choices=MediaType.choices,
        default=MediaType.GAME
    )

    class Status(models.TextChoices):
        BACKLOG = 'BACKLOG', 'Backlog'
        IN_PROGRESS = 'EM_CURSO', 'Em curso'
        COMPLETED = 'CONCLUIDO', 'Concluído'
        DROPPED = 'ABANDONADO', 'Abandonado'

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.BACKLOG
    )

    # Rank (0-10)
    rank = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Nota pessoal de 0 a 10"
    )

    # Comment and Dates
    comment = models.TextField(blank=True, null=True) # Optional field
    post_date = models.DateTimeField(auto_now_add=True) # Sets time automatically on creation
    
    def __str__(self):
        return f"{self.titulo} ({self.get_media_type_display()})"