from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager)


class SuperUserManager(BaseUserManager):
    def create_user(self, mobile, password, is_active=True, is_staff=False, is_superuser=False):
        if mobile is None:
            raise ValueError("Mobile is required")
        if password is None:
            raise ValueError("Password is required")
        user = self.model(mobile=mobile)
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_staff(self, mobile, password):
        user = self.create_user(mobile, password, is_staff=True)
        return user

    def create_superuser(self, mobile, password):
        user = self.create_user(mobile, password, is_staff=True, is_superuser=True)
        return user


class SuperUser(AbstractBaseUser):
    mobile = models.CharField(max_length=10,
                              unique=True,
                              blank=False,
                              null=False)
    active = models.BooleanField(default=False,
                                 blank=False,
                                 null=False)
    staff = models.BooleanField(default=False,
                                 blank=False,
                                 null=False)
    superuser = models.BooleanField(default=False,
                                 blank=False,
                                 null=False)

    USERNAME_FIELD = 'mobile'

    objects = SuperUserManager()

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.mobile
