from django.db import models

# Create your models here.



class Note(models.Model):
    note_Title = models.CharField('Title Note', max_length = 200)
    note_description = models.TextField('Content Note', max_length = 255)
    finished_note = models.BooleanField('Finished Task')
    user_creator = models.CharField('User Create Note', max_length = 150, blank = True)