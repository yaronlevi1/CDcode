CREATE SCHEMA `friends_assignemnt` ;

USE friends_assignemnt ;

CREATE TABLE `friends_assignemnt`.`friends` (
  `friend_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`friend_id`));

INSERT INTO `friends_assignemnt`.`friends` (`name`, `age`, `created_at`, `updated_at`) VALUES ('Jay Patel', 190,  NOW(), NOW());
INSERT INTO `friends_assignemnt`.`friends` (`name`, `age`, `created_at`, `updated_at`) VALUES ('Brendan Stanton', 175,  NOW(), NOW());


SELECT * FROM friends ;

SELECT name, age, DATE_FORMAT(created_at, '%b %D') AS date,  YEAR(created_at) AS year FROM friends