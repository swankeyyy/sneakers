# sneakers
e-commerce backend prjct





## Endpoints: 

#### Get product by ID:
    products/{product_uuid}


#### Get all active products (with flag is_active=True):
    products/all/



#### Get all brands with products (with flag is_active=True):
    products/brands/all/

#### Get all brand by uuid:
    products/brands/{brand_uuid}

#### Get products by size:
    products/sizes/{size}

#### Get orders of current authorized user:
    orders/

#### Add product to order of current user"
    orders/add_product/{product_uuid}
  

### Usage:
 - clone repository
 - set in src/settings your database url
 - run "alembic upgrade heads"

### Docs:
    http://127.0.0.1:8000/docs/

### Admin:
    http://127.0.0.1:8000/admin


any questions: swankyyy1@gmail.com


