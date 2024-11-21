# sneakers
e-commerce backend prjct





## Endpoints: 

#### Get product by ID:
    products/{product_uuid}

#### returns JSON like:
    {"id": "854e7541-58c5-4e5f-8ca6-11dad60e8f94",
    "name": "Sneaker",
    "description": "The best of the best",
    "slug": "best_sneaker",
    "image": "../app/images/img.jpg",
    "quantity": 1,
    "price": 12,
    "gender": "M",
    "created_at": "2024-11-20T17:54:18Z",
    "product_size": {
    "id": "f565d44d-418f-400f-a3f9-c69f7ba74f01",
    "size": 45
    },
    "product_brand": {
    "id": "a104ef42-baef-4efc-96a6-8729f1a6cc7e",
    "name": "The best Brand"
    }
    }

#### Get all active products (with flag is_active=True):
    products/{product_uuid}

#### returns list of JSON like:
    [
    {"id": "854e7541-58c5-4e5f-8ca6-11dad60e8f94",
    "name": "Sneaker",
    "slug": "best_sneaker",
    "image": "../app/images/img.jpg",
    "price": 12,
    "product_brand": {
    "id": "a104ef42-baef-4efc-96a6-8729f1a6cc7e",
    "name": "The best Brand"
    }
    },
    {"id": "854e7541-58c5-4e5f-8ca6-11dad60e8f94",
    "name": "Sneaker2",
    "slug": "best_sneaker2",
    "image": "../app/images/img.jpg",
    "price": 12,
    "product_brand": {
    "id": "a104ef42-baef-4efc-96a6-8729f1a6cc7e",
    "name": "The best Brand2"
    }
    }
    ]
  
