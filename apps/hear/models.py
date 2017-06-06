from django.db import models


# Create your models here.
class Hear(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    date_time = models.DateTimeField(db_column="date_time", auto_now_add=True, null=False)
    artist = models.CharField(db_column="artist", default=0, max_length=255, null=False, blank=False)
    song = models.CharField(db_column="song", max_length=255, default=0, null=False)
    tack_id = models.CharField(db_column="track_id", max_length=255, default=0, null=False)
    file = models.FileField(upload_to='hear', null=False, blank=False)

    class Meta:
        db_table="hear"
        verbose_name="KG Shazam"
        verbose_name_plural="KG Shazam"
        get_latest_by = "date_time" 
        ordering = ['-date_time'] 

    def __str__(self):
        return '%s' % self.id

