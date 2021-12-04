/*
SQLyog Trial v13.1.8 (64 bit)
MySQL - 8.0.27-0ubuntu0.20.04.1 : Database - bbgg
*********************************************************************
*/

/*!40101 SET NAMES utf8 */

/*!40101 SET SQL_MODE=''*/

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */
-- CREATE DATABASE /*!32312 IF NOT EXISTS*/bbgg /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */

USE bbgg;

/*Table structure for table Cart */



CREATE TABLE Cart (
  ProductID int NOT NULL,
  UserID int NOT NULL,
  Amount int DEFAULT NULL,
  ProductName char(1) DEFAULT NULL,
  ProductPrice int DEFAULT NULL,
  PRIMARY KEY (ProductID,UserID)
) ;

/*Data for the table Cart */

/*Table structure for table Company */



CREATE TABLE Company (
  CompanyID int NOT NULL,
  CompanyName char(255) DEFAULT NULL,
  CompanyGrade char(255) DEFAULT NULL,
  CompanyDescription char(255) DEFAULT NULL,
  CompanyPhone char(255) DEFAULT NULL,
  CompanyEmail char(255) DEFAULT NULL,
  PRIMARY KEY (CompanyID)
) ;

/*Data for the table Company */

/*Table structure for table Coupon */



CREATE TABLE Coupon (
  CouponID int NOT NULL,
  DiscountAmount int DEFAULT NULL,
  UsedCheck tinyint(1) DEFAULT NULL,
  CouponDateUsed date DEFAULT NULL,
  CouponDateMade date DEFAULT NULL,
  PRIMARY KEY (CouponID)
) ;

/*Data for the table Coupon */

insert  into Coupon(CouponID,DiscountAmount,UsedCheck,CouponDateUsed,CouponDateMade) values 
(1,10000,0,NULL,NULL);

/*Table structure for table Product */



CREATE TABLE Product (
  ProductID int NOT NULL,
  ProductName char(255) DEFAULT NULL,
  ProductRegion char(255) DEFAULT NULL,
  ProductPrice int DEFAULT NULL,
  ProductDescription char(255) DEFAULT NULL,
  ProductCompany char(255) DEFAULT NULL,
  ProductStock char(255) DEFAULT NULL,
  ProductDateCreated date DEFAULT NULL,
  ProductDateTour date DEFAULT NULL,
  PRIMARY KEY (ProductID)
) ;

/*Data for the table Product */

insert  into Product(ProductID,ProductName,ProductRegion,ProductPrice,ProductDescription,ProductCompany,ProductStock,ProductDateCreated,ProductDateTour) values 
(1,'special_trip','seoul',100000,'special trip!!!','apple',NULL,'2021-12-04','2021-12-16');

/*Table structure for table Purchase */



CREATE TABLE Purchase (
  PurchaseID int NOT NULL,
  ProductID int DEFAULT NULL,
  UserID int DEFAULT NULL,
  PurchaseDate date DEFAULT NULL,
  TotalPrice int DEFAULT NULL,
  Requirement char(255) DEFAULT NULL,
  CouponID int DEFAULT NULL,
  PRIMARY KEY (PurchaseID)
) ;

/*Data for the table Purchase */

/*Table structure for table Region */



CREATE TABLE Region (
  RegionID int NOT NULL,
  RegionName char(255) DEFAULT NULL,
  RegionDescription char(255) DEFAULT NULL,
  RegionGrade char(255) DEFAULT NULL,
  PRIMARY KEY (RegionID)
) ;

/*Data for the table Region */

/*Table structure for table Review */



CREATE TABLE Review (
  ReviewID int NOT NULL,
  ProductID int DEFAULT NULL,
  UserID int DEFAULT NULL,
  ReviewComment char(255) DEFAULT NULL,
  ReviewDate date DEFAULT NULL,
  ReviewGrade char(255) DEFAULT NULL,
  PRIMARY KEY (ReviewID)
) ;

/*Data for the table Review */

/*Table structure for table User */



CREATE TABLE Userx (
  UserID int NOT NULL,
  UserName char(255) DEFAULT NULL,
  Gender char(255) DEFAULT NULL,
  Age int DEFAULT NULL,
  Email char(255) DEFAULT NULL,
  Phone char(255) DEFAULT NULL,
  Grade char(255) DEFAULT NULL,
  Enrolldate date DEFAULT NULL,
  Password char(255) DEFAULT NULL,
  PRIMARY KEY (UserID)
) ;

/*Data for the table User */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */
