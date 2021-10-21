from django.db import models
from django.utils.text import slugify

# Create your models here.

class Adresa(models.Model):
    ulice = models.CharField(max_length=30)
    cislo = models.IntegerField()

class Oddil(models.Model):
    jmeno = models.CharField(max_length=30)
    vlajka = models.BooleanField()
    sidlo = models.OneToOneField(Adresa, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.jmeno

class Skaut(models.Model):
    prezdivka = models.CharField(max_length=100)
    vek = models.IntegerField()
    slug = models.SlugField(primary_key=True, default="", null=False)
    oddil = models.ForeignKey(Oddil, on_delete=models.SET_NULL, null=True,
        related_name="skauti")

    """
    def save(self, *args, **kwargs):
        print("volám save na skautovi")
        self.slug = slugify(self.prezdivka)
        super().save(*args, **kwargs)
    """

    def __str__(self):
        return f"{self.prezdivka}({self.vek})"

    class Meta:
        verbose_name_plural = "Skauti"
        ordering = ['prezdivka']

class Bobrik(models.Model):
    dovednost = models.CharField(max_length=200)
    skaut = models.ManyToManyField(Skaut)

    def __str__(self):
        return self.dovednost




