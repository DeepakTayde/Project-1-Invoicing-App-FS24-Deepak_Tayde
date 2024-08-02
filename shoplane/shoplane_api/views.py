from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data import *
from .serializer import *
import json
import jwt
 
# Create your views here.
class ProductView(APIView):
    def get(self, request):
        serializer = ProductSerializer(productData, many = True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        bodyData = request.data
        bodyData["product_id"] = len(productData)+1
        serializer = ProductSerializer(data=bodyData)
        if serializer.is_valid():
            productData.append(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        for product in productData:
            if product["product_id"] == id:
                productData.remove(product)
                return Response({"message": "Product has been deleted"},status=status.HTTP_200_OK)
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        for i, product in enumerate(productData):
            if product["product_id"] == id:
                bodyData=request.data
                bodyData["product_id"]=id
                serializer = ProductSerializer(data=bodyData)
                if serializer.is_valid():
                    productData[i] = serializer.data
                    return Response({"message":"Updated"}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Product not found"}, status=status.HTTP_404_NOT_FOUND)


class SpecificProductView(APIView):
    def get(self, request, name):
        for val in productData:
            if val["slug"] == name:
                serializer = ProductSerializer(val).data
                return Response(serializer, status=status.HTTP_200_OK)
        return Response({"message": "Product Not found"}, status=status.HTTP_404_NOT_FOUND)

class CartView(APIView):
    def post(self, request):
        bodyData = request.data
        bodyData["cart_id"] = len(carts)+1
        serializer = CartSerializer(data=bodyData)
        if serializer.is_valid():
            carts.append(serializer.data)
            return Response({"message" : "tem has been added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        serializer = CartSerializer(carts, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        for product in carts:
            if product["cart_id"] == id:
                carts.remove(product)
                return Response({"message": "Product has been removed"},status=status.HTTP_200_OK)
        return Response({"message":"product not found"}, status=status.HTTP_404_NOT_FOUND)



class SearchProductView(APIView):
    def get(self, request):
        query = request.GET.get('query', None)
        data = []
        for product in productData:
            if query.lower() in product['name'].lower() or query.lower() in product['slug'].lower() or query.lower() in product['description'].lower():
                data.append(product)
        serializer = ProductSerializer(data, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(userData, many = True).data
        return Response(serializer, status=status.HTTP_200_OK)

class SignupView(APIView):
    def post(self, request):
        bodyData = json.loads(request.body)
        for val in userData:
            if val["email"] == bodyData["email"]:
                return Response({"message": "User already exists"}, status=status.HTTP_302_FOUND)
        bodyData["user_id"] = len(userData)+1
        serializer = UserSerializer(data=bodyData)
        if serializer.is_valid():
            userData.append(serializer.data)
            return Response({"message" : "User has been added"}, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        bodyData = request.data
        for user in userData:
            if user["email"] == bodyData["email"] and user["password"] == bodyData["password"]:
                encoded_jwt = jwt.encode({"email": user["email"], "user_id":user["user_id"]}, "secret", algorithm="HS256")
                return Response({"message": "Login Successful", "token": str(encoded_jwt)}, status=status.HTTP_200_OK)
        return Response({"message": "Login Failed"}, status=status.HTTP_401_UNAUTHORIZED) 

class InvoiceView(APIView):
    def get(self, request):
        serializer = InvoiceSerializer(invoiceData, many = True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        bodyData = request.data
        bodyData["invoice_id"] = len(invoiceData)+1
        serializer = InvoiceSerializer(data=bodyData)
        if serializer.is_valid():
            invoiceData.append(serializer.data)
            return Response({"message" : "Invoice has been added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
class InvoiceDetailsView(APIView):
    def get(self, request, invoice_id):
        for invoice in invoiceData:
            if invoice["invoice_id"] == invoice_id:
                serializer = InvoiceSerializer(invoice).data
                return Response(serializer, status=status.HTTP_200_OK)
        return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ItemsView(APIView):
    def post(self, request, invoice_id):
        for invoice in invoiceData:
            if invoice["invoice_id"] == invoice_id:
                bodyData = request.data
                bodyData["item_id"] = len(invoice["items"])+1
                # bodyData["invoice_id"] = invoice_id
                serializer = ItemSerializer(data=bodyData)
                if serializer.is_valid():
                    invoice["items"].append(serializer.data)
                    return Response({"message" : "Item has been added"}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
            
        