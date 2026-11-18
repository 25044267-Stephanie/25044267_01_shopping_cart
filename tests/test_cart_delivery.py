
import pytest
from src.cart_delivery import qualifies_free_delivery


@pytest.mark.parametrize(
    ("total", "expected"),
    [
        (0, False),
        (4999, False),
        (5001, True),
    ]
)
def test_valid_delivery_values(total, expected):
    # Act
    result = qualifies_free_delivery(total)

    # Assert
    assert result is expected


def test_negative_delivery_total():
    with pytest.raises(ValueError):
        qualifies_free_delivery(-1)


@pytest.mark.parametrize(
    "total",
    [
        "5000",
        5000.5,
        True,
    ]
)
def test_invalid_delivery_data_types(total):
    with pytest.raises(TypeError):
        qualifies_free_delivery(total)
