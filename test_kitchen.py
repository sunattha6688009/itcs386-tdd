# Test list
# [ ] 200 g x 3 = 600 g
# [ ] multiplying a quantity does not modify the original
# [ ] two quantities with the same amount and unit are equal
# [ ] 1 oz is not the same as 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz, reduced to grams, using a conversion rate
# [ ] (200 g + 1 oz) x 2
# [ ] __hash__ (since __eq__ makes Quantity unhashable)


# A1
from kitchen import Quantity, grams, ounces, Converter

# def test_multiplication():
#     flour = Quantity(200)
#     assert flour.times(3).amount == 600

# # A3
# def test_multiplication_returns_a_new_quantity():
#     flour = Quantity(200)
#     assert flour.times(3).amount == 600
#     assert flour.times(2).amount == 400

# # A2
# # def test_multiplication_by_two():
# #     flour = Quantity(200)
# #     flour.times(2)
# #     assert flour.amount == 400

# # A4
# def test_equality():
#     assert Quantity(200) == Quantity(200)
#     assert Quantity(200) != Quantity(300)

# A5
def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")

def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)

def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)

def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)

def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)

def test_reduce_same_unit_needs_no_rate():
    converter = Converter()
    assert converter.reduce(grams(500), "g") == grams(500)

def test_mixed_addition():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    total = grams(200).plus(ounces(1))
    assert converter.reduce(total, "g") == grams(228)

def test_ounces_to_grams_direction():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    assert converter.reduce(ounces(2), "g") == grams(56)