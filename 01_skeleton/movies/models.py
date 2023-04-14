from django.db import models


class Movie(models.Model):
    user_id = models.ForeignKey(settings.AUTH.USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH.USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
