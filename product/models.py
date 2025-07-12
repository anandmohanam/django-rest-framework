from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            return round(sum([r.rating for r in reviews]) / reviews.count(), 2)
        return None

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'user'], name='unique_review_per_user')
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"
