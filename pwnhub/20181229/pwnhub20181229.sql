/*
 Navicat Premium Data Transfer

 Source Server         : Localhost
 Source Server Type    : MySQL
 Source Server Version : 100310
 Source Host           : localhost:3306
 Source Schema         : pwnhub20181229

 Target Server Type    : MySQL
 Target Server Version : 100310
 File Encoding         : 65001

 Date: 29/12/2018 02:04:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Flag
-- ----------------------------
DROP TABLE IF EXISTS `Flag`;
CREATE TABLE `Flag` (
  `Flag` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of Flag
-- ----------------------------
BEGIN;
INSERT INTO `Flag` VALUES ('Flag{SQL_MODE_KNOW_ONE_DOWN}');
COMMIT;

-- ----------------------------
-- Table structure for SU_user
-- ----------------------------
DROP TABLE IF EXISTS `SU_user`;
CREATE TABLE `SU_user` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(55) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `money` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of SU_user
-- ----------------------------
BEGIN;
INSERT INTO `SU_user` VALUES (1, 'admin', 'admin', '1000');
COMMIT;

-- ----------------------------
-- Table structure for ips
-- ----------------------------
DROP TABLE IF EXISTS `ips`;
CREATE TABLE `ips` (
  `ip` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;
