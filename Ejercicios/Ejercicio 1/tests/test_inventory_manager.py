# test_inventory_system.py
import pytest
from product import Product
from supplier import Supplier
from purchase_order import PurchaseOrder
from inventory_manager import InventoryManager

# Pruebas para la clase Product

def test_product_creation():
    product = Product(1, "Laptop", "Alta gama", 1500.0, 10)
    assert product.id == 1
    assert product.name == "Laptop"
    assert product.description == "Alta gama"
    assert product.price == 1500.0
    assert product.quantity_in_stock == 10

def test_product_creation_invalid_price():
    with pytest.raises(ValueError, match="El precio debe ser un valor positivo."):
        Product(2, "Smartphone", "Alta gama", -500.0, 5)

def test_product_creation_invalid_quantity():
    with pytest.raises(ValueError, match="La cantidad en stock debe ser positiva."):
        Product(3, "Tablet", "Dispositivo táctil", 300.0, -10)

def test_product_update_price():
    product = Product(4, "Monitor", "Full HD", 200.0, 8)
    product.update_price(250.0)
    assert product.price == 250.0

def test_product_update_price_invalid():
    product = Product(5, "Mouse", "Inalámbrico", 20.0, 50)
    with pytest.raises(ValueError, match="El nuevo precio debe ser un valor positivo."):
        product.update_price(-15.0)

def test_product_update_quantity():
    product = Product(6, "Teclado", "Mecánico", 50.0, 20)
    product.update_quantity(25)
    assert product.quantity_in_stock == 25

def test_product_update_quantity_invalid():
    product = Product(7, "Auriculares", "Bluetooth", 30.0, 15)
    with pytest.raises(ValueError, match="La nueva cantidad debe ser positiva."):
        product.update_quantity(-1)

def test_product_summary():
    product = Product(8, "Cámara", "4K", 500.0, 10)
    summary = product.summary()
    assert summary == {
        "id": 8,
        "name": "Cámara",
        "description": "4K",
        "price": 500.0,
        "quantity_in_stock": 10
    }

# Pruebas para la clase Supplier

def test_supplier_creation():
    supplier = Supplier(1, "Tech Corp", "tech@corp.com")
    assert supplier.id == 1
    assert supplier.name == "Tech Corp"
    assert supplier.contact_info == "tech@corp.com"
    assert supplier.products_supplied == set()

def test_supplier_creation_invalid_name():
    with pytest.raises(ValueError, match="El nombre debe ser una cadena no vacía."):
        Supplier(2, "", "contacto@corp.com")

def test_supplier_creation_invalid_contact_info():
    with pytest.raises(ValueError, match="La información de contacto debe ser una cadena no vacía."):
        Supplier(3, "Proveedor", "")

def test_supplier_add_product():
    supplier = Supplier(4, "Tech Corp", "tech@corp.com")
    supplier.add_product(10)
    assert 10 in supplier.products_supplied

def test_supplier_remove_product():
    supplier = Supplier(5, "Gadgets Inc.", "info@gadgets.com")
    supplier.add_product(15)
    supplier.remove_product(15)
    assert 15 not in supplier.products_supplied

def test_supplier_summary():
    supplier = Supplier(6, "Gadgets Inc.", "info@gadgets.com")
    supplier.add_product(20)
    summary = supplier.summary()
    assert summary == {
        "id": 6,
        "name": "Gadgets Inc.",
        "contact_info": "info@gadgets.com",
        "products_supplied": [20]
    }

# Pruebas para la clase PurchaseOrder

def test_purchase_order_creation():
    supplier = Supplier(7, "Tech Supplier", "supplier@tech.com")
    order = PurchaseOrder(1, supplier)
    assert order.order_id == 1
    assert order.supplier == supplier
    assert order.order_items == []
    assert order.status == "pendiente"

def test_purchase_order_create_order():
    supplier = Supplier(8, "Gadget Supplier", "info@gadget.com")
    order = PurchaseOrder(2, supplier)
    order.create_order([{"product_id": 1, "quantity": 5}])
    assert len(order.order_items) == 1
    assert order.order_items[0]["product_id"] == 1
    assert order.order_items[0]["quantity"] == 5

def test_purchase_order_create_order_invalid_quantity():
    supplier = Supplier(9, "Invalid Supplier", "invalid@sup.com")
    order = PurchaseOrder(3, supplier)
    with pytest.raises(ValueError, match="La cantidad de los artículos debe ser positiva."):
        order.create_order([{"product_id": 2, "quantity": -5}])

def test_purchase_order_update_status():
    supplier = Supplier(10, "Order Supplier", "order@supplier.com")
    order = PurchaseOrder(4, supplier)
    order.update_status("completada")
    assert order.status == "completada"

def test_purchase_order_update_status_invalid():
    supplier = Supplier(11, "Invalid Status Supplier", "invalid@status.com")
    order = PurchaseOrder(5, supplier)
    with pytest.raises(ValueError, match="Estado inválido."):
        order.update_status("inexistente")

def test_purchase_order_summary():
    supplier = Supplier(12, "Order Summary Supplier", "summary@supplier.com")
    order = PurchaseOrder(6, supplier)
    order.create_order([{"product_id": 3, "quantity": 10}])
    summary = order.summary()
    assert summary == {
        "order_id": 6,
        "supplier": supplier.summary(),
        "order_items": [{"product_id": 3, "quantity": 10}],
        "status": "pendiente"
    }

# Pruebas para la clase InventoryManager

def test_inventory_manager_add_product():
    manager = InventoryManager()
    product = Product(1, "Laptop", "Alta gama", 1500.0, 10)
    manager.manage_products("add", product)
    assert product.id in manager.products

def test_inventory_manager_update_product():
    manager = InventoryManager()
    product = Product(2, "Tablet", "Pantalla táctil", 300.0, 20)
    manager.manage_products("add", product)
    product.update_price(350.0)
    manager.manage_products("update", product)
    assert manager.products[2].price == 350.0

def test_inventory_manager_delete_product():
    manager = InventoryManager()
    product = Product(3, "Smartphone", "5G", 800.0, 5)
    manager.manage_products("add", product)
    manager.manage_products("delete", product)
    assert 3 not in manager.products

def test_inventory_manager_add_supplier():
    manager = InventoryManager()
    supplier = Supplier(1, "Tech Supplier", "supplier@tech.com")
    manager.manage_suppliers("add", supplier)
    assert supplier.id in manager.suppliers

def test_inventory_manager_add_purchase_order():
    manager = InventoryManager()
    supplier = Supplier(2, "Order Supplier", "order@supplier.com")
    order = PurchaseOrder(1, supplier)
    manager.manage_purchase_orders("add", order)
    assert order.order_id in manager.purchase_orders

def test_inventory_manager_generate_reports():
    manager = InventoryManager()
    product = Product(1, "Laptop", "Alta gama", 1500.0, 10)
    supplier = Supplier(2, "Tech Supplier", "supplier@tech.com")
    order = PurchaseOrder(3, supplier)
    order.create_order([{"product_id": 1, "quantity": 2}])
    manager.manage_products("add", product)
    manager.manage_suppliers("add", supplier)
    manager.manage_purchase_orders("add", order)
    reports = manager.generate_reports()
    assert len(reports["products"]) == 1
    assert len(reports["suppliers"]) == 1
    assert len(reports["purchase_orders"]) == 1
