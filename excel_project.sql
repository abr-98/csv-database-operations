-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 26, 2018 at 07:47 AM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `excel_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `STOCK_DETAILS`
--

CREATE TABLE `STOCK_DETAILS` (
  `Index` int(4) NOT NULL,
  `Date_update` text NOT NULL,
  `Scrip` text NOT NULL,
  `sector` text NOT NULL,
  `ACTION` text NOT NULL,
  `status` text NOT NULL,
  `EntryPrice` text NOT NULL,
  `EntryDate` text NOT NULL,
  `StopLoss` text NOT NULL,
  `ExitPrice` text NOT NULL,
  `ExitDate` text NOT NULL,
  `LTP` text NOT NULL,
  `LastTradingDay` text NOT NULL,
  `Return` text NOT NULL,
  `Group` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `STOCK_DETAILS`
--
ALTER TABLE `STOCK_DETAILS`
  ADD PRIMARY KEY (`Index`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `STOCK_DETAILS`
--
ALTER TABLE `STOCK_DETAILS`
  MODIFY `Index` int(4) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
