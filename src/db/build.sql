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


