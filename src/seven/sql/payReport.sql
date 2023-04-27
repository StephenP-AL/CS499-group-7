CREATE VIEW payReport AS
SELECT truckr_account.employeeID AS ID,
accountType,
(fName || ' ' || mName || ' ' || lName) AS fullName,
pay,
strftime('%Y', startDate) AS yr,
strftime('%m', startDate) AS mo 
FROM truckr_employee JOIN truckr_account
ON truckr_employee.employeeID = truckr_account.employeeID;
