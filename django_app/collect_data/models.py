from django.db import models

# Create your models here.
class Floorsheet(models.Model):
    contractId = models.PositiveBigIntegerField(primary_key=True)
    stockSymbol = models.CharField(max_length=20)
    buyerMemberId = models.CharField(max_length=20)
    sellerMemberId = models.CharField(max_length=20)
    contractQuantity = models.PositiveIntegerField()
    contractRate = models.PositiveIntegerField()
    contractAmount = models.PositiveBigIntegerField()
    businessDate = models.DateField()
    tradeBookId = models.CharField(max_length=20)
    stockId = models.CharField(max_length=20)
    buyerBrokerName = models.CharField(max_length=100)
    sellerBrokerName = models.CharField(max_length=100)
    tradeTime = models.DateTimeField()
    securityName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.businessDate)