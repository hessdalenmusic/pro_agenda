from django.db import models
from django.utils import timezone
from libgravatar import Gravatar

class Event(models.Model):

    priorities_list = (
                          ('0','sem prioridade'),
                        ('1','normal'),
                         ('2','Urgente'),
                        ('3','muito urgente'),
                        ('4', 'ultra mega urgente')
    )


    date = models.DateField()
    event = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=priorities_list)

    def Meta:
        ordering = ("-date", '-priority','event')

    def number_of_comments(self0):
        return self.comments_event.count()

    def __str__(self):
        return self.event

class Comments(models.Model):
    """comentario efetuados em uma determinado evento"""
    author = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=160)
    commented = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comment_event')

    """retornar apartir do email, configurando o Gravatar"""
    def avatar(self):
        g = Gravatar(self.email)
        return g.get_image(default="identicon")

    def __str__(self):
        return "{} comentou em {:%c}".format(self.author, self.commented)
