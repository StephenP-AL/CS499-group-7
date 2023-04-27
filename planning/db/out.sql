.mode insert
SELECT shipmentOut.shipID, shipmentOut.vehID, shipmentOut.departure, shipmentOut.estArrival, shipmentOut.arrived, shipmentOut.payment, shipmentOut.driver, shipmentOut.manifest, shipmentOut.purchaseOrder, client.clientName, client.street, client.city, client.state, client.zip AS zipcode
FROM shipmentOut JOIN client 
ON shipmentOut.clientID = client.clientID

;
