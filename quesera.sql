-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-03-2024 a las 21:11:01
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `quesera`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
(25, 'Can add slider image', 7, 'add_sliderimage'),
(26, 'Can change slider image', 7, 'change_sliderimage'),
(27, 'Can delete slider image', 7, 'delete_sliderimage'),
(28, 'Can view slider image', 7, 'view_sliderimage'),
(29, 'Can add carrito', 8, 'add_carrito'),
(30, 'Can change carrito', 8, 'change_carrito'),
(31, 'Can delete carrito', 8, 'delete_carrito'),
(32, 'Can view carrito', 8, 'view_carrito'),
(33, 'Can add categoria', 9, 'add_categoria'),
(34, 'Can change categoria', 9, 'change_categoria'),
(35, 'Can delete categoria', 9, 'delete_categoria'),
(36, 'Can view categoria', 9, 'view_categoria'),
(37, 'Can add producto', 10, 'add_producto'),
(38, 'Can change producto', 10, 'change_producto'),
(39, 'Can delete producto', 10, 'delete_producto'),
(40, 'Can view producto', 10, 'view_producto'),
(41, 'Can add detalle carrito', 11, 'add_detallecarrito'),
(42, 'Can change detalle carrito', 11, 'change_detallecarrito'),
(43, 'Can delete detalle carrito', 11, 'delete_detallecarrito'),
(44, 'Can view detalle carrito', 11, 'view_detallecarrito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$LDzSObcM19OZA62UvDy4a0$pMFLP0U03Lm05PQgqhUx848RCqZyA1MzaUey1OfvjQM=', '2024-03-06 19:34:58.731055', 1, 'leduan', '', '', 'ledu@mail.com', 1, 1, '2024-03-06 14:47:32.689424');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-03-06 14:48:22.558452', '1', 'img', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-03-06 15:04:28.511341', '2', 'dasda', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-03-06 15:40:51.274437', '3', 'dasdad', 1, '[{\"added\": {}}]', 7, 1),
(4, '2024-03-06 16:06:25.869380', '4', 'queso', 1, '[{\"added\": {}}]', 7, 1),
(5, '2024-03-06 16:07:09.820626', '5', 'dsadsa', 1, '[{\"added\": {}}]', 7, 1),
(6, '2024-03-06 17:41:09.521144', '6', 'img', 1, '[{\"added\": {}}]', 7, 1),
(7, '2024-03-06 17:41:29.249539', '7', 'a', 1, '[{\"added\": {}}]', 7, 1),
(8, '2024-03-06 17:43:46.063714', '7', 'a', 3, '', 7, 1),
(9, '2024-03-06 17:43:58.622278', '6', 'img', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(10, '2024-03-06 17:44:18.147949', '8', 'dasdadas', 1, '[{\"added\": {}}]', 7, 1),
(11, '2024-03-06 17:44:29.095155', '9', 'dasdadasdsa', 1, '[{\"added\": {}}]', 7, 1),
(12, '2024-03-06 17:57:34.581358', '8', 'dasdadas', 3, '', 7, 1),
(13, '2024-03-06 17:57:37.540308', '6', 'img', 3, '', 7, 1),
(14, '2024-03-06 17:57:46.018928', '10', 'adasda', 1, '[{\"added\": {}}]', 7, 1),
(15, '2024-03-06 17:58:07.714654', '11', 'dasda', 1, '[{\"added\": {}}]', 7, 1),
(16, '2024-03-06 19:37:52.397703', '1', 'Qusesos', 1, '[{\"added\": {}}]', 9, 1),
(17, '2024-03-06 19:38:52.524807', '1', 'Queso mozarella', 1, '[{\"added\": {}}]', 10, 1),
(18, '2024-03-06 19:39:23.846037', '2', 'Lechera', 1, '[{\"added\": {}}]', 10, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'Productos', 'carrito'),
(9, 'Productos', 'categoria'),
(11, 'Productos', 'detallecarrito'),
(10, 'Productos', 'producto'),
(7, 'Productos', 'sliderimage'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Productos', '0001_initial', '2024-03-06 14:45:09.486164'),
(2, 'contenttypes', '0001_initial', '2024-03-06 14:45:09.536610'),
(3, 'auth', '0001_initial', '2024-03-06 14:45:09.942168'),
(4, 'admin', '0001_initial', '2024-03-06 14:45:10.039789'),
(5, 'admin', '0002_logentry_remove_auto_add', '2024-03-06 14:45:10.046807'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-06 14:45:10.053780'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-03-06 14:45:10.099661'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-03-06 14:45:10.145158'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-03-06 14:45:10.160331'),
(10, 'auth', '0004_alter_user_username_opts', '2024-03-06 14:45:10.166361'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-03-06 14:45:10.202396'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-03-06 14:45:10.204397'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-03-06 14:45:10.212396'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-03-06 14:45:10.225991'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-03-06 14:45:10.238158'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-03-06 14:45:10.251263'),
(17, 'auth', '0011_update_proxy_permissions', '2024-03-06 14:45:10.260373'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-03-06 14:45:10.274354'),
(19, 'sessions', '0001_initial', '2024-03-06 14:45:10.300759'),
(20, 'Productos', '0002_alter_sliderimage_image', '2024-03-06 16:05:29.085672'),
(21, 'Productos', '0003_carrito_categoria_alter_sliderimage_title_producto_and_more', '2024-03-06 19:34:38.097116');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('do9nh3zdd8pak99ua7rqgco8stqnflpo', '.eJxVjrEOwjAMRP8lM4rqkLSBkZ1vqGzHJgXUSGk7If6dFnWA9d7d071Mj8uc-2WS2g_JnA2Yw29GyA8ZN5DuON6K5TLOdSC7VexOJ3stSZ6XvfsnyDjldR0okDonXkihBe2SDxJ9oyS-paCK2pHXRBHhBHJkYUnELoJrmKhbpYy1DnP53oT3B6GNPqM:1rhxRY:rjmyEb9OCLkQopaqdCJRGjqwCm6dnyfCpiO672tPRf4', '2024-03-20 20:00:48.325320'),
('sasi7sgnqq27mfmxu3hl9lrcrvherel9', '.eJxVjEEOwiAQRe_C2pAOQkGX7j0DYZgZqRpISrsy3l2bdKHb_977LxXTupS4dp7jROqsQB1-N0z5wXUDdE_11nRudZkn1Juid9r1tRE_L7v7d1BSL9_aoUMxhi2jwAjiyToOdhBkO6ITSeLRCmFIcAI-Zs5MmE0AM2REr94fGkc5qA:1rhsYj:ZgmxSu8hbXhJs_cncX8EGPBI_lyqCM1xAEUglt2Hb3Y', '2024-03-20 14:47:53.239145');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_carrito`
--

CREATE TABLE `productos_carrito` (
  `id` bigint(20) NOT NULL,
  `total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos_carrito`
--

INSERT INTO `productos_carrito` (`id`, `total`) VALUES
(1, 32000.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_categoria`
--

CREATE TABLE `productos_categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos_categoria`
--

INSERT INTO `productos_categoria` (`id`, `nombre`) VALUES
(1, 'Qusesos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_detallecarrito`
--

CREATE TABLE `productos_detallecarrito` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(10) UNSIGNED NOT NULL CHECK (`cantidad` >= 0),
  `carrito_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos_detallecarrito`
--

INSERT INTO `productos_detallecarrito` (`id`, `cantidad`, `carrito_id`, `producto_id`) VALUES
(1, 1, 1, 1),
(2, 1, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_producto`
--

CREATE TABLE `productos_producto` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `categoria_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos_producto`
--

INSERT INTO `productos_producto` (`id`, `nombre`, `precio`, `imagen`, `categoria_id`) VALUES
(1, 'Queso mozarella', 20000.00, 'imagenes/hacer-queso-duro_uBP2MbF.jpg', 1),
(2, 'Lechera', 12000.00, 'imagenes/R.jfif', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_sliderimage`
--

CREATE TABLE `productos_sliderimage` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos_sliderimage`
--

INSERT INTO `productos_sliderimage` (`id`, `image`, `title`, `description`) VALUES
(9, 'slider_images/Mortal-Kombat-X-Background-Wallpaper-03969.png', 'dasdadasdsa', 'dasda'),
(10, 'slider_images/fifa18_g9CfXSZ.png', 'adasda', 'dsad'),
(11, 'slider_images/thumb-1920-926723.png', 'dasda', 'dasda');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `productos_carrito`
--
ALTER TABLE `productos_carrito`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos_categoria`
--
ALTER TABLE `productos_categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos_detallecarrito`
--
ALTER TABLE `productos_detallecarrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Productos_detallecar_carrito_id_1715c14d_fk_Productos` (`carrito_id`),
  ADD KEY `Productos_detallecar_producto_id_83bd1f1a_fk_Productos` (`producto_id`);

--
-- Indices de la tabla `productos_producto`
--
ALTER TABLE `productos_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Productos_producto_categoria_id_4f5862b8_fk_Productos` (`categoria_id`);

--
-- Indices de la tabla `productos_sliderimage`
--
ALTER TABLE `productos_sliderimage`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `productos_carrito`
--
ALTER TABLE `productos_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `productos_categoria`
--
ALTER TABLE `productos_categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `productos_detallecarrito`
--
ALTER TABLE `productos_detallecarrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `productos_producto`
--
ALTER TABLE `productos_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `productos_sliderimage`
--
ALTER TABLE `productos_sliderimage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `productos_detallecarrito`
--
ALTER TABLE `productos_detallecarrito`
  ADD CONSTRAINT `Productos_detallecar_carrito_id_1715c14d_fk_Productos` FOREIGN KEY (`carrito_id`) REFERENCES `productos_carrito` (`id`),
  ADD CONSTRAINT `Productos_detallecar_producto_id_83bd1f1a_fk_Productos` FOREIGN KEY (`producto_id`) REFERENCES `productos_producto` (`id`);

--
-- Filtros para la tabla `productos_producto`
--
ALTER TABLE `productos_producto`
  ADD CONSTRAINT `Productos_producto_categoria_id_4f5862b8_fk_Productos` FOREIGN KEY (`categoria_id`) REFERENCES `productos_categoria` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
