<?php
session_start();
include_once "conexion.php";
$alarmas=mysqli_query($con,"select al.id_alarma as id,al.nombre as nombre,al.nombre_med as medicina,med.dosis as dosis, dia.fecha_inicio as inicio, dia.fecha_final as fin, horario.periodicidad as frecuencia  from alarma as al inner join medicamento as med on med.nombre_med=al.nombre_med inner join dia on dia.id_alarma=al.id_alarma inner join horario on horario.id_alarma=al.id_alarma;");
mysqli_close($con);
?>
<html>
<head>
<link rel="stylesheet" href="estilo2.css" media="all">
<div class="mensaje"><?php echo "Bievenido<h3>".$_SESSION["usuario"].'</h3><a href="cerrar.php">cerrar session</a> <a href="panel.php">\volver al menu principal</a>'; ?></div>
</head>
<body>
<br>
<table align="center" style="border:1px solid black; padding: 15px;">
<tr><td colspan=3 bgcolor="#000000"><font color="white"><center>Alarmas guardadas</center></font></td></tr>
<?php
while($row=mysqli_fetch_array($alarmas)) { ?>
<tr>
<td colspan=3>
<h3><?php echo '<center>'.$row["nombre"].'</center>';?></h3>
<?php echo $row["medicina"]." / ".$row["dosis"];?><br>
</td>
</tr>
<tr class="cajas">
<td colspan=2>
<?php echo "<b>Inicio:</b> ".$row["inicio"];?><br>
<?php echo "<b>Fin:</b> ".$row["fin"];?><br>
<?php echo "<b>Frecuencia:</b> ".$row["frecuencia"];?>
</td>
<td>
<?php echo '<input type="button" class="boton2" onclick="location.href=\'accion.php?accion=editar&id='.$row["id"].'\'" value="Editar"><br>' ?>
<?php echo '<input type="button" class="boton2" onclick="location.href=\'accion.php?accion=borrar&id='.$row["id"].'\'" value="Borrar">' ?>
</td>
</tr><br>
<?php 
}
?>
</table>
</body>
</html>