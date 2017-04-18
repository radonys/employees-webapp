
-- --------------------------------------------------------

--
-- Table structure for table `applicants`
--
-- Creation: Mar 26, 2017 at 05:28 AM
--

CREATE TABLE IF NOT EXISTS `applicants` (
  `emp_no` int(20) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `gender` enum('M','F') DEFAULT NULL,
  `dept_no` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
