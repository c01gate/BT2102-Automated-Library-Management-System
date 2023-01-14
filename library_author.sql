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
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author` (
  `accession_number` varchar(45) NOT NULL,
  `author_name` varchar(45) NOT NULL,
  PRIMARY KEY (`author_name`,`accession_number`),
  KEY `book_id_idx` (`accession_number`),
  CONSTRAINT `book_id` FOREIGN KEY (`accession_number`) REFERENCES `book` (`accession_number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES ('A01','George Orwell'),('A02','Gabrial Garcia Marquez'),('A03','Aldous Huxley'),('A04','Fyodor Dostoevsky'),('A05','C.S. Lewis'),('A06','Mary Shelley'),('A07','John Steinbeck'),('A08','Mark Twain'),('A09','Charles Dickens'),('A10','Joseph Heller'),('A11','Homer'),('A12','Victor Hugo'),('A13','James Joyce'),('A14','Vladimir Nabokov'),('A15','Ayn Rand'),('A16','Patrick Suskind'),('A17','Franz Kafka'),('A18','Bret Easton Ellis'),('A19','Albert Uderzo'),('A19','Rene Goscinny'),('A20','Ray Bradbury'),('A21','Isaac Asimov'),('A22','Friedrich Engels'),('A22','Karl Marx'),('A23','Thomas Paine'),('A24','Niccolo Machiavelli'),('A25','Adam Smith'),('A26','Miguel de Cervantes Saavedra'),('A27','Simone de Beauvoir'),('A28','Immanuel Kant'),('A29','Charles Darwin'),('A30','Isaac Newton'),('A31','Milan Kundera'),('A32','Sun Tzu'),('A33','Jorge Luis Borges'),('A34','Gabriel Garcia Marquez'),('A35','Juan Rulfo'),('A36','Octavio Paz'),('A37','Pablo Neruda'),('A38','Richard Feynman'),('A39','Stephen Hawking'),('A40','Carl Sagan'),('A41','Martin Gardner'),('A41','Silvanus P. Thompson'),('A42','Enrico Fermi'),('A43','Alexander Hamilton'),('A43','James Madison'),('A43','John Jay'),('A44','C. B. Macpherson'),('A44','John Lcke'),('A45','Karl Popper'),('A46','Howard Zinn'),('A47','William Golding'),('A48','George Orwell'),('A49','Ernest Hemingway'),('A50','Luo Guanzhong');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
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
