from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
    


class ContactLink(models.Model):
    PLATFORM_CHOICES = [
        ('whatsapp', 'WhatsApp'),
        ('instagram', 'Instagram'),
        ('email', 'Email'),
        ('phone', 'Teléfono'),
        ('website', 'Sitio Web'),
    ]
    
    platform = models.CharField(
        max_length=20, 
        choices=PLATFORM_CHOICES,
        unique=True
    )
    url = models.URLField(max_length=500)
    display_text = models.CharField(max_length=100, blank=True)
    icon_class = models.CharField(max_length=50, default='bi bi-link')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'platform']
        verbose_name = 'Enlace de Contacto'
        verbose_name_plural = 'Enlaces de Contacto'
    
    def __str__(self):
        return f"{self.get_platform_display()}: {self.url}"