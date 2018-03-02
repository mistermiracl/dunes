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

CREATE PROCEDURE usp_Orders_Create()
    ID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate TIMESTAMP,
    CurrentOrder BIT(1),
    CustomerID INT,
CREATE PROCEDURE usp_Orders_Update()

CREATE PROCEDURE usp_Orders_Delete()

CREATE PROCEDURE usp_Orders_Find()

CREATE PROCEDURE usp_Orders_FindAll()

-- ORDER DETAILS

CREATE PROCEDURE usp_OrderDetails_Create()

CREATE PROCEDURE usp_OrderDetails_Update()

CREATE PROCEDURE usp_OrderDetails_Delete()

CREATE PROCEDURE usp_OrderDetails_Find()

CREATE PROCEDURE usp_OrderDetails_FindAll()

