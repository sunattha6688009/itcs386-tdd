import pytest
from shipping import shipping_fee

# Return the shipping fee in baht for a parcel of weight_kg kilograms.
# Rule 1. The weight must be more than 0 kg. Otherwise raise ValueError.
# Rule 2. A parcel of up to 1 kg costs 40 baht.
# Rule 3. A parcel of more than 1 kg and up to 5 kg costs 60 baht.
# Rule 4. A parcel of more than 5 kg costs 60 baht plus 10 baht for every started kilogram above 5 kg. A 5.2 kg parcel costs 70 baht.

@pytest.mark.parametrize("weight", [0, -1])
def test_invalid_weight_is_rejected(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)

@pytest.mark.parametrize("weight, fee", [
    (0.5, 40),
    (1, 40),
    (5, 60),
    (4.9, 60),
    (1.1, 60),
    (5.1, 70),
    (6, 70),
    (6.1, 80)
])
def test_shipping_fee(weight, fee):
    assert shipping_fee(weight) == fee