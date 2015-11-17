-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema inventationery
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema inventationery
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `inventationery` DEFAULT CHARACTER SET utf8 ;
USE `inventationery` ;

-- -----------------------------------------------------
-- Table `inventationery`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`auth_group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(80) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `name` (`name` ASC)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`django_content_type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `app_label` VARCHAR(100) NOT NULL COMMENT '',
  `model` VARCHAR(100) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `django_content_type_app_label_3ec8c61c_uniq` (`app_label` ASC, `model` ASC)  COMMENT '')
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`auth_permission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(255) NOT NULL COMMENT '',
  `content_type_id` INT(11) NOT NULL COMMENT '',
  `codename` VARCHAR(100) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `content_type_id` (`content_type_id` ASC, `codename` ASC)  COMMENT '',
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `inventationery`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 40
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`auth_group_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `group_id` INT(11) NOT NULL COMMENT '',
  `permission_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `group_id` (`group_id` ASC, `permission_id` ASC)  COMMENT '',
  INDEX `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id` ASC)  COMMENT '',
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id`
    FOREIGN KEY (`permission_id`)
    REFERENCES `inventationery`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `inventationery`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`auth_user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `password` VARCHAR(128) NOT NULL COMMENT '',
  `last_login` DATETIME NULL DEFAULT NULL COMMENT '',
  `is_superuser` TINYINT(1) NOT NULL COMMENT '',
  `username` VARCHAR(30) NOT NULL COMMENT '',
  `first_name` VARCHAR(30) NOT NULL COMMENT '',
  `last_name` VARCHAR(30) NOT NULL COMMENT '',
  `email` VARCHAR(254) NOT NULL COMMENT '',
  `is_staff` TINYINT(1) NOT NULL COMMENT '',
  `is_active` TINYINT(1) NOT NULL COMMENT '',
  `date_joined` DATETIME NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `username` (`username` ASC)  COMMENT '')
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`auth_user_groups` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `user_id` INT(11) NOT NULL COMMENT '',
  `group_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `user_id` (`user_id` ASC, `group_id` ASC)  COMMENT '',
  INDEX `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id` ASC)  COMMENT '',
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `inventationery`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `inventationery`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`auth_user_user_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `user_id` INT(11) NOT NULL COMMENT '',
  `permission_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `user_id` (`user_id` ASC, `permission_id` ASC)  COMMENT '',
  INDEX `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id` ASC)  COMMENT '',
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id`
    FOREIGN KEY (`permission_id`)
    REFERENCES `inventationery`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `inventationery`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`dirparty_dirpartymodel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`dirparty_dirpartymodel` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `Name` VARCHAR(60) NOT NULL COMMENT '',
  `NameAlias` VARCHAR(50) NULL DEFAULT NULL COMMENT '',
  `LanguageCode` VARCHAR(5) NOT NULL COMMENT '',
  `SecondName` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `FirstLastName` VARCHAR(30) NOT NULL COMMENT '',
  `SecondLastName` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `Gender` VARCHAR(1) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`django_admin_log` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `action_time` DATETIME NOT NULL COMMENT '',
  `object_id` LONGTEXT NULL DEFAULT NULL COMMENT '',
  `object_repr` VARCHAR(200) NOT NULL COMMENT '',
  `action_flag` SMALLINT(5) UNSIGNED NOT NULL COMMENT '',
  `change_message` LONGTEXT NOT NULL COMMENT '',
  `content_type_id` INT(11) NULL DEFAULT NULL COMMENT '',
  `user_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id` ASC)  COMMENT '',
  INDEX `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id` ASC)  COMMENT '',
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `inventationery`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `inventationery`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`django_migrations` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `app` VARCHAR(255) NOT NULL COMMENT '',
  `name` VARCHAR(255) NOT NULL COMMENT '',
  `applied` DATETIME NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL COMMENT '',
  `session_data` LONGTEXT NOT NULL COMMENT '',
  `expire_date` DATETIME NOT NULL COMMENT '',
  PRIMARY KEY (`session_key`)  COMMENT '',
  INDEX `django_session_de54fa62` (`expire_date` ASC)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`vendor_vendmodel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`vendor_vendmodel` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `AccountNum` VARCHAR(5) NOT NULL COMMENT '',
  `AccountType` VARCHAR(3) NOT NULL COMMENT '',
  `OneTimeVendor` TINYINT(1) NOT NULL COMMENT '',
  `VendGroup` VARCHAR(3) NOT NULL COMMENT '',
  `CreditLimit` DECIMAL(15,2) NULL DEFAULT NULL COMMENT '',
  `CurrencyCode` VARCHAR(3) NOT NULL COMMENT '',
  `VATNum` VARCHAR(13) NULL DEFAULT NULL COMMENT '',
  `Notes` LONGTEXT NULL DEFAULT NULL COMMENT '',
  `Party_id` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `AccountNum` (`AccountNum` ASC)  COMMENT '',
  UNIQUE INDEX `Party_id` (`Party_id` ASC)  COMMENT '',
  CONSTRAINT `Vendor_vendmodel_Party_id_274be844_fk_DirParty_dirpartymodel_id`
    FOREIGN KEY (`Party_id`)
    REFERENCES `inventationery`.`dirparty_dirpartymodel` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`inventory_inventmodel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`inventory_inventmodel` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `ItemId` VARCHAR(20) NOT NULL COMMENT '',
  `ItemName` VARCHAR(50) NOT NULL COMMENT '',
  `Description` VARCHAR(100) NULL DEFAULT NULL COMMENT '',
  `UnitId` VARCHAR(20) NOT NULL COMMENT '',
  `Price` DECIMAL(10,2) NOT NULL COMMENT '',
  `VendorPrice` DECIMAL(10,2) NOT NULL COMMENT '',
  `ItemImage` VARCHAR(100) NULL DEFAULT NULL COMMENT '',
  `PrimaryVendor_id` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `ItemId` (`ItemId` ASC)  COMMENT '',
  INDEX `Inventory_inven_PrimaryVendor_id_6c249590_fk_Vendor_vendmodel_id` (`PrimaryVendor_id` ASC)  COMMENT '',
  CONSTRAINT `Inventory_inven_PrimaryVendor_id_6c249590_fk_Vendor_vendmodel_id`
    FOREIGN KEY (`PrimaryVendor_id`)
    REFERENCES `inventationery`.`vendor_vendmodel` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`logisticselectronicaddress_logisticselectronicaddressmodel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`logisticselectronicaddress_logisticselectronicaddressmodel` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `Description` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `Type` VARCHAR(30) NOT NULL COMMENT '',
  `Contact` VARCHAR(200) NULL DEFAULT NULL COMMENT '',
  `IsPrimary` TINYINT(1) NOT NULL COMMENT '',
  `Party_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `LogisticsElectron_Party_id_1a2e93e9_fk_DirParty_dirpartymodel_id` (`Party_id` ASC)  COMMENT '',
  CONSTRAINT `LogisticsElectron_Party_id_1a2e93e9_fk_DirParty_dirpartymodel_id`
    FOREIGN KEY (`Party_id`)
    REFERENCES `inventationery`.`dirparty_dirpartymodel` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`logisticspostaladdress_logisticspostaladdressmodel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`logisticspostaladdress_logisticspostaladdressmodel` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `Description` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `Purpose` VARCHAR(30) NOT NULL COMMENT '',
  `CountryRegionId` VARCHAR(3) NOT NULL COMMENT '',
  `ZipCode` VARCHAR(5) NULL DEFAULT NULL COMMENT '',
  `Street` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `StreetNumber` SMALLINT(5) UNSIGNED NULL DEFAULT NULL COMMENT '',
  `BuildingCompliment` VARCHAR(10) NULL DEFAULT NULL COMMENT '',
  `City` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `State` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `IsPrimary` TINYINT(1) NOT NULL COMMENT '',
  `Party_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `LogisticsPostalAd_Party_id_586bf4bd_fk_DirParty_dirpartymodel_id` (`Party_id` ASC)  COMMENT '',
  CONSTRAINT `LogisticsPostalAd_Party_id_586bf4bd_fk_DirParty_dirpartymodel_id`
    FOREIGN KEY (`Party_id`)
    REFERENCES `inventationery`.`dirparty_dirpartymodel` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`purchorder_purchordermodel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`purchorder_purchordermodel` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `PurchId` VARCHAR(45) NOT NULL COMMENT '',
  `PurchName` VARCHAR(100) NOT NULL COMMENT '',
  `PurchaseType` VARCHAR(50) NOT NULL COMMENT '',
  `OrderAccount` VARCHAR(50) NOT NULL COMMENT '',
  `InvoiceAccount` VARCHAR(50) NULL DEFAULT NULL COMMENT '',
  `PurchStatus` VARCHAR(100) NOT NULL COMMENT '',
  `WorkerPurchPlacer` VARCHAR(100) NULL DEFAULT NULL COMMENT '',
  `LanguageCode` VARCHAR(5) NOT NULL COMMENT '',
  `DeliveryName` VARCHAR(200) NULL DEFAULT NULL COMMENT '',
  `DeliveryDate` DATE NULL DEFAULT NULL COMMENT '',
  `ConfirmedDlv` DATE NULL DEFAULT NULL COMMENT '',
  `DlvMode` VARCHAR(20) NOT NULL COMMENT '',
  `CurrencyCode` VARCHAR(3) NOT NULL COMMENT '',
  `Payment` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `PaymMode` VARCHAR(30) NULL DEFAULT NULL COMMENT '',
  `CashDisc` DECIMAL(10,2) NULL DEFAULT NULL COMMENT '',
  `CashDiscPercent` DECIMAL(4,2) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `PurchId` (`PurchId` ASC)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `inventationery`.`purchorder_purchlinemodel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `inventationery`.`purchorder_purchlinemodel` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  `modified` DATETIME NOT NULL COMMENT '',
  `PurchId` VARCHAR(45) NOT NULL COMMENT '',
  `ItemId` VARCHAR(20) NOT NULL COMMENT '',
  `ItemName` VARCHAR(50) NOT NULL COMMENT '',
  `PurchQty` INT(10) UNSIGNED NOT NULL COMMENT '',
  `PurchUnit` VARCHAR(20) NOT NULL COMMENT '',
  `PurchPrice` DOUBLE NOT NULL COMMENT '',
  `LineDisc` DECIMAL(10,2) NOT NULL COMMENT '',
  `LinePercent` DECIMAL(10,2) NOT NULL COMMENT '',
  `LineAmount` DECIMAL(20,2) NOT NULL COMMENT '',
  `PurchLineStatus` VARCHAR(100) NOT NULL COMMENT '',
  `LineNum` SMALLINT(5) UNSIGNED NOT NULL COMMENT '',
  `PurchOrder_id` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `PurchId` (`PurchId` ASC)  COMMENT '',
  INDEX `PurchOrder_purchlinemodel_6727a990` (`PurchOrder_id` ASC)  COMMENT '',
  CONSTRAINT `PurchOrde_PurchOrder_id_d6281f5_fk_PurchOrder_purchordermodel_id`
    FOREIGN KEY (`PurchOrder_id`)
    REFERENCES `inventationery`.`purchorder_purchordermodel` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
