from django.db import models


# ADDRESS_CHOICES = (
#     ( 'Qibray', 'Qibray' ),
#     ( 'Yunsobot', 'Yunsobot' ),
#     ( 'Olmazor', 'Olmazor' ),
#     ( 'Chorsuv', 'Chorsuv' ),
#     ( 'Chilonzor', 'Chilonzor' ),
# )


class Order(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=250)
    liters = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return self.name
