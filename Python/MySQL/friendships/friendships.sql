/*
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema friendships
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friendships
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendships` DEFAULT CHARACTER SET utf8 ;
USE `friendships` ;

-- -----------------------------------------------------
-- Table `friendships`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendships`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `friendships`.`friendships`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendships`.`friendships` (
  `id` INT NULL,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  INDEX `fk_users_has_users_users2_idx` (`friend_id` ASC),
  INDEX `fk_users_has_users_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_users_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendships`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users2`
    FOREIGN KEY (`friend_id`)
    REFERENCES `friendships`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
*/

USE friendships ;

INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`, `updated_at`) VALUES ('Chris', 'Baker', NOW(), NOW());
INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`, `updated_at`) VALUES ('Diana', 'Smith', NOW(), NOW());
INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`, `updated_at`) VALUES ('James', 'Johnson', NOW(), NOW());
INSERT INTO `friendships`.`users` (`first_name`, `last_name`, `created_at`, `updated_at`) VALUES ('Jesica', 'Davidson', NOW(), NOW());

INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`, `created_at`, `updated_at`) VALUES ('7', '10', NOW(), NOW());
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`, `created_at`, `updated_at`) VALUES ('7', '9', NOW(), NOW());
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`, `created_at`, `updated_at`) VALUES ('7', '8', NOW(), NOW());
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`, `created_at`, `updated_at`) VALUES ('8', '7', NOW(), NOW());
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`, `created_at`, `updated_at`) VALUES ('9', '7', NOW(), NOW());
INSERT INTO `friendships`.`friendships` (`user_id`, `friend_id`, `created_at`, `updated_at`) VALUES ('10', '7', NOW(), NOW());

SELECT users.first_name, users.first_name , users2.first_name AS friend_fn , users2.last_name AS friend_ln
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 ON friendships.friend_id = users2.id 
ORDER BY 4











