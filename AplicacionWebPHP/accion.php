<?php
session_start();
include_once "conexion.php";
if($_GET["accion"]=='borrar'){
	
	mysqli_query($con,"delete from horario where id_alarma=".$_GET["id"].";");
	mysqli_query($con,"delete from dia where id_alarma=".$_GET["id"].";");
	mysqli_query($con,"delete from medicamento where nombre_med=(select nombre_med from alarma where id_alarma=".$_GET["id"].");");
	mysqli_query($con,"delete from alarma where id_alarma=".$_GET["id"].";");
	mysqli_close($con);
	echo "<script>alert('Alerta eliminada')</script>";
	echo "<script>location.href='alarmas.php';</script>";
}else{ 
$res=mysqli_fetch_array(mysqli_query($con,"select al.nombre as nombre,al.nombre_med as medicina,med.dosis as dosis,med.laboratorio as laboratorio,med.tipo as tipo,horario.minuto as minutos, horario.hora as hora, dia.fecha_inicio as inicio, dia.fecha_final as fin, horario.periodicidad as frecuencia  from alarma as al inner join medicamento as med on med.nombre_med=al.nombre_med inner join dia on dia.id_alarma=al.id_alarma inner join horario on horario.id_alarma=al.id_alarma where al.id_alarma=".$_GET["id"].";"));
?>
<html>
<head>
<link rel="stylesheet" href="estilo.css" media="all">
<div class="mensaje">Bievenido<h3><?php echo $_SESSION["usuario"] ?></h3><a href="cerrar.php">cerrar session</a></div>
</head>
<body>
<br>
<form action="editar.php" method="post">
<table align="center" style="border:1px solid black; padding: 15px;">
<caption>Editar alarma</caption>
<tr>
<td colspan=2>
<?php echo '<input type="hidden" name="id" value="'.$_GET["id"].'" />';?>
<span>Nombre:</span><br/>
<?php echo '<input class= "cajas" type="text" name="nombre" value="'.$res["nombre"].'" required>';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Medicamento:</span><br/>
<?php echo '<input class= "cajas" type="text" name="medicamento" value="'.$res["medicina"].'"required>';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Dosis:</span><br/>
<?php echo '<input class="cajas" type="number" name="dosis" value="'.$res["dosis"].'" required>';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Laboratorio:</span><br/>
<?php echo '<input class="cajas" type="text" value="'.$res["laboratorio"].'" name="laboratorio">';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Tipo:</span><br/>
<?php echo '<input class="cajas" type="text" value="'.$res["tipo"].'" name="tipo">';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Hora:</span><br/>
<?php echo '<input class="cajas" type="number" value="'.$res["hora"].'" name="hora">';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Minutos:</span><br/>
<?php echo '<input class="cajas" type="number" value="'.$res["minutos"].'" name="minuto">';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Frecuencia:</span><br/>
<?php echo '<input class="cajas" type="number" name="periodicidad" value="'.$res["frecuencia"].'" required>';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Inicio:</span><br/>
<?php echo '<input class="cajas" type="date" name="inicio" value="'.$res["inicio"].'" required>';?>
</td>
</tr>
<tr>
<td colspan=2>
<span>Fin:</span><br/>
<?php echo '<input class="cajas" type="date" name="fin" value="'.$res["fin"].'" required>';?>
</td>
</tr>
<tr>
<td>
<br/>
<input type="submit" class="boton" value="Guardar">
</td>
<td>
<br/>
<input type="button" class="boton" onclick="location.href='alarmas.php'" value="Cancelar">
</td>
</tr>
</table>
</form>
</body>
</html>
<?php
}

?>