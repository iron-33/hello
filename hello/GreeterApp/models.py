from django.db import models
class Name(models.Model):
    name=models.CharField(max_length=160, db_index=True)
    date_pub=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    