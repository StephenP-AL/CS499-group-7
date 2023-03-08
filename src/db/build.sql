DROP TABLE employee;
CREATE TABLE employee
(	employeeID int,
	fName varchar(20),
	mName varchar(20),
	lName varchar(20),
	street varchar(30),
	city varchar(30),
	state varchar(2),
	zip varchar(6),
	homePhone varchar(10),
	cellPhone varchar(10),
	pay numeric,
	startDate date,
	username varchar(20),
	PRIMARY KEY (employeeID)
);

DROP TABLE account;
CREATE TABLE account
(	employeeID int,
	accountType varchar(5),
	PRIMARY KEY (employeeID)
);

DROP TABLE client;
CREATE TABLE client
(	clientID int,
	clientName varchar(20),
	street varchar(30),
	city varchar(30),
	state varchar(2),
	zip varchar(6),
	PRIMARY KEY (clientID)
);

DROP TABLE shipmentOut;
CREATE TABLE shipmentOut
(	shipID varchar(10),
	clientID int,
	vehID int,
	departure datetime,
	estArrival datetime,
	arrived boolean,
	payment boolean,
	driver int,
	manifest int,
	purchaseOrder int,
	PRIMARY KEY (shipID),
	FOREIGN KEY(clientID) REFERENCES client(clientID),
	FOREIGN KEY(driver) REFERENCES employee(employeeID),
	FOREIGN KEY(manifest) REFERENCES manifest(manifestID),
	FOREIGN KEY(purchaseOrder) REFERENCES purchaseOrder(purchaseOrderID),
	FOREIGN KEY(vehID) REFERENCES vehicle(vehID)
);

DROP TABLE manifest;
CREATE TABLE manifest
(	manifestID int,
	costShippingHandling numeric,
	PRIMARY KEY (manifestID)
);

DROP TABLE purchaseOrder;
CREATE TABLE purchaseOrder 
(	purchaseOrderID int, 
	costShippingHandling numeric,
	PRIMARY KEY (purchaseOrderID)
);

DROP TABLE vehicle;
CREATE TABLE vehicle
(	vehID int,
	make varchar(20),
	model varchar(20),
	year int,
	vehType varchar(20),
	loadCapacity int,
	height int,
	partsList int,
	PRIMARY KEY (vehID)
	FOREIGN KEY(partsList) REFERENCES partsList(listID)
);

DROP TABLE shipmentIn;
CREATE TABLE shipmentIn
(	shipID varchar(10),
	clientID int,
	vehID int,
	departure datetime,
	estArrival datetime,
	arrived boolean,
	payment boolean,
	driver int,
	purchaseOrder int,
	PRIMARY KEY (shipID),
	FOREIGN KEY(clientID) REFERENCES client(clientID),
	FOREIGN KEY(driver) REFERENCES employee(employeeID),
	FOREIGN KEY(purchaseOrder) REFERENCES purchaseOrder(purchaseOrderID),
	FOREIGN KEY(vehID) REFERENCES vehicle(vehID)
);

DROP TABLE part;
CREATE TABLE part
(	partID int,
	onHand int,
	partName varchar(30),
	PRIMARY KEY(partID)
);

DROP TABLE partsList;
CREATE TABLE partsList
(	listID int,
	partID int,
	source varchar(30),
	cost numeric,
	PRIMARY KEY(listID,partID),
	FOREIGN KEY(partID) REFERENCES part(partID)
);

DROP TABLE maintenance;
CREATE TABLE maintenance
(	maintID int,
	vehID int,
	description varchar(30),
	completed datetime,
	partsList int,
	PRIMARY KEY(maintID),
	FOREIGN KEY(vehID) REFERENCES vehicle(vehID),
	FOREIGN KEY(partsList) REFERENCES partsList(listID)
);

DROP TABLE product;
CREATE TABLE product
(	productID int,
	price numeric,
	productName varchar(30),
	PRIMARY KEY(productID)
);

DROP TABLE manifestItem;
CREATE TABLE manifestItem
(	manifestID int,
	productID int,
	quantity int,
	PRIMARY KEY (manifestID, productID),
	FOREIGN KEY(manifestID) REFERENCES manifest(manifestID),
	FOREIGN KEY(productID) REFERENCES product(productID)
);

DROP TABLE orderItem;
CREATE TABLE orderItem
(	purchaseOrderID int,
	productID int,
	quantity int,
	status varchar(11),
	PRIMARY KEY (purchaseOrderID,productID),
	FOREIGN KEY (purchaseOrderID) REFERENCES purchaseOrder(purchaseOrderID),
	FOREIGN KEY (productID) REFERENCES product(productID)
);
