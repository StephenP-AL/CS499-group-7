-- Insert data into shipmentOut table
INSERT INTO shipmentOut (shipID, clientID, vehID, departure, estArrival, arrived, payment, driver, manifest, purchaseOrder)
VALUES
('SH0001', 1, 3, '2023-02-23 10:00:00', '2023-02-24 12:00:00', 1, 1, 5, 1, 1),
('SH0002', 2, 4, '2023-02-22 12:00:00', '2023-02-23 15:00:00', 1, 1, 9, 2, 2),
('SH0003', 3, 1, '2023-02-21 14:00:00', '2023-02-22 16:00:00', 1, 1, 13, 3, 3),
('SH0004', 4, 5, '2023-02-20 16:00:00', '2023-02-21 18:00:00', 1, 1, 1, 4, 4),
('SH0005', 5, 3, '2023-02-19 18:00:00', '2023-02-20 20:00:00', 1, 1, 5, 5, 5),
('SH0006', 6, 2, '2023-02-18 20:00:00', '2023-02-19 22:00:00', 0, 0, 9, 6, 6),
('SH0007', 7, 1, '2023-02-17 22:00:00', '2023-02-18 00:00:00', 0, 0, 13, 7, 7),
('SH0008', 8, 5, '2023-02-16 00:00:00', '2023-02-17 02:00:00', 0, 0, 1, 8, 8),
('SH0009', 9, 4, '2023-02-15 02:00:00', '2023-02-16 04:00:00', 0, 0, 5, 9, 9),
('SH0010', 10, 2, '2023-02-14 04:00:00', '2023-02-15 06:00:00', 0, 0, 9, 10, 10);

-- Insert data into purchaseOrder table
INSERT INTO purchaseOrder (purchaseOrderID, costShippingHandling)
VALUES
(1, 500),
(2, 500),
(3, 500),
(4, 500),
(5, 500),
(6, 500),
(7, 500),
(8, 500),
(9, 500),
(10, 500);

