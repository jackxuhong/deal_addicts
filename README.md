# Deal Addicts
Deal addicts are people who are addicted to deals.  The addiction affects a person's brain and behaviour and leads to an inability to buy anything without a price drop.

When desired price drops are caught, the patients proceed with the purchase and usually enjoy a surge of dopamine for a short while, although often followed by regrets after receiving bank / credit card statements.

When desired price drops are missed, the patients can suffer emotionally and psychologically for an extended period of time, or until the same or a better price can be acquired. 

This program is designed to help deal addicts better monitor price drops and reduce the likelihood of repeated sufferings.


# High Level Design

## Screens
### List of Products
- A list of products to be watched
- A button at the top to Add Product
- A button by each product to Edit Product

### Add Product
- specify product source, product #, target price, target qty, etc.
- specify watch frequency and notifiction method

### Edit Product
- edit target price, target qty, etc.
- edit watch frequency and notifiction method

### View Product History
- shows price history and stock history for a period

## Classes

### Product - an item that the a deal addict desires
- product_id (system generated int)
- product_name
- source (Amazon, HomeDepot, Ubiquiti, etc.)
- source_key (product no. or URL at the source)
- target_px (the desired price)
- target_qty (the desired stock quantity)
- in_stock (y/n)
- stock_qty (optional, may not be available)

### ProductWatcher - an abstract adapter that observes a product at its source
- get_url(product_id) - returns the URL to the product for a given product ID
- observe(product_ids) - observes a list of products and returns their current status

### ProductStatus - snapshot of product status at a certain time
- product_id
- in_stock
- stock_qty
- last_px
- last_updated


### ConcreteProductWatcher - a concrete implementation of ProductWatcher for a source
- get_url(product_id)
- observe(product_id)
