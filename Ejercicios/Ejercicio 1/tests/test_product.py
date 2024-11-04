# test_product.py
import pytest
from product import Product

def test_create_product_success():
    product = Product(1, "Laptop", "Portátil de alta gama", 1500.0, 10)
    assert product.id == 1
    assert product.name == "Laptop"
    assert product.description == "Portátil de alta gama"
    assert product.price == 1500.0
    assert product.quantity_in_stock == 10

def test_create_product_invalid_price():
    with pytest.raises(ValueError, match="El precio debe ser un valor positivo."):
        Product(2, "Smartphone", "Teléfono inteligente", -500.0, 5)

def test_create_product_invalid_quantity():
    with pytest.raises(ValueError, match="La cantidad en stock debe ser un entero positivo."):
        Product(3, "Tablet", "Dispositivo de pantalla táctil", 300.0, -10)

def test_create_product_empty_name():
    with pytest.raises(ValueError, match="El nombre debe ser una cadena no vacía."):
        Product(4, "", "Sin nombre", 100.0, 2)

def test_create_product_empty_description():
    with pytest.raises(ValueError, match="La descripción debe ser una cadena no vacía."):
        Product(5, "Teclado", "", 25.0, 15)

def test_update_price_success():
    product = Product(6, "Monitor", "Monitor Full HD", 200.0, 8)
    product.update_price(220.0)
    assert product.price == 220.0

def test_update_price_invalid():
    product = Product(7, "Mouse", "Ratón inalámbrico", 20.0, 50)
    with pytest.raises(ValueError, match="El nuevo precio debe ser un valor positivo."):
        product.update_price(-15.0)

def test_update_quantity_success():
    product = Product(8, "Impresora", "Impresora multifunción", 100.0, 4)
    product.update_quantity(6)
    assert product.quantity_in_stock == 6

def test_update_quantity_invalid():
    product = Product(9, "Escáner", "Escáner de documentos", 75.0, 3)
    with pytest.raises(ValueError, match="La nueva cantidad debe ser un entero positivo."):
        product.update_quantity(-1)

def test_product_summary():
    product = Product(10, "Auriculares", "Auriculares de alta fidelidad", 50.0, 20)
    summary = product.summary()
    assert summary == {
        "id": 10,
        "name": "Auriculares",
        "description": "Auriculares de alta fidelidad",
        "price": 50.0,
        "quantity_in_stock": 20
    }
