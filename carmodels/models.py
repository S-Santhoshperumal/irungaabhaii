from django.db import models

class Compactcar(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    
class Sedans(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    

class Suv(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    

class Vans(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    


class Trucks(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    


class Luxurycars(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    


class Convertibles(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    

class Electriccars_Hybrids (models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    
class Sportscars(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
    

class Motorcycles(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='carsmodels/', blank=True, null=True)  # Store images in /media/carmodels/

    def __str__(self):
        return self.name
