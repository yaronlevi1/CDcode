CREATE SCHEMA `email_validation` ;

USE email_validation ;

CREATE TABLE `email_validation`.`emails` (
  `email_id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`email_id`));

INSERT INTO `email_validation`.`emails` (`email`, `created_at`, `updated_at`) VALUES ('sss@gmail.com', NOW(), NOW());
INSERT INTO `email_validation`.`emails` (`email`, `created_at`, `updated_at`) VALUES ('ggg@gmail.com', NOW(), NOW());
INSERT INTO `email_validation`.`emails` (`email`, `created_at`, `updated_at`) VALUES ('ttt@gmail.com', NOW(), NOW());


SELECT * FROM emails ;

