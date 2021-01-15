from django.test import TestCase

# Create your tests here.

# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.views import status
# from .models import Produtos
# from .serializers import ProdutosSerializer

# tests for views

# class GetAllProdutosTest(BaseViewTest):

#     def test_get_all_produtos(self):
#         """
#         This test ensures that all produtos added in the setUp method
#         exist when we make a GET request to the produtos/ endpoint
#         """
#         # hit the API endpoint
#         response = self.client.get(
#             reverse("produtos-all", kwargs={"version": "v1"})
#         )
#         # fetch the data from db
#         expected = Produtos.objects.all()
#         serialized = ProdutosSerializer(expected, many=True)
#         self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)