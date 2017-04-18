
-- --------------------------------------------------------

--
-- Table structure for table `absentapp`
--
-- Creation: Mar 30, 2017 at 07:27 PM
--

CREATE TABLE IF NOT EXISTS `absentapp` (
  `emp_no` int(11) DEFAULT NULL,
  `days` int(3) DEFAULT NULL,
  `approval` enum('Yes','No','Pending') DEFAULT NULL,
  `dated` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `absentapp`
--

INSERT INTO `absentapp` (`emp_no`, `days`, `approval`, `dated`) VALUES
(499992, 3, 'No', '2017-04-05 12:15:35'),
(499992, 4, 'Yes', '2017-04-06 05:53:38');
