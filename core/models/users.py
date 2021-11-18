from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from core.models.locations import Location

USER_TYPE_CHOICES = [("student", "student"), ("teacher", "teacher"), ("counsellor", "counsellor")]


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User Must Have an Email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(email, username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=225, unique=True)
    secondary_email = models.EmailField(max_length=225, null=True, blank=True)
    username = models.CharField(max_length=191)
    first_name = models.CharField(max_length=191, null=True, blank=True)
    last_name = models.CharField(max_length=191, null=True, blank=True)
    full_name = models.CharField(max_length=191, null=True, blank=True)
    profile_image = models.ImageField(upload_to="image/", null=True, blank=True)
    photo_url = models.CharField(max_length=199, default="")
    area_code = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_user = models.BooleanField(default=True)
    approved = models.BooleanField(null=True, default=False)
    is_available = models.BooleanField(default=True, null=True, blank=True)
    is_locked = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified_mobile = models.BooleanField(default=False)
    is_verified_email = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True)
    address = models.CharField(max_length=199, blank=True, null=True)
    city = models.CharField(max_length=191, null=True, blank=True)
    country = models.CharField(max_length=191, null=True, blank=True)
    state = models.CharField(max_length=191, null=True, blank=True)
    role = models.CharField(max_length=191, choices=USER_TYPE_CHOICES, null=True, blank=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_verify = models.BooleanField(default=False)
    block_by_admin = models.BooleanField(default=False)
    facebook_id = models.CharField(null=True, max_length=191, blank=True)
    google_id = models.CharField(null=True, max_length=191, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    REQUIRED_FIELDS = [
        "username",
    ]
    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"

    def get_username(self):
        return self.email

    def __str__(self):
        return self.email
