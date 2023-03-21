from rest_framework.serializers import ModelSerializer

from backend.models import User, Category, Slide, Product, ProductOption, ProductImage, PageItem


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'phone', 'fullname', ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'position', 'image']


class SlideSerializer(ModelSerializer):
    class Meta:
        model = Slide
        fields = ['position', 'image']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']


class ProductOptionSerializer(ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['__all__']


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['__all__']


class PageItemSerializer(ModelSerializer):
    class Meta:
        model = PageItem
        fields = ['__all__']