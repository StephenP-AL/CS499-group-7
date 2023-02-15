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
	purchaseorder int,
	PRIMAY KEY (shipID),
	FOREIGN KEY(clientID) REFERENCES client(clientID),
	FOREIGN KEY(driver) REFERENCES employee(employeeID)
	--need FK for manifest, purchase order, and vehicle
);
