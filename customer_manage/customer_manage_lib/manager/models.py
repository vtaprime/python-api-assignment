from django.db import models


class CustomerTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    updated_at = models.IntegerField()
    created_at = models.IntegerField()
    is_deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_tab'
