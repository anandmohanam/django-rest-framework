from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'average_rating']

    def get_average_rating(self, obj):
        return obj.average_rating() or "No ratings yet"

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'feedback', 'created_at']

    def get_user(self, obj):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            return obj.user.username
        return None  # or return "Anonymous"

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def validate(self, data):
        request = self.context.get('request')
        user = request.user
        product = data.get('product')

        # Only apply this check during creation or update (but ignore current instance)
        if request.method in ['POST', 'PUT', 'PATCH']:
            existing = Review.objects.filter(user=user, product=product)
            if self.instance:
                existing = existing.exclude(pk=self.instance.pk)

            if existing.exists():
                raise serializers.ValidationError("You have already reviewed this product.")

        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.feedback = validated_data.get('feedback', instance.feedback)
        instance.save()
        return instance