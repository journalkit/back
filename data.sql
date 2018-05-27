DROP TABLE IF EXISTS `Discipline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Discipline` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO `Discipline` VALUES (1,'test',2);


DROP TABLE IF EXISTS `Exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Exam` (
  `id` int(11) DEFAULT NULL,
  `date` text,
  `closed` text,
  `discipline_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO `Exam` VALUES (1,'','0',1,1);


DROP TABLE IF EXISTS `Examlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Examlist` (
  `id` int(11) DEFAULT NULL,
  `ticket` varchar(256) DEFAULT NULL,
  `mark` varchar(1) DEFAULT NULL,
  `exam_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `Examlist` DISABLE KEYS */;
INSERT INTO `Examlist` VALUES (1,'1','4',1,1);
/*!40000 ALTER TABLE `Examlist` ENABLE KEYS */;


DROP TABLE IF EXISTS `Group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Group` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `Group` DISABLE KEYS */;
INSERT INTO `Group` VALUES (1,'test');
/*!40000 ALTER TABLE `Group` ENABLE KEYS */;


DROP TABLE IF EXISTS `Lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Lesson` (
  `id` int(11) DEFAULT NULL,
  `date` text,
  `control1` varchar(256) DEFAULT NULL,
  `control2` varchar(256) DEFAULT NULL,
  `statement_id` int(11) DEFAULT NULL,
  `theme_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40000 ALTER TABLE `Lesson` DISABLE KEYS */;
INSERT INTO `Lesson` VALUES (1,'','123','456',1,1);
/*!40000 ALTER TABLE `Lesson` ENABLE KEYS */;


DROP TABLE IF EXISTS `Record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Record` (
  `id` int(11) DEFAULT NULL,
  `mark1` varchar(1) DEFAULT NULL,
  `mark2` varchar(1) DEFAULT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `Record` DISABLE KEYS */;
INSERT INTO `Record` VALUES (1,'5','*',1,1);
/*!40000 ALTER TABLE `Record` ENABLE KEYS */;


DROP TABLE IF EXISTS `Role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Role` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `docs` text,
  `exams` text,
  `lessons` text,
  `users` text
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `Role` DISABLE KEYS */;
INSERT INTO `Role` VALUES (1,'Администратор','0','0','0','1'),(2,'Учитель','0','0','0','0'),(3,'Методист','0','0','0','0');
/*!40000 ALTER TABLE `Role` ENABLE KEYS */;


DROP TABLE IF EXISTS `Statement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Statement` (
  `id` int(11) DEFAULT NULL,
  `date_open` text,
  `date_close` text,
  `discipline_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `Statement` DISABLE KEYS */;
INSERT INTO `Statement` VALUES (1,'','',1,1);
/*!40000 ALTER TABLE `Statement` ENABLE KEYS */;


DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Student` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `surname` varchar(256) DEFAULT NULL,
  `patronymic` varchar(256) DEFAULT NULL,
  `record_book` varchar(256) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES (1,'Чугаев','Михаил','Александрович','123456',1);
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;


DROP TABLE IF EXISTS `Theme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Theme` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `discipline_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `Theme` DISABLE KEYS */;
INSERT INTO `Theme` VALUES (1,'test',1);
/*!40000 ALTER TABLE `Theme` ENABLE KEYS */;


DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) DEFAULT NULL,
  `login` varchar(256) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `token` varchar(256) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `surname` varchar(256) DEFAULT NULL,
  `patronymic` varchar(256) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
);
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'admin','1','1','Михаил','Чугаев','Александрович',1),(2,'test','1','1','1','2','3',2);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;

CREATE INDEX "discipline_teacher_id_ab7e3b81" ON "Discipline" ("teacher_id");
CREATE INDEX "exam_discipline_id_cb965ae4" ON "Exam" ("discipline_id");
CREATE INDEX "exam_group_id_5711c249" ON "Exam" ("group_id");
CREATE INDEX "examlist_exam_id_1cfd6d83" ON "Examlist" ("exam_id");
CREATE INDEX "examlist_student_id_fe280f39" ON "Examlist" ("student_id");
CREATE INDEX "lesson_statement_id_d8ac53a3" ON "Lesson" ("statement_id");
CREATE INDEX "lesson_theme_id_82de6453" ON "Lesson" ("theme_id");
CREATE INDEX "record_lesson_id_093969c3" ON "Record" ("lesson_id");
CREATE INDEX "record_student_id_47718c76" ON "Record" ("student_id");
CREATE INDEX "statement_discipline_id_3d9acc4a" ON "Statement" ("discipline_id");
CREATE INDEX "statement_group_id_d4b5af7d" ON "Statement" ("group_id");
CREATE INDEX "student_group_id_43a5025f" ON "Student" ("group_id");
CREATE INDEX "theme_discipline_id_dd93c59f" ON "Theme" ("discipline_id");
CREATE INDEX "user_role_id_0b60389b" ON "User" ("role_id");