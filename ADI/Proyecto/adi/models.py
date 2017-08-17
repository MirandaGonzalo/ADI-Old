from __future__ import unicode_literals
from django.conf import settings
from django.utils import timezone

from django.db import models

class Padre_Tutor(models.Model):
    nombre = models.CharField(max_length=20)
    dni = models.IntegerField()
    email = models.EmailField(max_length=40)
    telefono = models.IntegerField()

class Preceptor(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField(null=False)

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField(primary_key=True)
    preceptor = models.ForeignKey(Preceptor)



#    def count_like(self):
#        return Like.objects.filter(tweet=self).count()
#    def __str__(self):
#        return 'Tweet nro {} - by {}'.format(self.id, self.user)

class Formulario2(models.Model):
    preceptor = models.ForeignKey(settings.AUTH_USER_MODEL)
    nombre_alumno = models.CharField(max_length=20)
    apellido_alumno = models.CharField(max_length=20)
    dni_alumno = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)

class Formulario3(models.Model):
    preceptor = models.ForeignKey(settings.AUTH_USER_MODEL)
    alumno = models.ForeignKey(Alumno)
    fecha = models.DateTimeField(default=timezone.now)