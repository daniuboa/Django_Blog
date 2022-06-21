from email.policy import default
from unicodedata import category
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
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
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

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
# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Sites'

    def __str__(self):
        return self.name

# New user model
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='user/avatars/%Y/%m/%d/',
        default='user/avatars/default.jpg',
    )
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=100, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. Users'

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = '3. Categories'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = '4. Tags'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = RichTextField()
    featured_image = models.ImageField(
        upload_to='posts/featured_images/%Y/%m/%d/')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    # Each post can receive likes from multiple users, and each user can like multiple posts
    likes = models.ManyToManyField(User, related_name='post_like')

    # Each post belong to one user and one category.
    # Each post has many tags, and each tag has many posts.
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = '5. Posts'

    def __str__(self):
        return self.title

    def get_number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    # Each comment can receive likes from multiple users, and each user can like multiple comments
    likes = models.ManyToManyField(User, related_name='comment_like')

    # Each comment belongs to one user and one post
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = '6. Comments'

    def __str__(self):
        if len(self.content) > 50:
            comment = self.content[:50] + '...'
        else:
            comment = self.content
        return comment

    def get_number_of_likes(self):
        return self.likes.count()