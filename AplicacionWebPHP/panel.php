<?php
session_start();
$nombreusuario= $_SESSION["usuario"];

?>
<html>
<head>
<link rel="stylesheet" href="estilo.css" media="all">
<div class="mensaje">Bievenido<h3><?php echo $nombreusuario ?></h3><a href="cerrar.php"> \ cerrar session</a></div>
</head>
<body>
<br>
<form action="guardar.php" method="post">
<table align="center" style="border:1px solid black; padding: 15px;">
<caption>Nueva Alarma</caption>
<tr>
<td colspan=2>
<span>Nombre:</span><br/>
<input class= "cajas" type="text" name="nombre" required>
</td>
</tr>
<tr>
<td colspan=2>
<span>Medicamento:</span><br/>
<input class= "cajas" type="text" name="medicamento" required>
</td>
</tr>
<tr>
<td colspan=2>
<span>Dosis:</span><br/>
<input class="cajas" type="number" name="dosis" required>
</td>
</tr>
<tr>
<td colspan=2>
<span>Laboratorio:</span><br/>
<input class="cajas" type="text" name="laboratorio">
</td>
</tr>
<tr>
<td colspan=2>
<span>Tipo:</span><br/>
<input class="cajas" type="text" name="tipo">
</td>
</tr>
<tr>
<td colspan=2>
<span>Hora:</span><br/>
<input class="cajas" type="number" name="hora">
</td>
</tr>
<tr>
<td colspan=2>
<span>Minutos:</span><br/>
<input class="cajas" type="number" name="minuto">
</td>
</tr>
<tr>
<td colspan=2>
<span>Frecuencia:</span><br/>
<input class="cajas" type="number" name="periodicidad" required>
</td>
</tr>
<tr>
<td colspan=2>
<span>Inicio:</span><br/>
<input class="cajas" type="date" name="inicio" required>
</td>
</tr>
<tr>
<td colspan=2>
<span>Fin:</span><br/>
<input class="cajas" type="date" name="fin" required>
</td>
</tr>
<tr>
<td>
<br/>
<input type="submit" class="boton" value="Guardar">
</td>
<td>
<br/>
<input type="button" class="boton" onclick="location.href='alarmas.php'" value="Ver alarmas">
</td>
</tr>
</table>
</form>
</body>
</html>