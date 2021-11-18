from django.db import models
from core.models.users import User

class UserStatus(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} -- {self.active_status}'

    def save(self, *args, **kwargs):
        print("triggered")
        super(UserStatus, self).save(*args, **kwargs)