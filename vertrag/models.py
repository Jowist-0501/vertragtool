from django.db import models

# Create your models here.

class Firma(models.Model):
    id = models.AutoField(primary_key=True)
    firma = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    plz = models.IntegerField()
    ort = models.CharField(max_length=100)

    def __str__(self):
        return self.firma
    

class Standort(models.Model):
    id = models.AutoField(primary_key=True)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, related_name='standorte')
    bezeichnung = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bezeichnung} ({self.firma.firma})"


class Taetigkeit(models.Model):
    bezeichnung = models.CharField(max_length=100)

    def __str__(self):
        return self.bezeichnung

class Vertragsart(models.Model):
    bezeichnung = models.CharField(max_length=100)

    def __str__(self):
        return self.bezeichnung

class Lohnart(models.Model):
    bezeichnung = models.CharField(max_length=100)

    def __str__(self):
        return self.bezeichnung


class Vertrag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
    mitarbeiter = models.CharField(max_length=100)
    mitarbeiter_adresse = models.CharField(max_length=100)
    mitarbeiter_plz = models.IntegerField()
    mitarbeiter_ort = models.CharField(max_length=100)
    beginn = models.DateField()
    taetigkeit = models.ForeignKey(Taetigkeit, on_delete=models.SET_NULL, null=True)
    einsatzort = models.ForeignKey(Standort, on_delete=models.SET_NULL, null=True)
    vertragsart = models.ForeignKey(Vertragsart, on_delete=models.SET_NULL, null=True)
    lohnart = models.ForeignKey(Lohnart, on_delete=models.SET_NULL, null=True)
    arbeitsstunden = models.DecimalField(max_digits=10, decimal_places=2)
    urlaub = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.mitarbeiter} + {self.vertragsart}+'vertrag' + {self.firma}"

