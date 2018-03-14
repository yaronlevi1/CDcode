CREATE SCHEMA `login_and_registration` ;

USE login_and_registration ;

CREATE TABLE `login_and_registration`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `salt` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`user_id`));

INSERT INTO `login_and_registration`.`users` (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES ('John', 'Bon', 'Jovi@hotmail.com', 'volvo', NOW(), NOW());

SELECT * FROM users ;

