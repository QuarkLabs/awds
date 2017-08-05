-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2017 at 03:39 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sis`
--

-- --------------------------------------------------------

--
-- Table structure for table `crop`
--

CREATE TABLE `crop` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `crop`
--

INSERT INTO `crop` (`id`, `name`) VALUES
(1000, 'Paddy'),
(1001, 'Tomato');

-- --------------------------------------------------------

--
-- Table structure for table `crop_condition`
--

CREATE TABLE `crop_condition` (
  `id` int(11) NOT NULL,
  `farmer_has_crop_farmer_id` int(11) NOT NULL,
  `farmer_has_crop_crop_id` int(11) NOT NULL,
  `temperature` double NOT NULL,
  `shower` double NOT NULL,
  `moisture` double NOT NULL,
  `min_water` double NOT NULL,
  `rec_water` double NOT NULL,
  `calculated_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `crop_condition`
--

INSERT INTO `crop_condition` (`id`, `farmer_has_crop_farmer_id`, `farmer_has_crop_crop_id`, `temperature`, `shower`, `moisture`, `min_water`, `rec_water`, `calculated_date`) VALUES
(1, 100, 1000, 26, 100, 50, 10, 38, '2017-05-07 00:00:00'),
(2, 100, 1001, 38, 83, 50, 12, 18, '2017-05-10 00:00:00'),
(3, 100, 1000, 27, 83, 50, 10, 40, '2017-05-08 00:00:00'),
(4, 100, 1001, 38, 93, 50, 15, 20, '2017-05-11 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `farmer`
--

CREATE TABLE `farmer` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `farmer`
--

INSERT INTO `farmer` (`id`, `name`) VALUES
(100, 'Sumanapala Goyya');

-- --------------------------------------------------------

--
-- Table structure for table `farmer_has_crop`
--

CREATE TABLE `farmer_has_crop` (
  `farmer_id` int(11) NOT NULL,
  `crop_id` int(11) NOT NULL,
  `start_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `farmer_has_crop`
--

INSERT INTO `farmer_has_crop` (`farmer_id`, `crop_id`, `start_date`) VALUES
(100, 1000, '2017-01-01'),
(100, 1001, '2017-02-01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `crop`
--
ALTER TABLE `crop`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `crop_condition`
--
ALTER TABLE `crop_condition`
  ADD PRIMARY KEY (`id`,`calculated_date`),
  ADD KEY `fk_crop_condition_farmer_has_crop1_idx` (`farmer_has_crop_farmer_id`,`farmer_has_crop_crop_id`);

--
-- Indexes for table `farmer`
--
ALTER TABLE `farmer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `farmer_has_crop`
--
ALTER TABLE `farmer_has_crop`
  ADD PRIMARY KEY (`farmer_id`,`crop_id`),
  ADD KEY `fk_farmer_has_crop_crop1_idx` (`crop_id`),
  ADD KEY `fk_farmer_has_crop_farmer_idx` (`farmer_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `farmer`
--
ALTER TABLE `farmer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `crop_condition`
--
ALTER TABLE `crop_condition`
  ADD CONSTRAINT `fk_crop_condition_farmer_has_crop1` FOREIGN KEY (`farmer_has_crop_farmer_id`,`farmer_has_crop_crop_id`) REFERENCES `farmer_has_crop` (`farmer_id`, `crop_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `farmer_has_crop`
--
ALTER TABLE `farmer_has_crop`
  ADD CONSTRAINT `fk_farmer_has_crop_crop1` FOREIGN KEY (`crop_id`) REFERENCES `crop` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_farmer_has_crop_farmer` FOREIGN KEY (`farmer_id`) REFERENCES `farmer` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
