from django.db import models
from django.utils import timezone

# models.Model means it's a Django model, so should be saved in the database

# models.CharField - this is how you define text with a limited number of characters.
# models.TextField - this is for long text without a limit.
# models.DateTimeField - this is a date and time.
# models.ForeignKey - this is a link to another model.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	# def means this is a function/method and publish is the name of the method.
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	# When we call __str__() we get a text with the Post title
	def __str__(self):
		return self.title