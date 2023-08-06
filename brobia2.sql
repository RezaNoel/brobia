-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2023 at 05:57 PM
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
-- Database: `brobia2`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add city', 7, 'add_city'),
(26, 'Can change city', 7, 'change_city'),
(27, 'Can delete city', 7, 'delete_city'),
(28, 'Can view city', 7, 'view_city'),
(29, 'Can add hotel', 8, 'add_hotel'),
(30, 'Can change hotel', 8, 'change_hotel'),
(31, 'Can delete hotel', 8, 'delete_hotel'),
(32, 'Can view hotel', 8, 'view_hotel'),
(33, 'Can add room', 9, 'add_room'),
(34, 'Can change room', 9, 'change_room'),
(35, 'Can delete room', 9, 'delete_room'),
(36, 'Can view room', 9, 'view_room'),
(37, 'Can add facility', 10, 'add_facility'),
(38, 'Can change facility', 10, 'change_facility'),
(39, 'Can delete facility', 10, 'delete_facility'),
(40, 'Can view facility', 10, 'view_facility'),
(41, 'Can add request', 11, 'add_request'),
(42, 'Can change request', 11, 'change_request'),
(43, 'Can delete request', 11, 'delete_request'),
(44, 'Can view request', 11, 'view_request');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$QMzN8vpxEgPOtlHfGRsDRi$ded+vh4lkMpvQxUJ4TywJyw37wNIlFIrVn4KLa2UZt0=', '2023-07-25 09:13:33.696358', 1, 'reza', '', '', 'reza@reza.com', 1, 1, '2023-07-23 08:03:09.846002');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-07-23 08:04:03.226326', '1', 'مشهد', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-07-23 08:04:07.324775', '2', 'کیش', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-07-23 08:04:21.211187', '1', 'رضوان - مشهد', 1, '[{\"added\": {}}]', 8, 1),
(4, '2023-07-23 08:04:40.436368', '2', 'گوهر - مشهد', 1, '[{\"added\": {}}]', 8, 1),
(5, '2023-07-23 15:49:25.300300', '3', 'قشم', 1, '[{\"added\": {}}]', 7, 1),
(6, '2023-07-23 16:43:44.096035', '3', 'qeshm', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Slug\"]}}]', 7, 1),
(7, '2023-07-23 16:45:31.297083', '3', 'qeshm', 2, '[{\"changed\": {\"fields\": [\"Faname\"]}}]', 7, 1),
(8, '2023-07-23 16:46:35.969106', '2', 'Kish', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Faname\", \"Slug\"]}}]', 7, 1),
(9, '2023-07-23 16:46:42.367625', '3', 'Qeshm', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 7, 1),
(10, '2023-07-23 16:47:08.501012', '1', 'Mashhad', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Faname\", \"Slug\"]}}]', 7, 1),
(11, '2023-07-23 16:47:38.317148', '4', 'Isfahan', 1, '[{\"added\": {}}]', 7, 1),
(12, '2023-07-23 17:20:43.364244', '3', 'جام جم - Kish', 1, '[{\"added\": {}}]', 8, 1),
(13, '2023-07-23 17:34:19.915603', '3', 'jamejam - Kish', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Faname\"]}}]', 8, 1),
(14, '2023-07-23 17:34:52.541385', '2', 'gohar - Mashhad', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Faname\"]}}]', 8, 1),
(15, '2023-07-23 17:35:01.881600', '1', 'rezvan - Mashhad', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Faname\"]}}]', 8, 1),
(16, '2023-07-24 05:51:17.869702', '3', 'jamejam - Kish', 2, '[]', 8, 1),
(17, '2023-07-24 05:51:20.136338', '2', 'gohar - Mashhad', 2, '[]', 8, 1),
(18, '2023-07-24 05:51:21.583914', '1', 'rezvan - Mashhad', 2, '[]', 8, 1),
(19, '2023-07-24 07:04:11.457851', '1', 'rezvan - Mashhad', 2, '[{\"changed\": {\"fields\": [\"About\"]}}]', 8, 1),
(20, '2023-07-24 07:07:40.509403', '1', 'rezvan - Mashhad', 2, '[{\"changed\": {\"fields\": [\"Explanation\"]}}]', 8, 1),
(21, '2023-07-24 07:29:26.562290', '1', 'وای فای', 1, '[{\"added\": {}}]', 10, 1),
(22, '2023-07-24 07:30:02.835620', '2', 'زنگ بیداری', 1, '[{\"added\": {}}]', 10, 1),
(23, '2023-07-24 07:30:24.401951', '3', 'حمام', 1, '[{\"added\": {}}]', 10, 1),
(24, '2023-07-24 07:30:39.117553', '4', 'مرکز تناسب اندام', 1, '[{\"added\": {}}]', 10, 1),
(25, '2023-07-24 07:30:50.008196', '5', 'تلفن', 1, '[{\"added\": {}}]', 10, 1),
(26, '2023-07-24 07:31:00.491230', '6', 'خشک شویی', 1, '[{\"added\": {}}]', 10, 1),
(27, '2023-07-24 07:31:10.498885', '7', 'مینی بار', 1, '[{\"added\": {}}]', 10, 1),
(28, '2023-07-24 07:31:19.894126', '8', 'سشوار', 1, '[{\"added\": {}}]', 10, 1),
(29, '2023-07-24 07:31:30.579878', '9', 'صندلی بلند', 1, '[{\"added\": {}}]', 10, 1),
(30, '2023-07-24 07:31:41.670633', '10', 'رستوران', 1, '[{\"added\": {}}]', 10, 1),
(31, '2023-07-24 07:31:52.777975', '11', 'تهویه مطبوع', 1, '[{\"added\": {}}]', 10, 1),
(32, '2023-07-24 07:32:01.671000', '12', 'دمپایی', 1, '[{\"added\": {}}]', 10, 1),
(33, '2023-07-24 07:39:56.047946', '1', 'rezvan - Mashhad', 2, '[{\"changed\": {\"fields\": [\"Facilities\"]}}]', 8, 1),
(34, '2023-07-24 07:45:37.987800', '2', 'gohar - Mashhad', 2, '[{\"changed\": {\"fields\": [\"Facilities\"]}}]', 8, 1),
(35, '2023-07-24 07:45:50.379538', '1', 'rezvan - Mashhad', 2, '[{\"changed\": {\"fields\": [\"Facilities\"]}}]', 8, 1),
(36, '2023-07-24 07:45:57.220065', '2', 'gohar - Mashhad', 2, '[{\"changed\": {\"fields\": [\"Facilities\"]}}]', 8, 1),
(37, '2023-07-24 07:46:04.209170', '3', 'jamejam - Kish', 2, '[{\"changed\": {\"fields\": [\"Facilities\"]}}]', 8, 1),
(38, '2023-07-24 08:03:52.013151', '2', 'gohar - Mashhad', 2, '[{\"changed\": {\"fields\": [\"\\u0627\\u0645\\u06a9\\u0627\\u0646\\u0627\\u062a\", \"\\u062a\\u0648\\u0636\\u06cc\\u062d\\u0627\\u062a \\u06a9\\u0648\\u062a\\u0627\\u0647\", \"\\u062a\\u0648\\u0636\\u06cc\\u062d\\u0627\\u062a \\u0628\\u0644\\u0646\\u062f\"]}}]', 8, 1),
(39, '2023-07-24 08:30:45.239059', '1', 'سه تخته', 1, '[{\"added\": {}}]', 9, 1),
(40, '2023-07-24 08:32:22.862217', '1', 'سه تخته', 3, '', 9, 1),
(41, '2023-07-24 08:33:57.511513', '2', 'سه تخته', 1, '[{\"added\": {}}]', 9, 1),
(42, '2023-07-24 08:38:11.921342', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0627\\u0645\\u06a9\\u0627\\u0646\\u0627\\u062a\"]}}]', 9, 1),
(43, '2023-07-24 08:43:47.550044', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0627\\u0645\\u06a9\\u0627\\u0646\\u0627\\u062a\"]}}]', 9, 1),
(44, '2023-07-24 08:56:35.693967', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(45, '2023-07-24 09:03:03.151497', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(46, '2023-07-24 09:03:08.164123', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(47, '2023-07-24 09:03:15.058070', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(48, '2023-07-24 09:04:49.214161', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(49, '2023-07-24 09:06:07.842284', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(50, '2023-07-24 09:06:43.962273', '2', 'سه تخته', 2, '[]', 9, 1),
(51, '2023-07-24 09:06:52.564890', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(52, '2023-07-24 09:07:31.453586', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(53, '2023-07-24 09:07:36.869408', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(54, '2023-07-24 09:08:12.531918', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(55, '2023-07-24 09:08:18.246395', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(56, '2023-07-24 09:13:37.940656', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(57, '2023-07-24 09:13:42.959901', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(58, '2023-07-24 09:14:07.158019', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(59, '2023-07-24 09:14:12.118057', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(60, '2023-07-24 09:16:28.344942', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(61, '2023-07-24 09:16:34.235108', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(62, '2023-07-24 09:18:24.783081', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(63, '2023-07-24 09:19:31.257995', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(64, '2023-07-24 09:29:58.572885', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(65, '2023-07-24 09:31:01.870955', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(66, '2023-07-24 09:34:30.410096', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(67, '2023-07-24 09:34:35.386997', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(68, '2023-07-24 09:36:51.268262', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(69, '2023-07-24 09:36:56.316709', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(70, '2023-07-24 09:37:18.168805', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(71, '2023-07-24 09:37:40.726930', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(72, '2023-07-24 09:39:52.677130', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(73, '2023-07-24 09:40:01.421825', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(74, '2023-07-24 09:40:08.455890', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(75, '2023-07-24 09:49:26.732915', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(76, '2023-07-24 09:49:33.973817', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(77, '2023-07-24 09:50:01.862838', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(78, '2023-07-24 09:50:15.732223', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(79, '2023-07-24 09:51:21.990238', '3', 'دو تخته', 1, '[{\"added\": {}}]', 9, 1),
(80, '2023-07-24 16:21:31.153101', '5', 'تبریز', 1, '[{\"added\": {}}]', 7, 1),
(81, '2023-07-24 16:21:38.369383', '6', 'شیراز', 1, '[{\"added\": {}}]', 7, 1),
(82, '2023-07-25 07:09:56.558518', '3', 'دو تخته', 2, '[]', 9, 1),
(83, '2023-07-25 07:14:39.296052', '3', 'دو تخته', 2, '[]', 9, 1),
(84, '2023-07-25 07:14:59.434696', '2', 'سه تخته', 2, '[]', 9, 1),
(85, '2023-07-25 07:54:32.493684', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(86, '2023-07-25 07:58:18.592876', '3', 'دو تخته', 2, '[]', 9, 1),
(87, '2023-07-25 07:58:32.934252', '3', 'دو تخته', 2, '[]', 9, 1),
(88, '2023-07-25 08:20:46.116294', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(89, '2023-07-25 08:22:19.609144', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(90, '2023-07-25 08:22:24.347794', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(91, '2023-07-25 08:29:16.771276', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(92, '2023-07-25 08:33:38.886657', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(93, '2023-07-25 08:35:46.092130', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(94, '2023-07-25 09:02:35.357362', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\"]}}]', 9, 1),
(95, '2023-07-25 09:15:34.345814', '3', 'دو تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\", \"\\u0639\\u06a9\\u0633 \\u0631\\u0632\\u0631\\u0648\"]}}]', 9, 1),
(96, '2023-07-25 09:19:09.323547', '2', 'سه تخته', 2, '[{\"changed\": {\"fields\": [\"\\u0639\\u06a9\\u0633\", \"\\u0639\\u06a9\\u0633 \\u0631\\u0632\\u0631\\u0648\"]}}]', 9, 1),
(97, '2023-07-25 09:26:39.168435', '4', 'چهار تخته', 1, '[{\"added\": {}}]', 9, 1),
(98, '2023-07-25 15:57:47.600209', '4', 'چهار تخته', 2, '[]', 9, 1),
(99, '2023-07-25 15:57:51.888568', '3', 'دو تخته', 2, '[]', 9, 1),
(100, '2023-07-25 15:57:53.890450', '2', 'سه تخته', 2, '[]', 9, 1),
(101, '2023-07-30 09:03:40.166115', '1', 'Request object (1)', 1, '[{\"added\": {}}]', 11, 1),
(102, '2023-07-30 09:05:40.417088', '4', '4takhtrezvan', 2, '[{\"changed\": {\"fields\": [\"\\u0646\\u0627\\u0645\", \"\\u0646\\u0627\\u0645 \\u0646\\u0645\\u0627\\u06cc\\u0634\\u06cc\"]}}]', 9, 1),
(103, '2023-07-30 09:06:03.175531', '2', '3takhtgohar', 2, '[{\"changed\": {\"fields\": [\"\\u0646\\u0627\\u0645\", \"\\u0646\\u0627\\u0645 \\u0646\\u0645\\u0627\\u06cc\\u0634\\u06cc\"]}}]', 9, 1),
(104, '2023-07-30 09:06:45.360841', '3', '2takhtgohar', 2, '[{\"changed\": {\"fields\": [\"\\u0646\\u0627\\u0645\", \"\\u0646\\u0627\\u0645 \\u0646\\u0645\\u0627\\u06cc\\u0634\\u06cc\"]}}]', 9, 1),
(105, '2023-07-30 14:50:40.670120', '13', 'پیشنهاد ویژه', 1, '[{\"added\": {}}]', 10, 1),
(106, '2023-07-30 14:53:39.425721', '1', 'رضوان - مشهد', 2, '[{\"changed\": {\"fields\": [\"\\u0627\\u0645\\u06a9\\u0627\\u0646\\u0627\\u062a\"]}}]', 8, 1),
(107, '2023-07-30 14:59:56.652931', '1', 'رضوان - مشهد', 2, '[{\"changed\": {\"fields\": [\"\\u0627\\u0645\\u06a9\\u0627\\u0646\\u0627\\u062a\"]}}]', 8, 1),
(108, '2023-07-30 15:00:04.829206', '13', 'پیشنهاد ویژه', 3, '', 10, 1),
(109, '2023-07-30 15:00:12.694930', '1', 'رضوان - مشهد', 2, '[{\"changed\": {\"fields\": [\"\\u0622\\u0641\\u0631 \\u0648\\u06cc\\u0698\\u0647\"]}}]', 8, 1),
(110, '2023-07-30 15:28:34.524050', '2', 'گوهر - مشهد', 2, '[{\"changed\": {\"fields\": [\"\\u0622\\u0641\\u0631 \\u0648\\u06cc\\u0698\\u0647\"]}}]', 8, 1),
(111, '2023-07-30 15:28:45.683089', '2', 'گوهر - مشهد', 2, '[{\"changed\": {\"fields\": [\"\\u0622\\u0641\\u0631 \\u0648\\u06cc\\u0698\\u0647\"]}}]', 8, 1),
(112, '2023-07-30 15:30:54.460453', '1', 'Request object (1)', 2, '[{\"changed\": {\"fields\": [\"\\u06a9\\u0627\\u0646\\u0641\\u0631\\u0645\"]}}]', 11, 1),
(113, '2023-07-30 15:30:58.858091', '1', 'Request object (1)', 2, '[{\"changed\": {\"fields\": [\"\\u06a9\\u0627\\u0646\\u0641\\u0631\\u0645\"]}}]', 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'main', 'city'),
(10, 'main', 'facility'),
(8, 'main', 'hotel'),
(11, 'main', 'request'),
(9, 'main', 'room'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-23 08:02:31.244831'),
(2, 'auth', '0001_initial', '2023-07-23 08:02:31.813172'),
(3, 'admin', '0001_initial', '2023-07-23 08:02:31.944816'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-07-23 08:02:31.953792'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-23 08:02:31.960775'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-07-23 08:02:32.024604'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-07-23 08:02:32.078459'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-07-23 08:02:32.100401'),
(9, 'auth', '0004_alter_user_username_opts', '2023-07-23 08:02:32.107382'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-07-23 08:02:32.154256'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-07-23 08:02:32.157248'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-07-23 08:02:32.165228'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-07-23 08:02:32.182182'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-07-23 08:02:32.200185'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-07-23 08:02:32.224122'),
(16, 'auth', '0011_update_proxy_permissions', '2023-07-23 08:02:32.231104'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-07-23 08:02:32.252049'),
(18, 'main', '0001_initial', '2023-07-23 08:02:32.443844'),
(19, 'sessions', '0001_initial', '2023-07-23 08:02:32.482742'),
(20, 'main', '0002_city_slug', '2023-07-23 16:40:11.561989'),
(21, 'main', '0003_city_faname', '2023-07-23 16:45:20.676739'),
(22, 'main', '0004_alter_city_slug', '2023-07-23 16:47:27.069040'),
(23, 'main', '0005_hotel_faname', '2023-07-23 17:33:31.104341'),
(24, 'main', '0006_hotel_slug', '2023-07-24 05:50:28.774901'),
(25, 'main', '0007_hotel_about', '2023-07-24 07:03:36.713900'),
(26, 'main', '0008_rename_about_hotel_description_hotel_explanation', '2023-07-24 07:07:06.618774'),
(27, 'main', '0009_facility_hotel_facilities', '2023-07-24 07:26:26.426148'),
(28, 'main', '0010_facility_faname_alter_facility_name', '2023-07-24 07:28:47.842784'),
(29, 'main', '0011_room_price_alter_city_faname_alter_city_name_and_more', '2023-07-24 08:33:10.793134'),
(30, 'main', '0012_alter_room_price', '2023-07-24 08:33:37.715281'),
(31, 'main', '0013_room_facilities', '2023-07-24 08:37:28.232101'),
(32, 'main', '0014_room_image', '2023-07-24 08:55:40.866009'),
(33, 'main', '0015_alter_room_image', '2023-07-24 09:05:54.296236'),
(34, 'main', '0016_alter_room_image', '2023-07-24 09:06:38.337006'),
(35, 'main', '0017_alter_room_image', '2023-07-24 09:08:06.451552'),
(36, 'main', '0018_alter_room_image', '2023-07-24 09:16:22.525612'),
(37, 'main', '0002_room_slug_alter_room_image', '2023-07-25 07:09:31.840584'),
(38, 'main', '0002_request', '2023-07-30 09:02:56.175110'),
(39, 'main', '0003_room_faname', '2023-07-30 09:04:42.240158'),
(40, 'main', '0004_hotel_special_offer', '2023-07-30 14:59:46.818032'),
(41, 'main', '0005_request_confirm', '2023-07-30 15:30:47.414369');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2ysgl6dziuh04dcajzzz63ne0qcnxv23', '.eJxVjDkOwjAUBe_iGlnxJjuU9Jwh-ptxANlSliri7iRSCmjfzLxNDbAuZVhnmYaR1VUZdfndEOgl9QD8hPpomlpdphH1oeiTzvreWN630_07KDCXvSbP0QXKSNZibxij911AAfESWGLOxAkQHFvjdtYLIXUmeYyUkkX1-QIWkzkY:1qNyAF:kiDoRuQGydFKuuDKmSiyY2ME84Rrj9eKNBr3j9YHuck', '2023-08-07 16:12:03.873483'),
('nd6wtu4cy8ok8a76pnonoy92gb5dvgr4', '.eJxVjDkOwjAUBe_iGlnxJjuU9Jwh-ptxANlSliri7iRSCmjfzLxNDbAuZVhnmYaR1VUZdfndEOgl9QD8hPpomlpdphH1oeiTzvreWN630_07KDCXvSbP0QXKSNZibxij911AAfESWGLOxAkQHFvjdtYLIXUmeYyUkkX1-QIWkzkY:1qOE6n:JocI1wn-4xDjicc_TFmG7dIxxlzC3lBGYNW1JZ0GiN0', '2023-08-08 09:13:33.698457'),
('zm2hkrup297j2xjb5j0366xdqigkv6aq', '.eJxVjDkOwjAUBe_iGlnxJjuU9Jwh-ptxANlSliri7iRSCmjfzLxNDbAuZVhnmYaR1VUZdfndEOgl9QD8hPpomlpdphH1oeiTzvreWN630_07KDCXvSbP0QXKSNZibxij911AAfESWGLOxAkQHFvjdtYLIXUmeYyUkkX1-QIWkzkY:1qNU3d:2Yul0fmVvvybPBeGKcXDWNK1q0sz-aK8JtNSCf6JEQI', '2023-08-06 08:03:13.976698');

-- --------------------------------------------------------

--
-- Table structure for table `main_city`
--

CREATE TABLE `main_city` (
  `id` bigint(20) NOT NULL,
  `name` varchar(75) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `faname` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_city`
--

INSERT INTO `main_city` (`id`, `name`, `slug`, `faname`) VALUES
(1, 'Mashhad', 'mashhad', 'مشهد'),
(2, 'Kish', 'kish', 'کیش'),
(3, 'Qeshm', 'qeshm', 'قشم'),
(4, 'Isfahan', 'isfahan', 'اصفهان'),
(5, 'tabriz', 'tabriz', 'تبریز'),
(6, 'shiraz', 'shiraz', 'شیراز');

-- --------------------------------------------------------

--
-- Table structure for table `main_facility`
--

CREATE TABLE `main_facility` (
  `id` bigint(20) NOT NULL,
  `name` varchar(75) NOT NULL,
  `faname` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_facility`
--

INSERT INTO `main_facility` (`id`, `name`, `faname`) VALUES
(1, 'wifi-signal', 'وای فای'),
(2, 'alarm', 'زنگ بیداری'),
(3, 'bathrobe', 'حمام'),
(4, 'weightlifting', 'مرکز تناسب اندام'),
(5, 'phone-call', 'تلفن'),
(6, 'folded-towel', 'خشک شویی'),
(7, 'wine-glass', 'مینی بار'),
(8, 'hair-dryer', 'سشوار'),
(9, 'desk-chair', 'صندلی بلند'),
(10, 'hamburger', 'رستوران'),
(11, 'air-conditioner', 'تهویه مطبوع'),
(12, 'slippers', 'دمپایی');

-- --------------------------------------------------------

--
-- Table structure for table `main_hotel`
--

CREATE TABLE `main_hotel` (
  `id` bigint(20) NOT NULL,
  `name` varchar(75) NOT NULL,
  `address` varchar(75) NOT NULL,
  `starts` int(11) NOT NULL,
  `city_id` bigint(20) NOT NULL,
  `faname` varchar(75) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `explanation` longtext NOT NULL,
  `special_offer` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_hotel`
--

INSERT INTO `main_hotel` (`id`, `name`, `address`, `starts`, `city_id`, `faname`, `slug`, `description`, `explanation`, `special_offer`) VALUES
(1, 'rezvan', 'مشهد - خیابان شیرازی - هتل رضوان', 4, 1, 'رضوان', 'rezvan', 'این هتل بسیار نزدیک به حرم امام رضا (ع) است', 'این هتل بسیار زیبا و تمیز است و کادری مودب و مناسب دارد', 1),
(2, 'gohar', 'مشهد - امام رضا 5 - هتل گوهر', 3, 1, 'گوهر', 'gohar', 'این هتل گوهر است', 'این توضبح بلند است', 0),
(3, 'jamejam', 'کیش - بلوار دریا - هتل جام جم', 3, 2, 'جام جم', 'jamejam', '', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `main_hotel_facilities`
--

CREATE TABLE `main_hotel_facilities` (
  `id` bigint(20) NOT NULL,
  `hotel_id` bigint(20) NOT NULL,
  `facility_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_hotel_facilities`
--

INSERT INTO `main_hotel_facilities` (`id`, `hotel_id`, `facility_id`) VALUES
(1, 1, 2),
(7, 1, 8),
(24, 2, 1),
(20, 2, 3),
(21, 2, 5),
(22, 3, 1),
(23, 3, 10);

-- --------------------------------------------------------

--
-- Table structure for table `main_request`
--

CREATE TABLE `main_request` (
  `id` bigint(20) NOT NULL,
  `enter` varchar(20) NOT NULL,
  `exit` varchar(20) NOT NULL,
  `room_count` int(11) NOT NULL,
  `passenger_count` int(11) NOT NULL,
  `room_id` bigint(20) NOT NULL,
  `confirm` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_request`
--

INSERT INTO `main_request` (`id`, `enter`, `exit`, `room_count`, `passenger_count`, `room_id`, `confirm`) VALUES
(1, '1402/05/10', '1402/05/13', 1, 3, 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `main_room`
--

CREATE TABLE `main_room` (
  `id` bigint(20) NOT NULL,
  `name` varchar(75) NOT NULL,
  `bed` int(11) NOT NULL,
  `hotel_id` bigint(20) NOT NULL,
  `price` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `image_booking` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `faname` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_room`
--

INSERT INTO `main_room` (`id`, `name`, `bed`, `hotel_id`, `price`, `image`, `image_booking`, `slug`, `faname`) VALUES
(2, '3takhtgohar', 3, 2, 1300000, 'static/img/200x154/rezvan.jpeg', 'static/img/240x160/rezvan.jpeg', '3takhtgohar-gohar', 'سه تخته'),
(3, '2takhtgohar', 2, 2, 820000, 'static/img/200x154/img1_wUgMrjN.jpg', 'static/img/240x160/img1_2XeKoqg.jpg', '2takhtgohar-gohar', 'دو تخته'),
(4, '4takhtrezvan', 4, 1, 1200000, 'static/img/200x154/rezvan_B0MT0Nv.jpeg', 'static/img/240x160/rezvan_bd0r2LU.jpeg', '4takhtrezvan-rezvan', 'چهار تخته');

-- --------------------------------------------------------

--
-- Table structure for table `main_room_facilities`
--

CREATE TABLE `main_room_facilities` (
  `id` bigint(20) NOT NULL,
  `room_id` bigint(20) NOT NULL,
  `facility_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_room_facilities`
--

INSERT INTO `main_room_facilities` (`id`, `room_id`, `facility_id`) VALUES
(1, 2, 1),
(2, 2, 3),
(3, 2, 11),
(4, 2, 12),
(5, 3, 3),
(6, 4, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `main_city`
--
ALTER TABLE `main_city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_city_slug_f78d04eb` (`slug`);

--
-- Indexes for table `main_facility`
--
ALTER TABLE `main_facility`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_hotel`
--
ALTER TABLE `main_hotel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_hotel_city_id_e7e16958_fk_main_city_id` (`city_id`),
  ADD KEY `main_hotel_slug_fef10b88` (`slug`);

--
-- Indexes for table `main_hotel_facilities`
--
ALTER TABLE `main_hotel_facilities`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_hotel_facilities_hotel_id_facility_id_89ad3334_uniq` (`hotel_id`,`facility_id`),
  ADD KEY `main_hotel_facilities_facility_id_e47497bf_fk_main_facility_id` (`facility_id`);

--
-- Indexes for table `main_request`
--
ALTER TABLE `main_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_request_room_id_fbe54c32_fk_main_room_id` (`room_id`);

--
-- Indexes for table `main_room`
--
ALTER TABLE `main_room`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_room_hotel_id_4025f4eb_fk_main_hotel_id` (`hotel_id`),
  ADD KEY `main_room_slug_e14dd176` (`slug`);

--
-- Indexes for table `main_room_facilities`
--
ALTER TABLE `main_room_facilities`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_room_facilities_room_id_facility_id_4a41a5e5_uniq` (`room_id`,`facility_id`),
  ADD KEY `main_room_facilities_facility_id_c2ad2c06_fk_main_facility_id` (`facility_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=114;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `main_city`
--
ALTER TABLE `main_city`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `main_facility`
--
ALTER TABLE `main_facility`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `main_hotel`
--
ALTER TABLE `main_hotel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `main_hotel_facilities`
--
ALTER TABLE `main_hotel_facilities`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `main_request`
--
ALTER TABLE `main_request`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `main_room`
--
ALTER TABLE `main_room`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `main_room_facilities`
--
ALTER TABLE `main_room_facilities`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `main_hotel`
--
ALTER TABLE `main_hotel`
  ADD CONSTRAINT `main_hotel_city_id_e7e16958_fk_main_city_id` FOREIGN KEY (`city_id`) REFERENCES `main_city` (`id`);

--
-- Constraints for table `main_hotel_facilities`
--
ALTER TABLE `main_hotel_facilities`
  ADD CONSTRAINT `main_hotel_facilities_facility_id_e47497bf_fk_main_facility_id` FOREIGN KEY (`facility_id`) REFERENCES `main_facility` (`id`),
  ADD CONSTRAINT `main_hotel_facilities_hotel_id_6cdc6081_fk_main_hotel_id` FOREIGN KEY (`hotel_id`) REFERENCES `main_hotel` (`id`);

--
-- Constraints for table `main_request`
--
ALTER TABLE `main_request`
  ADD CONSTRAINT `main_request_room_id_fbe54c32_fk_main_room_id` FOREIGN KEY (`room_id`) REFERENCES `main_room` (`id`);

--
-- Constraints for table `main_room`
--
ALTER TABLE `main_room`
  ADD CONSTRAINT `main_room_hotel_id_4025f4eb_fk_main_hotel_id` FOREIGN KEY (`hotel_id`) REFERENCES `main_hotel` (`id`);

--
-- Constraints for table `main_room_facilities`
--
ALTER TABLE `main_room_facilities`
  ADD CONSTRAINT `main_room_facilities_facility_id_c2ad2c06_fk_main_facility_id` FOREIGN KEY (`facility_id`) REFERENCES `main_facility` (`id`),
  ADD CONSTRAINT `main_room_facilities_room_id_9b5b3a47_fk_main_room_id` FOREIGN KEY (`room_id`) REFERENCES `main_room` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
