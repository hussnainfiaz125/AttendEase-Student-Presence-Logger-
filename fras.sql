-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: May 31, 2024 at 10:02 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fras`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(11) NOT NULL,
  `Attendance_Id` varchar(255) NOT NULL,
  `Roll` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Dep` varchar(255) NOT NULL,
  `Time` varchar(255) NOT NULL,
  `Date` varchar(255) NOT NULL,
  `Attendance` varchar(255) NOT NULL,
  `teacher_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`id`, `Attendance_Id`, `Roll`, `Name`, `Dep`, `Time`, `Date`, `Attendance`, `teacher_id`) VALUES
(331, '2', '2', 'Hussnain', 'Computer Science', '22:55:01', '2024-05-28', 'Present', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(332, '5', '2', 'Abdullah', 'Computer Science', '22:55:04', '2024-05-28', 'Present', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(333, '7', '7', 'Ahmad', 'Computer Science', '22:55:07', '2024-05-28', 'Present', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(334, '3', '3', 'jerry', 'Computer Science', '22:56:17', '2024-05-28', 'Absent', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(335, '6', '6', 'uzzy', 'Computer Science', '22:56:17', '2024-05-28', 'Absent', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(347, '2', '2', 'Hussnain', 'Computer Science', '00:39:20', '2024-06-01', 'Absent', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(348, '5', '2', 'Abdullah', 'Computer Science', '00:39:20', '2024-06-01', 'Absent', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(349, '3', '3', 'jerry', 'Computer Science', '00:39:20', '2024-06-01', 'Absent', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(350, '6', '6', 'uzzy', 'Computer Science', '00:39:20', '2024-06-01', 'Absent', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(351, '7', '7', 'Ahmad', 'Computer Science', '00:39:20', '2024-06-01', 'Absent', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL DEFAULT '',
  `lname` varchar(255) NOT NULL DEFAULT '',
  `contact` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `securityQ` varchar(255) NOT NULL,
  `securityA` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `teacher_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `fname`, `lname`, `contact`, `email`, `securityQ`, `securityA`, `password`, `teacher_id`) VALUES
(1, 'irfan', 'ch', '0465465', 'irfan@123', 'Your Birth Place ', 'hasilpur', '1234', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(2, 'ali', 'ch', '35485456', 'ali@123', 'Your Birth Place ', 'aklk', '1234', 'acb4df53-77a3-404f-9314-ecb30173744a');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `Dep` varchar(255) NOT NULL,
  `Course` varchar(255) NOT NULL,
  `Year` varchar(255) NOT NULL,
  `Semester` varchar(255) NOT NULL,
  `Student_id` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Division` varchar(255) NOT NULL,
  `Roll` varchar(255) NOT NULL,
  `Gender` varchar(255) NOT NULL,
  `Dob` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Teacher` varchar(255) NOT NULL,
  `PhotoSample` varchar(50) NOT NULL,
  `teacher_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `Dep`, `Course`, `Year`, `Semester`, `Student_id`, `Name`, `Division`, `Roll`, `Gender`, `Dob`, `Email`, `Phone`, `Address`, `Teacher`, `PhotoSample`, `teacher_id`) VALUES
(20, 'Computer Science', 'CSI-321-ItA', '2020-2024', '1st', '2', 'Hussnain', 'A', '2', 'Male', '', '', '', '', '', '1', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(22, 'Computer Science', 'CSI-321-ItA', '2020-2024', '1st', '5', 'Abdullah', 'A', '2', 'Male', '', '', '', '', '', '1', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(23, 'Computer Science', 'CSI-321-ItA', '2020-2024', '1st', '3', 'jerry', 'A', '3', 'Male', '', '', '', '', '', '0', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(24, 'Computer Science', 'ECO-408-ItPE', '2020-2024', '2nd', '6', 'uzzy', 'A', '6', 'Male', '', '', '', '', '', '', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f'),
(27, 'Computer Science', 'CSI-418-WC', '2020-2024', '4th', '7', 'Ahmad', 'A', '7', 'Male', '29-12-2001', 'Ahmad@gmail.com', '', 'Hasilpur', 'Abdullah', '0', '78cd445b-aa23-4d87-9aea-1c11a7e1cb0f');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=352;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
