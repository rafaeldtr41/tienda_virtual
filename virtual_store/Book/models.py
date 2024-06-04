from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from pathlib import Path
from Book.pdf_handler import write_preview, extract_image




concatenar_con_aleatorios = lambda texto: texto + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
#genera uuid

class Book_File(models.Model):

    file = models.FileField()
    slug = models.SlugField(unique=True)


class Preview_Book_File(models.Model):

    book_original = models.ForeignKey(Book_File, on_delete=models.CASCADE)
    file = models.FileField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
    #genera un uuid y lo guarda         
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


class Image_Book(models.Model):

    imagen = models.ImageField()
    slug = models.SlugField(unique=True)

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


class Author(models.Model):

    nombre = models.CharField(max_lenght=255)
    apellido = models.CharField(max_lenght=255)
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

    name = models.CharField(max_lenght=255)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    Preview_Book = models.ForeignKey(Preview_Book_File, on_delete=models.CASCADE)
    Book_file = models.ForeignKey(Book_File, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    is_free = models.BooleanField()
    image = models.ForeignKey(Image_Book, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
         
        value = concatenar_con_aleatorios("name")
        state = True
        while state:
            
            try:
                aux = Book.objects.get(slug=value)
                value = concatenar_con_aleatorios("file")
            
            except:

                state = False

        self.slug = slugify(value, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)


@receiver(post_save, sender=Book_File)
def save_Preview_Book_File(sender, instance, **kwargs):
    #Despues de crear un documento se crea el preview y la imagen de portada.
    aux_path = instance.file
    dir_path = aux_path.parent
    state = True
    value = concatenar_con_aleatorios("preview_file")
    
    while state:
        #Confirmar el uuid
        try:
            aux = Preview_Book_File.objects.get(slug = value)
            value = concatenar_con_aleatorios("preview_file")

        except:
            state = False
    
    dir = write_preview(aux_path, dir_path, value)
    aux = Preview_Book_File.objects.create(book_original=instance, file=dir)
    aux.save() # se guarda

    value = concatenar_con_aleatorios("imagen")
    state = True
    while state:
        # lo  mismo con la imagen
        try:
            aux = Image_Book.objects.get(slug = value)
            value = concatenar_con_aleatorios("imagen")

        except:
            state = False
    

    dir = extract_image(dir, dirpath, value)
    aux = Image_Book.objects.create(image=dir)
    aux.save()
    