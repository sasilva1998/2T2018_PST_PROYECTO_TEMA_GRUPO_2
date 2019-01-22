<?php
session_start();
include_once "conexion.php";
$id=$_POST["id"];
$nombre=$_POST["nombre"];
$medicamento=$_POST["medicamento"];
$dosis=$_POST["dosis"];
$laboratorio=$_POST["laboratorio"];
$tipo=$_POST["tipo"];
$hora=$_POST["hora"];
$minuto=$_POST["minuto"];
$periodicidad=$_POST["periodicidad"];
$inicio=$_POST["inicio"];
$fin=$_POST["fin"];
$res=mysqli_query($con,"SELECT count(*) AS cuenta from medicamento where nombre_med='".$medicamento."';");
$count=(mysqli_fetch_array($res))["cuenta"];
if($count==1){
	mysqli_query($con,"update medicamento set dosis=".$dosis.", laboratorio='".$laboratorio."', tipo='".$tipo."' where nombre_med='".$medicamento."';");
}else{
	mysqli_query($con,"delete from medicamento where nombre_med=(select nombre_med from alarma where id_alarma=".$id.");");
	$res=mysqli_query($con,"insert into medicamento values ('".$medicamento."',".$dosis.",'".$laboratorio."','".$tipo."');");
	
}
mysqli_query($con,"update alarma set nombre='".$nombre."',nombre_med='".$medicamento."' where id_alarma=".$id.";");
mysqli_query($con,"update horario set hora=".$hora.",minuto=".$minuto.",periodicidad=".$periodicidad." where id_alarma=".$id.";");
mysqli_query($con,"update dia set fecha_inicio='".$inicio."',fecha_final='".$fin."' where id_alarma=".$id.";");

echo "<script>alert('Alarma modificada')</script>";
echo "<script>location.href='alarmas.php';</script>";
?>
