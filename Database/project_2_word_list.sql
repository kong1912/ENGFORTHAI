-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: project_2
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `word_list`
--

DROP TABLE IF EXISTS `word_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `word_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `word` varchar(45) NOT NULL,
  `lesson` varchar(45) NOT NULL,
  `stress` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word_list`
--

LOCK TABLES `word_list` WRITE;
/*!40000 ALTER TABLE `word_list` DISABLE KEYS */;
INSERT INTO `word_list` VALUES (1,'altogether','1','1_1'),(2,'smooth','1','1_1'),(3,'though','1','1_1'),(4,'writhe','1','1_1'),(5,'eight','1','1_2'),(6,'hundredth','1','1_2'),(7,'width','1','1_2'),(8,'athlete','1','1_3'),(9,'hypothesis','1','1_3'),(10,'stealth','1','1_3'),(11,'theorist','1','1_3'),(12,'bashful','2','2_1'),(13,'chicanery','2','2_1'),(14,'distinguish','2','2_1'),(15,'flush','2','2_1'),(16,'ratio','2','2_1'),(17,'shipment','2','2_1'),(18,'camouflage','2','2_2'),(19,'jupe','2','2_2'),(20,'jus','2','2_2'),(21,'luxury','2','2_2'),(22,'sabotage','2','2_2'),(23,'unusual','2','2_2'),(34,'charge','3','3_1'),(35,'fragile','3','3_1'),(36,'indulge','3','3_1'),(37,'jewelry','3','3_1'),(38,'judge','3','3_1'),(39,'vegetable','3','3_1'),(40,'challenge','3','3_2'),(41,'choke','3','3_2'),(42,'etching','3','3_2'),(43,'larch','3','3_2'),(44,'purchase','3','3_2'),(45,'starch','3','3_2'),(46,'decease','4','4_1'),(47,'overseas','4','4_1'),(48,'practice','4','4_1'),(49,'process','4','4_1'),(50,'securely','4','4_1'),(51,'successor','4','4_1'),(52,'criticize','4','4_2'),(53,'emphasize','4','4_2'),(54,'enzyme','4','4_2'),(55,'equalizer','4','4_2'),(56,'zealous','4','4_2'),(57,'zipper','4','4_2'),(58,'belonging','5','5_1'),(59,'bilingual','5','5_1'),(60,'dabble','5','5_1'),(61,'orbit','5','5_1'),(62,'reverb','5','5_1'),(63,'robe','5','5_1'),(64,'appellate','5','5_2'),(65,'correspondence','5','5_2'),(66,'landscape','5','5_2'),(67,'pathogens','5','5_2'),(68,'proposal','5','5_2'),(69,'rope','5','5_2');
/*!40000 ALTER TABLE `word_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-02 20:57:48
