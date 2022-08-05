from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(
            self,
            phone,
            password=None,
            is_active=True,
            is_admin=False,
            **kwargs
    ):
        if not phone:
            raise ValueError("Users must have a phone number")

        user_obj = self.model(
            phone=phone,
            active=is_active,
            admin=is_admin,
            **kwargs
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(
            self,
            phone,
            password=None,
            is_active=True,
            is_admin=True,
            **kwargs
    ):
        user = self.create_user(
            phone,
            password=password,
            is_active=is_active,
            is_admin=is_admin,
            **kwargs
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Group:
        ADMINISTRATOR = "Administrator"
        MODERATOR = "Moderator"
        STUDENT = "Student"
        PARENT = "Parent"
        TRAINER = "Trainer"

    phone_regex = RegexValidator(
        regex=r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}",
        message='Phone number must be entered in the format: ...',
    )

    parents = models.ManyToManyField('self', related_name='children', symmetrical=False, blank=True)
    trainer = models.ForeignKey('self', related_name='students', on_delete=models.DO_NOTHING, null=True)

    full_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(validators=[phone_regex], max_length=12, unique=True)
    password = models.CharField(max_length=100, null=True)

    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __contains__(self, group_name):
        # Example: User.Group.PARENT in user_object
        group, created = Group.objects.get_or_create(name=group_name)
        return group in self.groups.all()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        return self.full_name + self.phone

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_active(self):
        return self.active


class PhoneOTP(models.Model):
    phone_regex = RegexValidator(
        regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}',
        message='Phone number must be entered in the format: ...',
    )
    phone = models.CharField(validators=[phone_regex], max_length=12, unique=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    count = models.IntegerField(default=0)
    last_modified = models.DateTimeField(auto_now=True)
    used = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.phone) + 'is sent' + str(self.count)

    @property
    def is_used(self):
        return self.used
