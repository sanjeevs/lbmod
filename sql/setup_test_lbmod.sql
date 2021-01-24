CREATE DATABASE IF NOT EXISTS test_lbmod;
USE test_lbmod;

DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS products(
	`product_id` INT NOT NULL AUTO_INCREMENT,
	`sku` VARCHAR(20) UNIQUE NOT NULL,
	`upc` VARCHAR(20) NOT NULL,
	`name` VARCHAR(45),
	`description` VARCHAR(255),
	`category1` VARCHAR(45),
	`category2` VARCHAR(45),
	`storage` VARCHAR(45),
	`keywords` VARCHAR(255),
	`quantity` INT UNSIGNED DEFAULT 0,
	`price` DECIMAL(8,2) DEFAULT 0,
	`item_weight` DECIMAL(4,2) DEFAULT 0,
	`item_weight_unit` VARCHAR(16),
	`item_volume` DECIMAL(4,2) DEFAULT 0,
	`item_volume_unit` VARCHAR(16),
	`expiry_date` DATE,
	`items_per_case` INT DEFAULT 0,
	`case_wt` DECIMAL(4,2) DEFAULT 0,
	`case_wt_unit` VARCHAR(16),
	`case_dim` VARCHAR(8),
	`case_dim_unit` VARCHAR(8),
	`photo1` VARCHAR(255),
	`photo2` VARCHAR(255),
	`photo3` VARCHAR(255),
	`created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`last_updated` TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`product_id`)
);

DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(45) NOT NULL,
  `full_name` VARCHAR(45) NULL,
  `phone_number` VARCHAR(45) NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE INDEX `company_name_UNIQUE` (`company_name` ASC));

DROP TABLE IF EXISTS addresses;
CREATE TABLE IF NOT EXISTS addresses (
  `address_id` INT NOT NULL AUTO_INCREMENT,
  `contact_person` VARCHAR(45) NULL,
  `street_address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `zip_code` VARCHAR(45) NULL,
  `phone_number` VARCHAR(45) NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`address_id`, `customer_id`),
  INDEX `fk_addresses_customers1_idx` (`customer_id` ASC),
  CONSTRAINT `fk_addresses_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES customers (`customer_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
