from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
        # return reverse('category', args=[str(self.slug)])

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def get_absolute_url(self):
        return reverse('brand', args=[str(self.slug)])

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Наменование')
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(verbose_name='Наличие', default=True)
    brand = models.ManyToManyField(Brand, related_name='brand', blank=True, null=True)
    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='product', verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # user =
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('product', args=[self.id, self.slug])
