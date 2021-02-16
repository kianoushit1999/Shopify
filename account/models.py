from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
class UserManager(BaseUserManager):

    def _create_user(self, email, password, phone, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, phone=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, phone, **extra_fields)

    def create_superuser(self, email, password, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, phone, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    phone_re = RegexValidator(regex=r'^\+?1?\d{10,15}$',
                              message="Your phone number should be like this format +9999...")
    phone = models.CharField(verbose_name=_("phone_number"), validators=[phone_re], max_length=17, blank=True,
                             help_text="Enter valid phone number because it'll send you a message at once")

    image = models.ImageField(upload_to='images/user', blank=True, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'phone']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Email(models.Model):
    subject = models.CharField(
        verbose_name=_('subject'),
        max_length=128,
    )
    body = models.TextField(
        verbose_name=_('body'),
        blank=True
    )

    user = models.ForeignKey(
        to=User,
        verbose_name=_("user"),
        related_name='receive_email',
        related_query_name='receive_email_q',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'R_Email'
        verbose_name_plural = 'R_Emails'

class Address(models.Model):
    city = models.CharField(_('city'), max_length=128)
    street = models.CharField(_('street'), max_length=128)
    allay = models.CharField(_('allay'), max_length=128)
    zip_code = models.IntegerField(_('zip_code'), blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='address_user',
        related_query_name='address_user_q',
    )

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'address'

class Shop(models.Model):
    name = models.CharField(_('shop_name'), max_length=100)
    slug = models.SlugField(_('slug'), db_index=True, unique=True)
    description = models.TextField(_('description'), blank=True)
    image = models.ImageField(upload_to='images/shop')
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='shop_user',
        related_query_name='shop_user',
    )

    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shops'