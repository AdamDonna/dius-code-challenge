## Dius Code Challenge - Shopping Cart System

This is my solution for the challenge provided [here](https://github.com/DiUS/coding-tests/blob/master/dius_shopping.md)
I'll be discussing the solution design, why it's good and where it has flaws.
This document will also provide some insight into my thinking around my approach and any assumptions i made from the document

### Assumptions
1) When we have a 3 for 2 deal on Apple TVs. It is applied for ever 3 tvs purchased
2) When we bundle in a free VGA adapter free of charge with every MacBook Pro sold, this can either be adding one to the cart, or one already in the cart.



### Solution design

#### Notes
This solution isn't usually what I would head towards but was heavily influenced by two factors
1) The required interface of
```python
co = Checkout(pricingRules)
co.scan(item1)
co.scan(item2)
co.total()
```
2) Not having an ORM or dynamic way make the relationships configurable
3) Pricing Rules have relations other products in this domain, rather than a percentage discount

#### Written approach
1) Products are registered in a catalog using a base class subscription patter.
This would effectively replicate a DB/ORM which is what would realistically be used for.
2) Pricing rules is responsible for knowing which rule to use for which product
The pricing rules class maps the pricing rules to products.
This is meant to replication the mapping between discount type and product which would be used in a DB based aproach
3) Scan product by SKU as required in the interface
4) Discount rules are applied at total calculation, so new items can be determined to be added
5) Intermediate checkout item is use for cart calculation.
This gives us some advantages around introducing new discounts in the future
It also has some advantages when we need to get a receipt for the order. The user can determine what they paid for and what was free.



### Running Tests
Tests can be run with the standard python unittest framework

```bash
pipenv shell
pipenv run python -m unittest
```


### Notes
- Took about 3.5 hours because my original design wasn't meeting the interface requirements
- Also spent some time making sure my docs and tests were up to scratch
