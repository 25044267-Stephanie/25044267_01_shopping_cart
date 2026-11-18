
import pytest
from src.cart_total import calculate_total


@pytest.mark.parametrize(
    ("unit_price", "quantity", "expected"),
    [
        (1000, 2, 2000),
        (0, 3, 0),
        (1000, 1, 1000),
    ]
)
def test_valid_cart_total(unit_price, quantity, expected):
    # Act
    result = calculate_total(unit_price, quantity)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    ("unit_price", "quantity"),
    [
        (-100, 2),
        (1000, -1),
    ]
)
def test_negative_values(unit_price, quantity):
    with pytest.raises(ValueError):
        calculate_total(unit_price, quantity)


@pytest.mark.parametrize(
    ("unit_price", "quantity"),
    [
        ("1000", 2),
        (1000, 2.5),
        (True, 2),
    ]
)
def test_invalid_data_types(unit_price, quantity):
    with pytest.raises(TypeError):
        calculate_total(unit_price, quantity)
