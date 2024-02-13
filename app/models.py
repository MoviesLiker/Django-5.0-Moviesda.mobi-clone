from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category}"


class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    director = models.CharField(max_length=255)
    starring = models.TextField()
    genres = models.TextField()
    quality = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    poster = models.TextField(null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"


class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_size = models.CharField(max_length=255)
    vide_size = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    add_on = models.CharField(max_length=255)
    screenshot = models.TextField(null=True)
    server1 = models.TextField()
    server2 = models.TextField()

    def __str__(self):
        return f"{self.file_name}"
