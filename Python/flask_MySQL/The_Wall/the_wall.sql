/*
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema The_Wall
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema The_Wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `The_Wall` DEFAULT CHARACTER SET utf8 ;
USE `The_Wall` ;

-- -----------------------------------------------------
-- Table `The_Wall`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_Wall`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `salt`  VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `The_Wall`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_Wall`.`messages` (
  `message_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `message` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`message_id`),
  INDEX `fk_messages_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `The_Wall`.`users` (`user_id`)
    ON DELETE NO ACTIONmeggagemeggage
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `The_Wall`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_Wall`.`comments` (
  `comment_id` INT NOT NULL AUTO_INCREMENT,
  `message_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `commentscol` VARCHAR(45) NULL,
  PRIMARY KEY (`comment_id`),
  INDEX `fk_comments_messages1_idx` (`message_id` ASC),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`message_id`)
    REFERENCES `The_Wall`.`messages` (`message_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `The_Wall`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
*/


select * FROM users; 
select * FROM messages; 

select * FROM comments; 


SELECT CONCAT(users.first_name, ' ',users.last_name) AS name, messages.message_id, messages.user_id,
messages.message, date_format( messages.created_at, '%M %D %Y') AS date, messages.created_at
FROM messages 
JOIN users ON messages.user_id = users.user_id 
ORDER BY messages.created_at ;











messages












