import pytest
from ecommerce_platform import EcommercePlatform
from product import Product
from user import User

def test_add_product():
    platform = EcommercePlatform()
    product = Product(1, "Laptop", "Portátil de alta gama", 1500.0, 10)
    platform.manage_products("add", product)
    assert 1 in platform.products

def test_register_user():
    platform = EcommercePlatform()
    user = User(1, "user1", "user1@example.com", "password")
    platform.manage_users("add", user)
    assert 1 in platform.users

def test_create_order():
    platform = EcommercePlatform()
    product = Product(1, "Phone", "Smartphone", 500.0, 10)
    platform.manage_products("add", product)
    user = User(1, "user1", "user1@example.com", "password")
    platform.manage_users("add", user)
    user.add_to_cart(1, 2)
    order = platform.create_order(1)
    assert order.total_amount == 1000.0
    assert order.status == "pending"

def test_checkout_insufficient_stock():
    platform = EcommercePlatform()
    product = Product(1, "Tablet", "10-inch display", 300.0, 1)
    platform.manage_products("add", product)
    user = User(1, "user2", "user2@example.com", "password")
    platform.manage_users("add", user)
    user.add_to_cart(1, 2)
    with pytest.raises(ValueError, match="no disponible en la cantidad solicitada"):
        platform.create_order(1)

def test_order_payment():
    order = Order(1, User(1, "user3", "user3@example.com", "password"), {}, 300.0)
    order.process_payment({"status": "success"})
    assert order.status == "completed"
