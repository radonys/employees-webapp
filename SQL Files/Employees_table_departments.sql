
-- --------------------------------------------------------

--
-- Table structure for table `departments`
--
-- Creation: Mar 22, 2017 at 11:17 AM
--

CREATE TABLE IF NOT EXISTS `departments` (
  `dept_no` char(4) NOT NULL,
  `dept_name` varchar(40) NOT NULL,
  PRIMARY KEY (`dept_no`),
  UNIQUE KEY `dept_name` (`dept_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`dept_no`, `dept_name`) VALUES
('d009', 'Customer Service'),
('d005', 'Development'),
('d002', 'Finance'),
('d003', 'Human Resources'),
('d001', 'Marketing'),
('d004', 'Production'),
('d006', 'Quality Management'),
('d008', 'Research'),
('d007', 'Sales');
