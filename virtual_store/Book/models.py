from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from pathlib import Path
from django.core.files import File
import random



concatenar_con_aleatorios = lambda texto: texto + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
#genera uuid



class Book_File(models.Model):

    file = models.FileField(upload_to='media')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):

        value = concatenar_con_aleatorios("file")
        state = True

        while state:
            
            try:
                aux = Book_File.objects.get(slug=value)
                value = concatenar_con_aleatorios("file")
            
            except:

                state = False

        self.slug = slugify(value, allow_unicode=True)
        super(Book_File, self).save(*args, **kwargs)



class Preview_Book_File(models.Model):

    book_original = models.ForeignKey(Book_File, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
    #genera un uuid y lo guarda         
        value = concatenar_con_aleatorios("preview")
        state = True
        while state:
            
            try:
                aux = Preview_Book_File.objects.get(slug=value)
                value = concatenar_con_aleatorios("preview")
            
            except:

                state = False

        self.slug = slugify(value, allow_unicode=True)
        super(Preview_Book_File, self).save(*args, **kwargs)


class Image_Book(models.Model):

    imagen = models.ImageField('media')
    slug = models.SlugField(unique=True, blank=True)

def save(self, *args, **kwargs):
    #genera un uuid y lo guarda         
        value = concatenar_con_aleatorios("file")
        state = True
        while state:
            
            try:
                aux = Image_Book.objects.get(slug=value)
                value = concatenar_con_aleatorios("file")
            
            except:

                state = False

        self.slug = slugify(value, allow_unicode=True)
        super(Image_Book, self).save(*args, **kwargs)


class Pre_saved_PDF(models.Model):

    pdf = models.OneToOneField(Book_File, on_delete=models.CASCADE)
    preview_pdf = models.OneToOneField(Preview_Book_File, on_delete=models.CASCADE)
    #imagen = models.OneToOneField(Image_Book, on_delete=models.CASCADE)
    

class Author(models.Model):

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
         
        value = concatenar_con_aleatorios(self.nombre + self.apellido)
        state = True
        while state:
            
            try:
                aux = Author.objects.get(slug=value)
                value = concatenar_con_aleatorios("file")
            
            except:

                state = False

        self.slug = slugify(value, allow_unicode=True)
        super(Author, self).save(*args, **kwargs)


class Book(models.Model):

    name = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    preview_book = models.ForeignKey(Preview_Book_File, on_delete=models.CASCADE)
    book_file = models.ForeignKey(Book_File, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    is_free = models.BooleanField()
    image = models.ImageField()
    merchant_uuid = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True, default="")

    def save(self, *args, **kwargs):
         
        value = concatenar_con_aleatorios("name")
        state = True
        while state:
            
            try:
                aux = Book.objects.get(slug=value)
                value = concatenar_con_aleatorios("book")
            
            except:

                state = False

        self.slug = slugify(value, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)


class Noticia(models.Model):

    titulo = models.CharField( max_length=255)
    imagen = models.ImageField(default="P1190517_uJ5T2cc.JPG")
    texto = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
         
        value = concatenar_con_aleatorios("name")
        state = True
        while state:
            
            try:
                aux = Noticia.objects.get(slug=value)
                value = concatenar_con_aleatorios("noticia")
            
            except:

                state = False

        self.slug = slugify(value, allow_unicode=True)
        super(Noticia, self).save(*args, **kwargs)


"""
@receiver(post_save, sender=Book_File)
def save_Preview_Book_File(sender, instance, **kwargs):
    #Despues de crear un documento se crea el preview y la imagen de portada.
    orig_pdf = File()
    aux = Pre_saved_PDF.objects.create(pdf=instance, preview_pdf=preview, imagen=imagen)
    aux.save()    
"""

@receiver(post_save, sender=Book)
def delete_pre_saved_pdf(sender, instance, **kwargs):

    pre = Pre_saved_PDF.objects.get(pdf=instance.book_file)
    pre.delete()
