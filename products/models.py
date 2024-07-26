from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

class Product(models.Model):
    titles = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to = 'products/', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return self.titles
    
def new_slug(sender, instance, *args, **kwargs):
    if instance.titles and not instance.slug:
        slug = slugify(instance.titles)
        
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.titles, str(uuid.uuid4())[:8])
            )
        instance.slug = slug

pre_save.connect(new_slug, sender = Product)