CREATE DATABASE IF NOT EXISTS test_lbmod;
USE test_lbmod;

DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS products(
	`product_id` INT NOT NULL AUTO_INCREMENT,
	`sku` VARCHAR(20) UNIQUE NOT NULL,
	`upc` VARCHAR(20) NOT NULL,
	`name` VARCHAR(45) NOT NULL,
	`description` VARCHAR(255) NOT NULL,
	`category1` VARCHAR(45) NOT NULL,
	`category2` VARCHAR(45) NOT NULL,
	`storage` VARCHAR(45) NOT NULL,
	`keywords` VARCHAR(255) NOT NULL,
	`quantity` INT DEFAULT 0,
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

