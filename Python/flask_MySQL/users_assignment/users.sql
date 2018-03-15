CREATE SCHEMA `users_assignemnt` ;

USE users_assignemnt ;


CREATE TABLE `users_assignemnt`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`user_id`));


DELETE FROM users
WHERE user_id=5 ;

UPDATE users SET first_name='rrrrrr', last_name='eeeeeeeeeeeeee', email='rrrrr' WHERE user_id='2';


SELECT * FROM users ;