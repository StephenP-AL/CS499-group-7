CREATE VIEW viewOrderProduct AS
SELECT truckr_orderitem.purchaseOrderID as purchaseOrderID, truckr_product.productID as productID, truckr_orderitem.quantity as quantity, truckr_product.productName as productName, truckr_product.price as price, truckr_orderitem.status as status
FROM truckr_orderitem JOIN truckr_product
WHERE truckr_orderitem.productID = truckr_product.productID;
