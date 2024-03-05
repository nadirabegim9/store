from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Дополнительные поля можно добавить здесь
    pass

    def __str__(self):
        return self.username


class Brand(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание')
    color = models.CharField(max_length=50)
    screen_size = models.CharField(max_length=32, verbose_name='размер экрана')
    screen_technology = models.CharField(max_length=50,
                                         verbose_name='технология, используемая на экране (например, OLED)')
    processor = models.CharField(max_length=50, verbose_name='процессор')
    rom = models.IntegerField()
    ram = models.IntegerField(verbose_name="количество ядер")
    camera_resolution = models.CharField(max_length=50)
    video_resolution = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    warranty = models.IntegerField()

    def __str__(self):
        return self.name


class ProductPhotos(models.Model):
    product_photo = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                help_text="Rate the item with 0 to 6 stars.",
                                verbose_name="Rating")

    def __str__(self):
        return f"{self.product} - {self.user} - {self.stars} stars"



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.product}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, default=1, related_name='product_favorite')
    summ_products = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.product}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)

    def __str__(self):
        return self.user

