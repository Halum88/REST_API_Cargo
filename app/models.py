from tortoise.models import Model
from tortoise import fields


class Tariff(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=255)
    rate = fields.DecimalField(max_digits=8, decimal_places=4)
