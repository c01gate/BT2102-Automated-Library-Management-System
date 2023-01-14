CREATE DATABASE  IF NOT EXISTS `library` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library`;
-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: library
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `accession_number` varchar(45) NOT NULL,
  `title` varchar(256) NOT NULL,
  `isbn` bigint NOT NULL,
  `publisher` varchar(45) NOT NULL,
  `pub_year` int NOT NULL,
  `borrow_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `membership_id_borrowed` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`accession_number`),
  KEY `membership_id_loaned_idx` (`membership_id_borrowed`),
  CONSTRAINT `membership_id_loaned` FOREIGN KEY (`membership_id_borrowed`) REFERENCES `Membership` (`membership_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES ('A01','A 1984 Story',9790000000001,'Intra S.r.l.s.',2017,NULL,NULL,NULL,NULL),('A02','100 anos de soledad',9790000000002,'Vintage Espanol',2017,NULL,NULL,NULL,NULL),('A03','Brave New World',9790000000003,'Harper Perennial',2006,NULL,NULL,NULL,NULL),('A04','Crime and Punishment',9790000000004,'Penguin',2002,NULL,NULL,NULL,NULL),('A05','The Lion, The Witch and The Wardrobe',9790000000005,'Harper Collins',2002,NULL,NULL,NULL,NULL),('A06','Frankenstein',9790000000006,'Reader\'s Library Classics',2021,NULL,NULL,NULL,NULL),('A07','The Grapes of Wrath',9790000000007,'Penguin Classics',2006,NULL,NULL,NULL,NULL),('A08','The Adventures of Huckleberry Finn',9790000000008,'SeaWolf Press',2021,NULL,NULL,NULL,NULL),('A09','Great Expectations',9790000000009,'Penguin Classics',2002,NULL,NULL,NULL,NULL),('A10','Catch-22',9790000000010,'Simon & Schuster',2011,NULL,NULL,NULL,NULL),('A11','The Iliad',9790000000011,'Penguin Classics',1998,NULL,NULL,NULL,NULL),('A12','Les Miserables',9790000000012,'Signet',2013,NULL,NULL,NULL,NULL),('A13','Ulysses',9790000000013,'Vintage',1990,NULL,NULL,NULL,NULL),('A14','Lolita',9790000000014,'Vintage',1989,NULL,NULL,NULL,NULL),('A15','Atlas Shrugged',9790000000015,'Dutton',2005,NULL,NULL,NULL,NULL),('A16','Perfume',9790000000016,'Papercutz',2020,NULL,NULL,NULL,NULL),('A17','The Metamorphosis',9790000000017,'12th Media Service',2017,NULL,NULL,NULL,NULL),('A18','American Psycho',9790000000018,'ROBERT LAFFONT',2019,NULL,NULL,NULL,NULL),('A19','Asterix the Gaul',9790000000019,'Papercutz',2020,NULL,NULL,NULL,NULL),('A20','Fahrenheit',9790000000020,'Simon & Schuster',2012,NULL,NULL,NULL,NULL),('A21','Foundation',9790000000021,'Bantam Spectra Books',1991,NULL,NULL,NULL,NULL),('A22','The Communist Manifesto',9790000000022,'Penguin Classics',2002,NULL,NULL,NULL,NULL),('A23','\"Rights of Man, Common Sense, and Other Political Writings\"',9790000000023,'Oxford University Press',2009,NULL,NULL,NULL,NULL),('A24','The Prince',9790000000024,'Independently published',2019,NULL,NULL,NULL,NULL),('A25','The Wealth of Nations',9790000000025,'Royal Classics',2021,NULL,NULL,NULL,NULL),('A26','Don Quijote',9790000000026,'Ecco',2005,NULL,NULL,NULL,NULL),('A27','The Second Sex',9790000000027,'Vintage',2011,NULL,NULL,NULL,NULL),('A28','Critique of Pure Reason',9790000000028,'Cambridge University Press',1999,NULL,NULL,NULL,NULL),('A29','On The Origin of Species',9790000000029,'Signet',2003,NULL,NULL,NULL,NULL),('A30','Philosophae Naturalis Principia Mathematica',9790000000030,'University of California Press',2016,NULL,NULL,NULL,NULL),('A31','The Unbearable Lightness of Being',9790000000031,'Harper Perennial Modern Classics',2009,NULL,NULL,NULL,NULL),('A32','The Art of War',9790000000032,'LSC Communications',2007,NULL,NULL,NULL,NULL),('A33','Ficciones',9790000000033,'Penguin Books',1999,NULL,NULL,NULL,NULL),('A34','El Amor en Los Tiempos del Colera',9790000000034,'Vintage',2007,NULL,NULL,NULL,NULL),('A35','Pedro Paramo',9790000000035,'Grove Press',1994,NULL,NULL,NULL,NULL),('A36','The Labyrinth of Solitude',9790000000036,'Penguin Books',2008,NULL,NULL,NULL,NULL),('A37','Twenty Love Poems and a Song of Despair',9790000000037,'Penguin Classics',2006,NULL,NULL,NULL,NULL),('A38','QED: The Strange Theory of Light and Matter',9790000000038,'Princeton University Press',2014,NULL,NULL,NULL,NULL),('A39','A Brief History of Time',9790000000039,'Bantam',1996,NULL,NULL,NULL,NULL),('A40','Cosmos',9790000000040,'Ballantine Books',2013,NULL,NULL,NULL,NULL),('A41','Calculus Made Easy',9790000000041,'St Martins Pr',1970,NULL,NULL,NULL,NULL),('A42','Notes on Thermodynamics and Statistics',9790000000042,'University of Chicago Press',1988,NULL,NULL,NULL,NULL),('A43','The Federalist,Alexander Hamilton',9790000000043,'Coventry House Publishing',2015,NULL,NULL,NULL,NULL),('A44','Second Treatise of Government',9790000000044,'\"Hackett Publishing Company, Inc.\"',1980,NULL,NULL,NULL,NULL),('A45','The Open Society and Its Enemies',9790000000045,'Princeton University Press',2020,NULL,NULL,NULL,NULL),('A46','A People\'s History of the United States',9790000000046,'Harper Perennial Modern Classics',2015,NULL,NULL,NULL,NULL),('A47','Lord of the Flies',9790000000047,'Penguin Books',2003,NULL,NULL,NULL,NULL),('A48','Animal farm',9790000000048,'Wisehouse Classics',2021,NULL,NULL,NULL,NULL),('A49','The Old Man and the Sea',9790000000049,'Scribner',1995,NULL,NULL,NULL,NULL),('A50','Romance of the Three Kingdoms',9790000000050,'Penguin Books',2018,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-11  0:58:23
