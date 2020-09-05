## Dius Code Challenge - Shopping Cart System

### Getting Started


### Running Tests
```bash
pipenv shell
pipenv run python -m unittest
```

### Solution design

1) Products are registered in a catalog
2) Pricing rules is responsible for knowing which rule to use for which product
3) Scan product by SKU
4) Discount rules are applied at total calculation
