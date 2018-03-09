CREATE DATABASE IF NOT EXISTS Dunes;

USE Dunes;

CREATE TABLE IF NOT EXISTS Customer
(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(200),
    Password VARCHAR(200),
    Name VARCHAR(200),
    LastName VARCHAR(200),
    Birthday DATE,
    ProfilePicPath TEXT
) ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS Product
(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(200),
    Description TEXT,
    Price DECIMAL(12,2),
    Stock INT,
    ImagePath TEXT
) ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS Orders
(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate TIMESTAMP,
    CurrentOrder BIT(1),
    CustomerID INT,
    CONSTRAINT FK_Orders_Customer FOREIGN KEY(CustomerID) REFERENCES Customer(ID) 
) ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS `Orders Details`
(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(12,2),
    CONSTRAINT FK_OrderDetails_Orders FOREIGN KEY(OrderID) REFERENCES Orders(ID),
    CONSTRAINT FK_OrderDetails_Product FOREIGN KEY(ProductID) REFERENCES Product(ID)
) ENGINE = INNODB;

-- CUSTOMER

CREATE PROCEDURE usp_Customer_Create(IN unam VARCHAR(200), IN pass VARCHAR(200), IN nam VARCHAR(200), IN lastNam VARCHAR(200), IN bday DATE, IN mail VARCHAR(300), IN pic TEXT)
    INSERT INTO Customer(Username, Password, Name, LastName, Birthday, EMail, ProfilePicPath)
           VALUES(unam, pass, nam, lastNam, bday, mail, pic);

CREATE PROCEDURE usp_Customer_Update(IN id INT, IN unam VARCHAR(200), IN pass VARCHAR(200), IN nam VARCHAR(200), IN lastNam VARCHAR(200), IN bday DATE, IN mail VARCHAR(300), IN pic TEXT)
    UPDATE Customer SET Username = unam, Password = pass, Name = nam, LastName = lastNam, Birthday = bday, EMail = mail, ProfilePicPath = pic
    WHERE ID = id;

CREATE PROCEDURE usp_Customer_Find(IN cusID INT)
    SELECT ID, Username, Password, Name, LastName, Birthday, EMail, ProfilePicPath
    FROM Customer WHERE ID = cusID;

CREATE PROCEDURE usp_Customer_FindAll()
    SELECT ID, Username, Password, Name, LastName, Birthday, EMail, ProfilePicPath 
    FROM Customer;

CREATE PROCEDURE usp_Customer_Login(IN user VARCHAR(200), IN pass VARCHAR(200))
    SELECT ID, Username, Password, Name, LastName, Birthday, EMail, ProfilePicPath
    FROM Customer WHERE Username = user AND Password = pass;

-- PRODUCT

CREATE PROCEDURE usp_Product_FindAll()
    SELECT ID, Name, Description, Price, Stock, ImagePath 
    FROM Product;

CREATE PROCEDURE usp_Product_Find(IN proID INT)
    SELECT ID, Name, Description, Price, Stock, ImagePath
    FROM Product WHERE ID = proID;
    
-- ORDERS

CREATE PROCEDURE usp_Orders_Create(IN orDate TIMESTAMP, IN currOrder BIT(1), IN cusID INT)
    INSERT INTO Orders(OrderDate, CurrentOrder, CustomerID)
        VALUES (orDate, currOrder, cusID);

CREATE PROCEDURE usp_Orders_Update(IN orID INT, IN currOrder BIT(1))
    UPDATE Orders SET CurrentOrder = currOrder 
    WHERE ID = orID;

DELIMITER //
CREATE PROCEDURE usp_Orders_Delete(IN orID INT)
    BEGIN
        DELETE FROM `Order Details` WHERE OrderID = orID;
        DELETE FROM Orders WHERE ID = orID;
    END//
DELIMITER ;

CREATE PROCEDURE usp_Orders_Find(IN orID INT)
    SELECT ID, OrderDate, CONVERT(CurrentOrder, UNSIGNED) AS CurrentOrder, CustomerID
    FROM Orders WHERE ID = orID;

CREATE PROCEDURE usp_Orders_FindAll(IN cusID INT)
    SELECT ID, OrderDate, CAST(CurrentOrder AS UNSIGNED) CurrentOrder, CustomerID
    FROM Orders WHERE CustomerID = cusID;

CREATE PROCEDURE usp_Orders_Find_Current(IN cusID INT)
    SELECT ID, OrderDate, CONVERT(CurrentOrder, UNSIGNED) CurrentOrder, CustomerID
    FROM Orders WHERE CustomerID = cusID AND CONVERT(CurrentOrder, UNSIGNED) = 1;
    
-- ORDER DETAILS

CREATE PROCEDURE usp_OrderDetails_Create(IN orID INT, IN proID INT, IN quan INT, IN uPrice DECIMAL(12,2))
    INSERT INTO `Order Details`(OrderID, ProductID, Quantity, UnitPrice)
        VALUES (orID, proID, quan, uPrice);

CREATE PROCEDURE usp_OrderDetails_Update(IN odID INT, IN quan INT)
    UPDATE `Order Details` SET Quantity = quan
    WHERE ID = odID;

CREATE PROCEDURE usp_OrderDetails_Delete(IN odID INT)
    DELETE FROM `Order Details` 
    WHERE ID = odID;

CREATE PROCEDURE usp_OrderDetails_Find(IN odID INT)
    SELECT ID, OrderID, ProductID, Quantity, UnitPrice
    FROM `Order Details` WHERE ID = odID;

CREATE PROCEDURE usp_OrderDetails_FindAll(IN orID INT)
    SELECT ID, OrderID, ProductID, Quantity, UnitPrice
    FROM `Order Details` WHERE OrderID = orID;

-- CUSTOM

--CREATE PROCEDURE usp_Orders_And_Details_Find()

--CREATE PROCEDURE usp_Orders_And_Details_FindAll()

