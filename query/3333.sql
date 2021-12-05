/*
SQLyog Community
MySQL - 8.0.27-0ubuntu0.20.04.1 : Database - bbgg
*********************************************************************
*/

/*!40101 SET NAMES utf8 */

/*!40101 SET SQL_MODE=''*/

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */

/*Table structure for table Cart */

CREATE TABLE Cart (
  ProductID int unsigned NOT NULL AUTO_INCREMENT,
  UserID int NOT NULL,
  Amount int DEFAULT NULL,
  ProductName char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  ProductPrice int DEFAULT NULL,
  PRIMARY KEY (ProductID,UserID)
) ;

/*Data for the table Cart */

insert  into Cart(ProductID,UserID,Amount,ProductName,ProductPrice) values 
(1,1,1,'I dont',100000);

/*Table structure for table Company */

CREATE TABLE Company (
  CompanyID int unsigned NOT NULL AUTO_INCREMENT,
  CompanyName char(255) DEFAULT NULL,
  CompanyGrade char(255) DEFAULT NULL,
  CompanyDescription char(255) DEFAULT NULL,
  CompanyPhone char(255) DEFAULT NULL,
  CompanyEmail char(255) DEFAULT NULL,
  PRIMARY KEY (CompanyID)
) AUTO_INCREMENT=3 ;

/*Data for the table Company */

insert  into Company(CompanyID,CompanyName,CompanyGrade,CompanyDescription,CompanyPhone,CompanyEmail) values 
(1,'APPLE','A','apple is big tech company',NULL,NULL),
(2,'SAMSUNG','B','samsung is big tech company',NULL,NULL);

/*Table structure for table Coupon */

CREATE TABLE Coupon (
  CouponID int unsigned NOT NULL AUTO_INCREMENT,
  UserID int DEFAULT NULL,
  DiscountAmount int DEFAULT NULL,
  UsedCheck tinyint(1) DEFAULT '0',
  CouponDateUsed datetime DEFAULT NULL,
  CouponDateMade datetime DEFAULT NULL,
  PRIMARY KEY (CouponID)
) AUTO_INCREMENT=4 ;

/*Data for the table Coupon */

insert  into Coupon(CouponID,UserID,DiscountAmount,UsedCheck,CouponDateUsed,CouponDateMade) values 
(1,1,10000,1,NULL,NULL),
(2,1,20000,0,NULL,NULL),
(3,1,30000,NULL,NULL,NULL);

/*Table structure for table Product */

CREATE TABLE Product (
  ProductID int unsigned NOT NULL AUTO_INCREMENT,
  ProductName char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  ProductRegion char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  ProductPrice int DEFAULT NULL,
  ProductDescription char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  ProductCompany char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  ProductStock int DEFAULT NULL,
  ProductDateCreated date DEFAULT NULL,
  ProductDateTour date DEFAULT NULL,
  PRIMARY KEY (ProductID)
) AUTO_INCREMENT=6 ;

/*Data for the table Product */

insert  into Product(ProductID,ProductName,ProductRegion,ProductPrice,ProductDescription,ProductCompany,ProductStock,ProductDateCreated,ProductDateTour) values 
(1,'special tour','Seoul',100000,'Seoul, the capital of South Korea, is a huge metropolis where modern skyscrapers, high-tech subways and pop culture meet Buddhist temples, palaces and street markets.','apple',NULL,'2021-12-04','2021-12-16'),
(2,'cheap tour','Ulsan',70000,'Ulsan, officially the Ulsan Metropolitan City is South Korea\'s seventh-largest metropolitan city and the eighth-largest city overall, with a population of over 1.1 million inhabitants.','samsung',NULL,'2021-12-02','2021-12-17'),
(3,'luxury tour','Jeju',200000,'Jeju City, on Jejudo Island, is the capital of South Korea\'s Jeju Province.','apple',NULL,'2021-12-01','2021-12-23'),
(4,'Dongdaemun tour','Seoul',150000,' Notable attractions include futuristic Dongdaemun Design Plaza, a convention hall with curving architecture and a rooftop park;','samsung',NULL,'2021-12-01','2021-12-23'),
(5,'hot-springs tour','Jeju',200000,'In the city, Sinsan Park has displays of marine animals at Jeju Folklore and Natural History Museum','samsung',NULL,'2021-12-01','2021-12-23');

/*Table structure for table Purchase */

CREATE TABLE Purchase (
  PurchaseID int unsigned NOT NULL AUTO_INCREMENT,
  ProductID int DEFAULT NULL,
  UserID int DEFAULT NULL,
  PurchaseDate datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  TotalPrice int DEFAULT NULL,
  Requirement char(255) DEFAULT NULL,
  CouponID int DEFAULT NULL,
  PRIMARY KEY (PurchaseID)
) AUTO_INCREMENT=3 ;

/*Data for the table Purchase */

insert  into Purchase(PurchaseID,ProductID,UserID,PurchaseDate,TotalPrice,Requirement,CouponID) values 
(1,1,1,'2021-12-01 00:00:00',30000,NULL,NULL),
(2,1,1,NULL,90000,NULL,1);

/*Table structure for table Region */

CREATE TABLE Region (
  RegionID int unsigned NOT NULL AUTO_INCREMENT,
  RegionName char(255) DEFAULT NULL,
  RegionDescription char(255) DEFAULT NULL,
  RegionGrade char(255) DEFAULT NULL,
  PRIMARY KEY (RegionID)
) AUTO_INCREMENT=4 ;

/*Data for the table Region */

insert  into Region(RegionID,RegionName,RegionDescription,RegionGrade) values 
(1,'Jeju',NULL,NULL),
(2,'Ulsan',NULL,NULL),
(3,'Seoul',NULL,NULL);

/*Table structure for table Review */

CREATE TABLE Review (
  ReviewID int unsigned NOT NULL AUTO_INCREMENT,
  ProductID int DEFAULT NULL,
  UserID int DEFAULT NULL,
  ReviewComment char(255) DEFAULT NULL,
  ReviewDate date DEFAULT NULL,
  ReviewGrade char(255) DEFAULT NULL,
  PRIMARY KEY (ReviewID)
) ;

/*Data for the table Review */

/*Table structure for table Userx */

CREATE TABLE Userx (
  UserID int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  UserName char(255) DEFAULT NULL,
  Gender char(255) DEFAULT NULL,
  Age int DEFAULT NULL,
  Email char(255) DEFAULT NULL,
  Phone char(255) DEFAULT NULL,
  Grade char(255) DEFAULT NULL,
  Enrolldate date DEFAULT NULL,
  Password char(255) DEFAULT NULL,
  PRIMARY KEY (UserID)
) AUTO_INCREMENT=4 ;

/*Data for the table Userx */

insert  into Userx(UserID,UserName,Gender,Age,Email,Phone,Grade,Enrolldate,Password) values 
(0000000001,'jobs','male',50,'1@a.com',NULL,NULL,NULL,'1234'),
(0000000002,'trump','male',50,'2@a.com',NULL,NULL,NULL,'1234'),
(0000000003,'turing','male',100,'3@a.com',NULL,NULL,NULL,'1234');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */
