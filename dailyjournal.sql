INSERT INTO `JournalEntries` VALUES (null, '2020-11-28','Filtering the moods',"Nashville software school. nashville,TN",1);
INSERT INTO `JournalEntries` VALUES (null, '2021-11-18','Frontend development',"I LOVE MY FAMLY AND NSS",2);
INSERT INTO `JournalEntries` VALUES (null, '2018-01-12','Filtering the moods',"FRONTEND DEVELOPER",3);
INSERT INTO `JournalEntries` VALUES (null, '2019-08-25','Filtering the moods',"BACKEND DEVELOPER",4);
INSERT INTO `JournalEntries` VALUES (null, '2017-03-20','Frontend development',"I LOVE MY LIFE AND NSS",5);


INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Frustated");
INSERT INTO `Moods` VALUES (null, "Ok");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Angry");

DELETE FROM `JournalEntries`;
DROP TABLE `JournalEntries`;
UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'JournalEntries';

INSERT INTO `Tag` VALUES (null, "John");
INSERT INTO `Tag` VALUES (null, "Joe");
INSERT INTO `Tag` VALUES (null, "Jake");


INSERT INTO `entry_tag` VALUES (null,1,2);
INSERT INTO `entry_tag` VALUES (null, 2,3);
INSERT INTO `entry_tag` VALUES (null, 3,4);
INSERT INTO `entry_tag` VALUES (null, 5,6);


CREATE TABLE `JournalEntries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	DATE NOT NULL,
	`concept`	TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `moodsId` INTEGER NOT NULL,
    FOREIGN KEY(`moodsId`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL    
);

CREATE TABLE `Tag` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL
);

CREATE TABLE `entry_tag` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id` INTEGER,
    `tag_id` INTEGER,
    FOREIGN KEY(`entry_id`) REFERENCES `JournalEntries`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tag`(`id`)
);
