#type:ignore
from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicate wishlist entries

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delivery = models.BooleanField(default=False)
    delivery_name = models.CharField(max_length=100, blank=True)
    delivery_phone = models.CharField(max_length=20, blank=True)
    delivery_address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    





class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    profile_link = models.URLField()
    hear_about = models.CharField(max_length=50)
    governorate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=50)
    floor = models.CharField(max_length=10)
    apartment = models.CharField(max_length=10)
    agreed_to_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class IndividualProfile(BaseProfile):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    camera_system = models.CharField(max_length=100, blank=True)
    professional_category = models.CharField(max_length=50)
    portfolio_link = models.URLField()
    id_front = models.FileField(upload_to='ids/individual/')
    id_rear = models.FileField(upload_to='ids/individual/')
    other_id = models.FileField(upload_to='ids/individual/')

class CorporateProfile(BaseProfile):
    company_name = models.CharField(max_length=100)
    company_address = models.TextField()
    company_website = models.URLField(blank=True)
    company_social = models.URLField()
    ceo_name = models.CharField(max_length=100)
    ceo_phone = models.CharField(max_length=20)
    ceo_email = models.EmailField()
    ceo_id_front = models.FileField(upload_to='ids/corporate/')
    ceo_id_rear = models.FileField(upload_to='ids/corporate/')
    authorized_name = models.CharField(max_length=100)
    authorized_phone = models.CharField(max_length=20)
    authorized_email = models.EmailField()
    authorized_id_front = models.FileField(upload_to='ids/corporate/')
    authorized_id_rear = models.FileField(upload_to='ids/corporate/')
    tax_certificate = models.FileField(upload_to='docs/corporate/')
    commercial_registration = models.FileField(upload_to='docs/corporate/')

class StudioProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField(default="temp@example.com")
    studio_name = models.CharField(max_length=100)  # ✅ add this field
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ add this field

    def __str__(self):
        return self.studio_name
