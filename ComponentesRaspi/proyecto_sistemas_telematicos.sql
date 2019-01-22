-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-01-2019 a las 01:34:03
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_sistemas_telematicos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alarma`
--

CREATE TABLE `alarma` (
  `id_alarma` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `nombre_med` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `alarma`
--

INSERT INTO `alarma` (`id_alarma`, `nombre`, `nombre_med`) VALUES
(1, 'test', 'aspirina'),
(2, 'Pulmonia', 'sertal'),
(3, 'Cancer', 'lemon flu');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dia`
--

CREATE TABLE `dia` (
  `id_dia` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_final` date NOT NULL,
  `id_alarma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dia`
--

INSERT INTO `dia` (`id_dia`, `fecha_inicio`, `fecha_final`, `id_alarma`) VALUES
(12, '2019-01-30', '2019-01-09', 1),
(13, '2019-01-15', '2019-01-24', 2),
(14, '2019-01-15', '2019-01-19', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

CREATE TABLE `horario` (
  `id_horario` int(11) NOT NULL,
  `hora` int(2) NOT NULL,
  `minuto` int(2) NOT NULL,
  `periodicidad` int(2) NOT NULL,
  `id_alarma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `horario`
--

INSERT INTO `horario` (`id_horario`, `hora`, `minuto`, `periodicidad`, `id_alarma`) VALUES
(11, 3, 3, 3, 1),
(12, 2, 4, 4, 2),
(13, 4, 3, 3, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE `login` (
  `usuario` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `login`
--

INSERT INTO `login` (`usuario`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicamento`
--

CREATE TABLE `medicamento` (
  `nombre_med` varchar(30) NOT NULL,
  `dosis` int(1) NOT NULL,
  `laboratorio` varchar(30) NOT NULL,
  `tipo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `medicamento`
--

INSERT INTO `medicamento` (`nombre_med`, `dosis`, `laboratorio`, `tipo`) VALUES
('aspirina', 3, 'bayern', 'anticoagulante'),
('lemon flu', 3, 'bayern', 'oncogeno'),
('sertal', 2, 'bayern', 'analgesico');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alarma`
--
ALTER TABLE `alarma`
  ADD PRIMARY KEY (`id_alarma`),
  ADD KEY `nombre_med` (`nombre_med`);

--
-- Indices de la tabla `dia`
--
ALTER TABLE `dia`
  ADD PRIMARY KEY (`id_dia`),
  ADD KEY `id_alarma` (`id_alarma`);

--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`id_horario`),
  ADD KEY `id_alarma` (`id_alarma`);

--
-- Indices de la tabla `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`usuario`);

--
-- Indices de la tabla `medicamento`
--
ALTER TABLE `medicamento`
  ADD PRIMARY KEY (`nombre_med`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alarma`
--
ALTER TABLE `alarma`
  MODIFY `id_alarma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `dia`
--
ALTER TABLE `dia`
  MODIFY `id_dia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `horario`
--
ALTER TABLE `horario`
  MODIFY `id_horario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `dia`
--
ALTER TABLE `dia`
  ADD CONSTRAINT `Dia_ibfk_1` FOREIGN KEY (`id_alarma`) REFERENCES `alarma` (`id_alarma`);

--
-- Filtros para la tabla `horario`
--
ALTER TABLE `horario`
  ADD CONSTRAINT `Horario_ibfk_1` FOREIGN KEY (`id_alarma`) REFERENCES `alarma` (`id_alarma`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
