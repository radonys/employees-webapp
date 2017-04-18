
-- --------------------------------------------------------

--
-- Table structure for table `absentreq`
--
-- Creation: Mar 30, 2017 at 04:50 PM
--

CREATE TABLE IF NOT EXISTS `absentreq` (
  `emp_no` int(11) DEFAULT NULL,
  `days` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Triggers `absentreq`
--
DELIMITER $$
CREATE TRIGGER `insert_on_Absentapp` AFTER INSERT ON `absentreq` FOR EACH ROW begin insert into absentapp (emp_no,days,approval) values (new.emp_no,new.days,'Pending'); END
$$
DELIMITER ;
