-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 21, 2023 at 07:04 PM
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
-- Database: `brobia`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user`
--

CREATE TABLE `accounts_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `nid` varchar(10) NOT NULL,
  `birthdate` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_user`
--

INSERT INTO `accounts_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`, `nid`, `birthdate`) VALUES
(1, 'pbkdf2_sha256$600000$phdfTGH1hvd7Olt9Aj0vQF$19Vh/+cJFSClyrT2F4o3+N3O4eU5CATkx4uqbjDXpFA=', '2023-10-19 15:33:25.351631', 0, '09129471382', 'رضا', 'توانگر', '', 0, 1, '2023-08-26 15:35:10.544361', '09129471382', '', ''),
(2, 'pbkdf2_sha256$600000$xXEpsrC5ChKCkn48jh2GV6$X4f+Jfg0WUuGPzqJQqPxJ1khnJkjs0KFDmydwzkCmbc=', '2023-10-20 17:57:19.515951', 1, 'reza', '', '', 'reza@reza.com', 1, 1, '2023-09-01 02:53:57.924803', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_groups`
--

CREATE TABLE `accounts_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_hotel_likes`
--

CREATE TABLE `accounts_user_hotel_likes` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `hotel_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_reserves`
--

CREATE TABLE `accounts_user_reserves` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `request_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_user_permissions`
--

CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add شهر', 6, 'add_city'),
(22, 'Can change شهر', 6, 'change_city'),
(23, 'Can delete شهر', 6, 'delete_city'),
(24, 'Can view شهر', 6, 'view_city'),
(25, 'Can add اماکانات', 7, 'add_facility'),
(26, 'Can change اماکانات', 7, 'change_facility'),
(27, 'Can delete اماکانات', 7, 'delete_facility'),
(28, 'Can view اماکانات', 7, 'view_facility'),
(29, 'Can add هتل', 8, 'add_hotel'),
(30, 'Can change هتل', 8, 'change_hotel'),
(31, 'Can delete هتل', 8, 'delete_hotel'),
(32, 'Can view هتل', 8, 'view_hotel'),
(33, 'Can add اتاق', 9, 'add_room'),
(34, 'Can change اتاق', 9, 'change_room'),
(35, 'Can delete اتاق', 9, 'delete_room'),
(36, 'Can view اتاق', 9, 'view_room'),
(37, 'Can add درخواست', 10, 'add_request'),
(38, 'Can change درخواست', 10, 'change_request'),
(39, 'Can delete درخواست', 10, 'delete_request'),
(40, 'Can view درخواست', 10, 'view_request'),
(41, 'Can add مسافران', 11, 'add_passenger'),
(42, 'Can change مسافران', 11, 'change_passenger'),
(43, 'Can delete مسافران', 11, 'delete_passenger'),
(44, 'Can view مسافران', 11, 'view_passenger'),
(45, 'Can add اطلاعات کاربر', 12, 'add_user'),
(46, 'Can change اطلاعات کاربر', 12, 'change_user'),
(47, 'Can delete اطلاعات کاربر', 12, 'delete_user'),
(48, 'Can view اطلاعات کاربر', 12, 'view_user');

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
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-09-01 06:28:25.085704', '22', 'xzmnMvbajM', 2, '[{\"changed\": {\"fields\": [\"\\u0648\\u0636\\u0639\\u06cc\\u062a\"]}}]', 10, 2),
(2, '2023-09-04 10:04:59.715842', '3', 'جام جم - کیش', 2, '[{\"changed\": {\"fields\": [\"\\u0644\\u06cc\\u0646\\u06a9\"]}}]', 8, 2),
(3, '2023-09-04 10:05:07.741383', '3', 'جام جم - کیش', 2, '[{\"changed\": {\"fields\": [\"\\u0644\\u06cc\\u0646\\u06a9\"]}}]', 8, 2),
(4, '2023-09-06 07:54:56.372636', '23', 'sxd28scPfZ', 2, '[{\"changed\": {\"fields\": [\"\\u0648\\u0636\\u0639\\u06cc\\u062a\"]}}]', 10, 2),
(5, '2023-09-06 08:00:07.610579', '23', 'sxd28scPfZ', 2, '[{\"changed\": {\"fields\": [\"\\u0648\\u0636\\u0639\\u06cc\\u062a \\u0631\\u0632\\u0631\\u0648\"]}}]', 10, 2),
(6, '2023-09-06 08:00:25.729480', '23', 'sxd28scPfZ', 2, '[{\"changed\": {\"fields\": [\"\\u0632\\u0645\\u0627\\u0646 \\u0631\\u0632\\u0631\\u0648\"]}}]', 10, 2),
(7, '2023-09-07 07:20:02.462049', '4', 'هما - مشهد', 1, '[{\"added\": {}}]', 8, 2),
(8, '2023-09-07 07:21:00.074306', '4', 'هما - مشهد', 2, '[{\"changed\": {\"fields\": [\"\\u0622\\u062f\\u0631\\u0633\"]}}]', 8, 2),
(9, '2023-09-10 06:36:05.383743', '24', 'Ncd9fMBdSt', 2, '[{\"changed\": {\"fields\": [\"\\u0648\\u0636\\u0639\\u06cc\\u062a\"]}}]', 10, 2),
(10, '2023-09-10 06:37:08.754601', '24', 'Ncd9fMBdSt', 2, '[{\"changed\": {\"fields\": [\"\\u0648\\u0636\\u0639\\u06cc\\u062a \\u0631\\u0632\\u0631\\u0648\"]}}]', 10, 2),
(11, '2023-10-19 16:10:45.941624', '5', 'تبریز', 2, '[{\"changed\": {\"fields\": [\"\\u0646\\u0627\\u0645 \\u0627\\u0635\\u0644\\u06cc\"]}}]', 6, 2),
(12, '2023-10-19 16:10:49.626275', '6', 'شیراز', 2, '[{\"changed\": {\"fields\": [\"\\u0646\\u0627\\u0645 \\u0627\\u0635\\u0644\\u06cc\"]}}]', 6, 2);

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
(12, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'main', 'city'),
(7, 'main', 'facility'),
(8, 'main', 'hotel'),
(11, 'main', 'passenger'),
(10, 'main', 'request'),
(9, 'main', 'room'),
(5, 'sessions', 'session');

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
(1, 'main', '0001_initial', '2023-08-26 15:32:16.517660'),
(2, 'main', '0002_request_reserve_status', '2023-08-26 15:32:16.563540'),
(3, 'main', '0003_request_needs_passenger', '2023-08-26 15:32:16.769985'),
(4, 'main', '0004_request_reserve_time', '2023-08-26 15:32:16.802896'),
(5, 'main', '0005_alter_passenger_nid_alter_passenger_phone', '2023-08-26 15:32:16.903639'),
(6, 'contenttypes', '0001_initial', '2023-08-26 15:32:16.944518'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-08-26 15:32:17.098344'),
(8, 'auth', '0001_initial', '2023-08-26 15:32:17.346681'),
(9, 'auth', '0002_alter_permission_name_max_length', '2023-08-26 15:32:17.400536'),
(10, 'auth', '0003_alter_user_email_max_length', '2023-08-26 15:32:17.409513'),
(11, 'auth', '0004_alter_user_username_opts', '2023-08-26 15:32:17.415497'),
(12, 'auth', '0005_alter_user_last_login_null', '2023-08-26 15:32:17.420484'),
(13, 'auth', '0006_require_contenttypes_0002', '2023-08-26 15:32:17.422476'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2023-08-26 15:32:17.428462'),
(15, 'auth', '0008_alter_user_username_max_length', '2023-08-26 15:32:17.433450'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2023-08-26 15:32:17.439433'),
(17, 'auth', '0010_alter_group_name_max_length', '2023-08-26 15:32:17.459380'),
(18, 'auth', '0011_update_proxy_permissions', '2023-08-26 15:32:17.470350'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2023-08-26 15:32:17.477331'),
(20, 'accounts', '0001_initial', '2023-08-26 15:32:17.867974'),
(21, 'accounts', '0002_alter_user_birthdate_alter_user_nid_alter_user_phone', '2023-08-26 15:32:17.893905'),
(22, 'admin', '0001_initial', '2023-08-26 15:32:18.014583'),
(23, 'admin', '0002_logentry_remove_auto_add', '2023-08-26 15:32:18.022562'),
(24, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-26 15:32:18.029542'),
(25, 'sessions', '0001_initial', '2023-08-26 15:32:18.143173'),
(26, 'main', '0006_hotel_likes_hotel_online_reserve', '2023-10-20 17:57:13.482519'),
(27, 'accounts', '0003_user_hotel_likes', '2023-10-20 17:57:13.648893');

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
('1k60bkd8o7jn72v2s2obqk0dvmyopg15', '.eJxVjEEOwiAQAP_C2ZAWdgU8eu8byMKuUjU0Ke3J-HdD0oNeZybzVpH2rcS9yRpnVhdl1OmXJcpPqV3wg-p90Xmp2zon3RN92KanheV1Pdq_QaFW-hZsTkYo3NAICApbFhgROQFaB8MZUCQ44x0Q5EGEMNjReY_Oep_V5wvjzTda:1qtVbY:LLIB-WPquh47ldD5cHto9HmGfGzdKs_o_d_QA59ysJY', '2023-11-02 16:10:36.726326'),
('8xs4l9bpu5a9n7jxfju8jfptceznqiah', '.eJxVjEEOwiAQAP_C2ZAWdgU8eu8byMKuUjU0Ke3J-HdD0oNeZybzVpH2rcS9yRpnVhdl1OmXJcpPqV3wg-p90Xmp2zon3RN92KanheV1Pdq_QaFW-hZsTkYo3NAICApbFhgROQFaB8MZUCQ44x0Q5EGEMNjReY_Oep_V5wvjzTda:1qttkN:pfR0bXtLjkFzaPx0XDSKPloPw_AXsEX7rWFfbzodNa4', '2023-11-03 17:57:19.517969'),
('9m3n6ld3ekgm3cznt6lbfefavrt93g7f', 'e30:1qd6L7:9DuAf-Y63LnOtMr8ajHtnE8vEsbrpQH9MVuNCNffT-0', '2023-09-18 09:57:49.646401'),
('ee064ttt890vll7p2sf7sisbcgtrqf7e', '.eJxVjEEOwiAQRe_C2hCgQwZcuvcMZIYhUjWQlHZlvLs26UK3_733XyrRtta0jbKkWdRZWXX63Zjyo7QdyJ3arevc27rMrHdFH3Toa5fyvBzu30GlUb-18RmRwRQDLqILIGw9ZRsxIDmwk4RsIgA4n4thBCE2ED1OyOKgqPcHtRY22A:1qtV1Z:nOp5z8EDIAArjvj3MIjYD4-lVfD57Qe4mp9sXxC54hM', '2023-11-02 15:33:25.356617'),
('gclza5s51q00anlivbps5ryju6zf2gy9', '.eJxVjEEOwiAQRe_C2hCgQwZcuvcMZIYhUjWQlHZlvLs26UK3_733XyrRtta0jbKkWdRZWXX63Zjyo7QdyJ3arevc27rMrHdFH3Toa5fyvBzu30GlUb-18RmRwRQDLqILIGw9ZRsxIDmwk4RsIgA4n4thBCE2ED1OyOKgqPcHtRY22A:1qfE5h:R_7cnT6H-KpTdVgCdE-PIYNusKvLKr_j5NnQr4Qwuog', '2023-09-24 06:38:41.611525'),
('jhkzfu0kvsiouz8sjfxngxnynhp521da', '.eJxVjEEOwiAQAP_C2ZAWdgU8eu8byMKuUjU0Ke3J-HdD0oNeZybzVpH2rcS9yRpnVhdl1OmXJcpPqV3wg-p90Xmp2zon3RN92KanheV1Pdq_QaFW-hZsTkYo3NAICApbFhgROQFaB8MZUCQ44x0Q5EGEMNjReY_Oep_V5wvjzTda:1qd6QJ:igpgbSuvJixTKsNiwS3FAmazZkGuBuOD5P9SvQDqvCo', '2023-09-18 10:03:11.976963');

-- --------------------------------------------------------

--
-- Table structure for table `main_city`
--

CREATE TABLE `main_city` (
  `id` bigint(20) NOT NULL,
  `name` varchar(75) NOT NULL,
  `faname` varchar(75) NOT NULL,
  `slug` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_city`
--

INSERT INTO `main_city` (`id`, `name`, `faname`, `slug`) VALUES
(1, 'Mashhad', 'مشهد', 'mashhad'),
(2, 'Kish', 'کیش', 'kish'),
(3, 'Qeshm', 'قشم', 'qeshm'),
(4, 'Isfahan', 'اصفهان', 'isfahan'),
(5, 'Tabriz', 'تبریز', 'tabriz'),
(6, 'Shiraz', 'شیراز', 'shiraz');

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
  `faname` varchar(75) NOT NULL,
  `address` varchar(75) NOT NULL,
  `starts` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `explanation` longtext NOT NULL,
  `slug` varchar(50) NOT NULL,
  `special_offer` tinyint(1) NOT NULL,
  `city_id` bigint(20) NOT NULL,
  `likes` int(11) NOT NULL,
  `online_reserve` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_hotel`
--

INSERT INTO `main_hotel` (`id`, `name`, `faname`, `address`, `starts`, `description`, `explanation`, `slug`, `special_offer`, `city_id`, `likes`, `online_reserve`) VALUES
(1, 'rezvan', 'رضوان', 'مشهد - خیابان شیرازی - هتل رضوان', 4, 'این هتل بسیار نزدیک به حرم امام رضا (ع) است', 'این هتل بسیار زیبا و تمیز است و کادری مودب و مناسب دارد', 'rezvan', 1, 1, 0, 0),
(2, 'gohar', 'گوهر', 'مشهد - امام رضا 5 - هتل گوهر', 3, 'این هتل گوهر است', 'این توضبح بلند است', 'gohar', 0, 1, 0, 0),
(3, 'jamejam', 'جام جم', 'کیش - بلوار دریا - هتل جام جم', 3, '', '', 'jamejam', 0, 2, 0, 0),
(4, 'homa', 'هما', 'مشهد - میدان احمد آباد-نبش کلاهدوز-هتل هما1 (هایت سابق)', 5, 'صبحانه بوفه کامل - اینترنت بی سیم - آب معدنی و چای در اتاق- سرویس رفت به حرم رضوی (یک ساعت) قبل از نماز-زمین تنیس- تاکسی سرویس24 ساعته - خدمات پزشکی 24 ساعته- خدمات لباسشویی - پارکینگ- فضای سبز بسیار زیبا و وسیع...-باغ مصفا(پیست پیاده روی)-نوشیدنی خوشامد گویی در بدو ورود-پیست دوچرخه سواری\r\n**امکان پخت و پز در آپارتمان ها و ویلاها وجود دارد.**', 'هزینه اقامت کودکان زیر 3سال رایگان می باشد.کودکان 3 تا 7 سال(در صورت عدم استفاده از سرویس اضافه)نیم بها می باشد.\r\nسرویس اضافه بصورت تخت تاشو می باشد.\r\nپذیرش صیغه نامه معتبر با مهر برجسته امکان پذیر است.\r\nپذیرش خانم تنها (بالای 18 سال)فقط با ارائه مدارک شناسایی معتبر امکان پذیر میباشد.', 'homa', 0, 1, 0, 0);

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
(23, 3, 10),
(25, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `main_passenger`
--

CREATE TABLE `main_passenger` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(75) NOT NULL,
  `lastname` varchar(75) NOT NULL,
  `email` varchar(75) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `nid` varchar(10) NOT NULL,
  `birthdate` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_passenger`
--

INSERT INTO `main_passenger` (`id`, `firstname`, `lastname`, `email`, `phone`, `nid`, `birthdate`) VALUES
(1, 'رضا', 'توانگر', 'rezatvg112@gmail.com', '09129471382', '1170545454', '1402/06/03'),
(2, 'رضا', 'Tavangar', 'rezatvg112@gmail.com', '09129471382', '1160484745', '1402/06/02');

-- --------------------------------------------------------

--
-- Table structure for table `main_passenger_reserves`
--

CREATE TABLE `main_passenger_reserves` (
  `id` bigint(20) NOT NULL,
  `passenger_id` bigint(20) NOT NULL,
  `request_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_passenger_reserves`
--

INSERT INTO `main_passenger_reserves` (`id`, `passenger_id`, `request_id`) VALUES
(1, 1, 23),
(2, 2, 23);

-- --------------------------------------------------------

--
-- Table structure for table `main_request`
--

CREATE TABLE `main_request` (
  `id` bigint(20) NOT NULL,
  `reserve_code` varchar(10) NOT NULL,
  `enter` varchar(20) NOT NULL,
  `exit` varchar(20) NOT NULL,
  `room_count` int(11) NOT NULL,
  `passenger_count` int(11) NOT NULL,
  `child_count` int(11) NOT NULL,
  `confirm` varchar(1) NOT NULL,
  `room_id` bigint(20) NOT NULL,
  `reserve_status` varchar(5) NOT NULL,
  `needs` varchar(255) NOT NULL,
  `reserve_time` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_request`
--

INSERT INTO `main_request` (`id`, `reserve_code`, `enter`, `exit`, `room_count`, `passenger_count`, `child_count`, `confirm`, `room_id`, `reserve_status`, `needs`, `reserve_time`) VALUES
(22, 'xzmnMvbajM', '1402/06/10', '1402/06/14', 1, 2, 0, 'A', 4, 'WI', '', '09:51'),
(23, 'sxd28scPfZ', '1402/06/20', '1402/06/27', 1, 2, 0, 'A', 2, 'P', '', '11:35'),
(24, 'Ncd9fMBdSt', '1402/06/21', '1402/06/25', 1, 2, 0, 'A', 2, 'P', '', '10:05'),
(25, '51iVwE1Mx1', '1402/07/12', '1402/07/23', 1, 2, 0, 'W', 4, 'WC', '', '17:16'),
(26, 'qhulEJTeHL', '1402/07/12', '1402/07/16', 1, 2, 0, 'W', 4, 'WC', '', '20:43');

-- --------------------------------------------------------

--
-- Table structure for table `main_room`
--

CREATE TABLE `main_room` (
  `id` bigint(20) NOT NULL,
  `name` varchar(75) NOT NULL,
  `faname` varchar(75) NOT NULL,
  `price` int(11) NOT NULL,
  `bed` int(11) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `image_booking` varchar(100) NOT NULL,
  `hotel_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `main_room`
--

INSERT INTO `main_room` (`id`, `name`, `faname`, `price`, `bed`, `slug`, `image`, `image_booking`, `hotel_id`) VALUES
(2, '3takhtgohar', 'سه تخته', 1300000, 3, '3takhtgohar-gohar', 'static/img/200x154/rezvan.jpeg', 'static/img/240x160/rezvan.jpeg', 2),
(3, '2takhtgohar', 'دو تخته', 820000, 2, '2takhtgohar-gohar', 'static/img/200x154/img1_wUgMrjN.jpg', 'static/img/240x160/img1_2XeKoqg.jpg', 2),
(4, '4takhtrezvan', 'چهار تخته', 1200000, 4, '4takhtrezvan-rezvan', 'static/img/200x154/rezvan_B0MT0Nv.jpeg', 'static/img/240x160/rezvan_bd0r2LU.jpeg', 1);

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
-- Indexes for table `accounts_user`
--
ALTER TABLE `accounts_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  ADD KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `accounts_user_hotel_likes`
--
ALTER TABLE `accounts_user_hotel_likes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_hotel_likes_user_id_hotel_id_7815ee85_uniq` (`user_id`,`hotel_id`),
  ADD KEY `accounts_user_hotel_likes_hotel_id_08087274_fk_main_hotel_id` (`hotel_id`);

--
-- Indexes for table `accounts_user_reserves`
--
ALTER TABLE `accounts_user_reserves`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_reserves_user_id_request_id_f513a3a4_uniq` (`user_id`,`request_id`),
  ADD KEY `accounts_user_reserves_request_id_763bb2ac_fk_main_request_id` (`request_id`);

--
-- Indexes for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  ADD KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`);

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
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`);

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
-- Indexes for table `main_passenger`
--
ALTER TABLE `main_passenger`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_passenger_reserves`
--
ALTER TABLE `main_passenger_reserves`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_passenger_reserves_passenger_id_request_id_f1ee5901_uniq` (`passenger_id`,`request_id`),
  ADD KEY `main_passenger_reserves_request_id_5ddfe85b_fk_main_request_id` (`request_id`);

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
-- AUTO_INCREMENT for table `accounts_user`
--
ALTER TABLE `accounts_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounts_user_hotel_likes`
--
ALTER TABLE `accounts_user_hotel_likes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounts_user_reserves`
--
ALTER TABLE `accounts_user_reserves`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `main_city`
--
ALTER TABLE `main_city`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `main_facility`
--
ALTER TABLE `main_facility`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `main_hotel`
--
ALTER TABLE `main_hotel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `main_hotel_facilities`
--
ALTER TABLE `main_hotel_facilities`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `main_passenger`
--
ALTER TABLE `main_passenger`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `main_passenger_reserves`
--
ALTER TABLE `main_passenger_reserves`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `main_request`
--
ALTER TABLE `main_request`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

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
-- Constraints for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_hotel_likes`
--
ALTER TABLE `accounts_user_hotel_likes`
  ADD CONSTRAINT `accounts_user_hotel_likes_hotel_id_08087274_fk_main_hotel_id` FOREIGN KEY (`hotel_id`) REFERENCES `main_hotel` (`id`),
  ADD CONSTRAINT `accounts_user_hotel_likes_user_id_ff912371_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_reserves`
--
ALTER TABLE `accounts_user_reserves`
  ADD CONSTRAINT `accounts_user_reserves_request_id_763bb2ac_fk_main_request_id` FOREIGN KEY (`request_id`) REFERENCES `main_request` (`id`),
  ADD CONSTRAINT `accounts_user_reserves_user_id_1b407514_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

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
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

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
-- Constraints for table `main_passenger_reserves`
--
ALTER TABLE `main_passenger_reserves`
  ADD CONSTRAINT `main_passenger_reser_passenger_id_0fa15c74_fk_main_pass` FOREIGN KEY (`passenger_id`) REFERENCES `main_passenger` (`id`),
  ADD CONSTRAINT `main_passenger_reserves_request_id_5ddfe85b_fk_main_request_id` FOREIGN KEY (`request_id`) REFERENCES `main_request` (`id`);

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
