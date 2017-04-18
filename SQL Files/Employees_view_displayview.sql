
-- --------------------------------------------------------

--
-- Structure for view `displayview`
--
DROP TABLE IF EXISTS `displayview`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `employees`.`displayview`  AS  (select `employees`.`applicants`.`emp_no` AS `emp_no`,`employees`.`applicants`.`birth_date` AS `birth_date`,`employees`.`applicants`.`first_name` AS `first_name`,`employees`.`applicants`.`last_name` AS `last_name`,`employees`.`applicants`.`gender` AS `gender`,`employees`.`applicants`.`hire_date` AS `hire_date`,`employees`.`applicants`.`dept_no` AS `dept_no` from `employees`.`applicants`) ;
