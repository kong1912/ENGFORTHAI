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
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word_list`
--

LOCK TABLES `word_list` WRITE;
/*!40000 ALTER TABLE `word_list` DISABLE KEYS */;
INSERT INTO `word_list` VALUES (1,'athlete','1','1'),(2,'health','1','1'),(3,'depth','1','1'),(4,'thatch','1','1'),(5,'atheist','1','1'),(6,'oath ','1','1'),(7,'path','1','1'),(8,'though ','1','1'),(9,'leather','1','1'),(10,'writhe','1','1'),(11,'theorist','1','1'),(12,'father','1','1'),(13,'earthwork','1','1'),(14,'stealth','1','1'),(15,'ratio','2','2'),(16,'chicanery','2','2'),(17,'tuition','2','2'),(18,'initially ','2','2'),(19,'dictionary ','2','2'),(20,'flush','2','2'),(21,'privileges','2','2'),(22,'convention','2','2'),(23,'charade','2','2'),(24,'decision','2','2'),(25,'rouge','2','2'),(26,'confusion','2','2'),(27,'bashful','2','2'),(28,'vegetable','3','3'),(29,'margarine','3','3'),(30,'jewelry','3','3'),(31,'fragile','3','3'),(32,'teenager','3','3'),(33,'Judge','3','3'),(34,'Charge','3','3'),(35,'orchard','3','3'),(36,'inch','3','3'),(37,'larch','3','3'),(38,'jerk','3','3'),(39,'urgent','3','3'),(40,'huge','3','3'),(41,'etching','3','3'),(42,'riches','3','3'),(43,'choke','3','3'),(44,'cruise','4','4'),(45,'dessert ','4','4'),(46,'excite','4','4'),(47,'Caves','4','4'),(48,'raise','4','4'),(49,'disease','4','4'),(50,'decease ','4','4'),(51,'compromise','4','4'),(52,'shelves','4','4'),(53,'overseas ','4','4'),(54,'finalize ','4','4'),(55,'enthusiast','4','4'),(56,'realize','4','4'),(57,'process','4','4'),(58,'successor','4','4'),(59,'securely','4','4'),(60,'costly','4','4'),(61,'task ','4','4'),(62,'dispose','4','4'),(63,'belonging','5','5'),(64,'grasp','5','5'),(65,'dapple','5','5'),(66,'dabble','5','5'),(67,'rope','5','5'),(68,'robe','5','5'),(69,' fierce','5','5'),(70,'stamp','5','5'),(71,'correspondence ','5','5'),(72,'proposal ','5','5'),(73,'picnic','5','5'),(74,'ramp','5','5');
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

-- Dump completed on 2022-04-25 11:26:40
