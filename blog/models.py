from django.conf import settings
from django.db import models
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    content = models.TextField()
    is_active = models.BooleanField()
    picture = models.ImageField(upload_to='uploads/')
    def publish(self):
	    self.save()
    def __str__(self):
	    return self.title

class Article(models.Model):
	title = models.CharField(max_length=200)
	abstract = models.TextField()
	content = models.TextField()
	picture = models.ImageField(upload_to='uploads/')
	def publish(self):
	    self.save()
	def __str__(self):
	    return self.title
		
class New(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	def publish(self):
	    self.save()
	def __str__(self):
	    return self.title
		
class Signup(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #class Meta:
     #   unique_together = ('course', 'email',)
    def publish(self):
        self.save()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    def publish(self):
        self.save()
    def __str__(self):
        return self.name

