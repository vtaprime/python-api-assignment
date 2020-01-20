from django.db import models


class CustomerTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.BigIntegerField()
    updated_at = models.BigIntegerField()
    is_deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_tab'
