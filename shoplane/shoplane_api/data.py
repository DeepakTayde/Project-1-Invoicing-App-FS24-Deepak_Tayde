productData = [

    {
        "product_id": 1,
        
        "name": "Product 1",

        "slug": "product-1",

        "image": "products/product1.jpg",

        "brand": "Brand A",

        "shipping": "Free Shipping",

        "description": "This is a description for Product 1.",

        "price": "49.99",

        "category_id": 1,

        "featured": True,

        "active": True,

        "created": "2023-04-22T10:00:00Z",

        "modified": "2023-04-22T10:00:00Z"

    },

    {
        "product_id": 2,
        "name": "Product 2",

        "slug": "product-2",

        "image": "products/product2.jpg",

        "brand": "Brand B",

        "shipping": "Standard Shipping",

        "description": "This is a description for Product 2.",

        "price": "29.99",

        "category_id": 2,

        "featured": False,

        "active": True,

        "created": "2023-04-21T15:00:00Z",

        "modified": "2023-04-21T15:00:00Z"

    },

    {
        "product_id": 3,
        "name": "Product 3",

        "slug": "product-3",

        "image": "products/product3.jpg",

        "brand": "Brand C",

        "shipping": "Free Shipping",

        "description": "This is a description for Product 3.",

        "price": "19.99",

        "category_id": 1,

        "featured": True,

        "active": False,

        "created": "2023-04-20T18:00:00Z",

        "modified": "2023-04-20T18:00:00Z"

    }


]

carts = [
    {
        "cart_id": 1,
        "product_id": 1,
        "quantity": 2,
        "discount": 0.0,
    }
]

userData = [{
    "user_id": 1,
    "first_name": "Deepak",
    "last_name": "Tayde",
    "username": "user1",
    "email": "user1@gmail.com",
    "password": "user1",
},]

invoiceData = [
    {
        "invoice_id": 1,
        "client_name":"Deepak Tayde",
        "date": "2024-04-20",
        "items":[
            {
                "item_id": 1,
                "desc" : "testing",
                "quantity": 2,
                "rate": 10.0,
            },
                        {
                "item_id": 2,
                "desc" : "product",
                "quantity": 2,
                "rate": 10.0,
            }

        ],

    }
]