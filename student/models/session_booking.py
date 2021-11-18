from django.db import models
from core.models.users import User
from counsellor.models.session_model import Session


class SessionBooking(models.Model):
    """
            Student booking session model.
    """
    transaction_id = models.CharField(max_length=191,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_session_user',null=True)
    counsellor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='counsellor_user',null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE,related_name='session_obj',null=True)
    card_number = models.CharField(max_length=191,null=True,blank=True)
    cvv_number = models.PositiveIntegerField(null=True,blank=True)
    expiry_date = models.CharField(max_length=191,null=True,blank=True)
    name_on_card = models.CharField(max_length=191, null=True, blank=True)
    is_booking = models.BooleanField(default=False)
    purchase_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "session_booking"
        verbose_name = "Session_booking"
        verbose_name_plural = "Session_booking"


