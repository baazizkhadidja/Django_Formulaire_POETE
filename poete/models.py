# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DateNaissance(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    date_naissance = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DATE_NAISSANCE'


class NomPoete(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nom = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NOM_POETE'


class PrenomPoete(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    prenom = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PRENOM_POETE'


class TableMere(models.Model):
    id = models.SmallIntegerField(blank=True, primary_key=True)
    id_nom_poete = models.SmallIntegerField(blank=True, null=True)
    id_prenom_poete = models.SmallIntegerField(blank=True, null=True)
    id_poeme = models.SmallIntegerField(blank=True, null=True)
    id_date_naissance = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TABLE_MERE'


class TitrePoeme(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    statut = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TITRE_POEME'
