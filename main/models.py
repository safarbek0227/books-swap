from django.db import models
from django.conf import settings
from account.models import User
from main.slug import unique_slugify


# Create your models here.
class Genre(models.Model):
    title = models.CharField("Title", max_length=256)
    slug = models.SlugField("Slug", max_length=256, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "genre"
        verbose_name = "genre"
        verbose_name_plural = "genres"

class Book(models.Model):
    ADDRESS = (
		('Andijon', 'Andijon'),
		('Namangan', 'Namangan'),
		('Samarqand', 'Samarqand'),
		('Tashkent', 'Tashkent'),
		('Jizzax', 'Jizzax'),
		('Surxondaryo', 'Surxondaryo'),
		('Navoiy', 'Navoiy'),
		('Xorazm', 'Xorazm'),
		('Qashqadaryo', 'Qashqadaryo'),
		('Buxoro', 'Buxoro'),
		('Sirdaryo', 'Sirdaryo'),
		('Fargona', 'Fargona'),
	)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", default=None, null=True)
    slug = models.SlugField("Slug", max_length=256, blank=True, unique=True)	
    title = models.CharField("Title", max_length=256)
    author_pen = models.CharField("Book Author", max_length=100)
    location = models.CharField('loacation', max_length=256,  choices=ADDRESS)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books", default=None, null=True)
    description = models.TextField("Description", max_length=200)
    image = models.ImageField("Image", upload_to="book_images")
    created_at = models.DateTimeField("Created time", auto_now_add=True)
    likes_count = models.PositiveIntegerField("Likes", default=0)
    is_checked = models.BooleanField(default=False)
    is_ban = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    @property
    def image_url(self):
        return f"{settings.HOST}{self.image.url}" if self.image else ""
    def save(self,*args, **kwargs):
        slug = '%s' % (self.title)
        unique_slugify(self, slug)
        try:
            this = Book.objects.get(id=self.id)
            print(type(this))
            if this.image != self.image:
                this.image.delete()

        except: pass
        super(Book, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Book, self).delete(*args, **kwargs)
        storage.delete(path)


    class Meta:
        ordering = ['-id']
        db_table = "book"
        unique_together = ["slug"]
        verbose_name = "book"
        verbose_name_plural = "books"
