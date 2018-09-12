from django.db import models

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


    def __str__(self):
        return self.event

class Comments(models.Model):
    nome = models.CharField(max_length=100)
    date = models.DateField()
    comment = models.TextField()

    def __str__(self):
        return self.nome
