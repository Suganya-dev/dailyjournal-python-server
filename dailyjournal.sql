INSERT INTO `JournalEntries` VALUES (null, '2020-11-28','Filtering the moods','1605579733872','0');
INSERT INTO `JournalEntries` VALUES (null, '2021-11-18','Frontend development','1123568933872','0');
INSERT INTO `JournalEntries` VALUES (null, '2018-01-12','Filtering the moods','1605579733872','0');
INSERT INTO `JournalEntries` VALUES (null, '2019-08-25','Filtering the moods','1605579733872','0');
INSERT INTO `JournalEntries` VALUES (null, '2017-03-20','Frontend development','1605579733872','0');


INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Frustated");
INSERT INTO `Moods` VALUES (null, "Ok");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Angry");



CREATE TABLE `JournalEntries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	DATE NOT NULL,
	`concept`	TEXT NOT NULL,
    `timestamp` FLOAT,
    `moodsId` INTEGER NOT NULL,
    FOREIGN KEY(`moodsId`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL    
);

CREATE TABLE `Tags` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `body`    TEXT NOT NULL,
);

CREATE TABLE `Entrytags` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title`    TEXT NOT NULL,
    `author`  TEXT NOT NULL,
    `moodsId`  INTEGER NOT NULL,
    `tagsId`  INTEGER NOT NULL,
    FOREIGN KEY(`moodsId`) REFERENCES `Moods`(`id`),
    FOREIGN KEY(`tagsId`) REFERENCES `Tags`(`id`)
);
