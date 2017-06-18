from django.db import models
from django.utils import timezone


# Create your models here.
class Melody(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    track_id = models.CharField(db_column="track_id", max_length=255, unique=True)
    artist = models.CharField(db_column="artist", max_length=255)
    song = models.CharField(db_column="song", max_length=255)
    date_added = models.DateTimeField(db_column="date_added", default=timezone.now)
    
    class Meta:
        db_table="melody"
        verbose_name="Мелодия"
        verbose_name_plural="Мелодии"
        get_latest_by="id"
        ordering = ['id']
       
    def __str__(self):
        return "%s - %s" % (self.artist,self.song)


class Hear(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
#    song = models.CharField(max_length=255, blank=True, null=True, db_column="song")
    song = models.ForeignKey(Melody, on_delete=models.SET_NULL, blank=True, null=True, db_column="song")
    detail = models.CharField(max_length=255)
    mpfile = models.FileField(upload_to='hear/', null=False, blank=False)
    date_time = models.DateTimeField(db_column="date_time", auto_now_add=True, null=False)

    class Meta:
        db_table="hear"
        verbose_name="KG Shazam"
        verbose_name_plural="KG Shazam"
        get_latest_by = "date_time" 
        ordering = ['-date_time'] 

    def __str__(self):
        return '%s' % self.id

