<?php
session_start();
include_once "conexion.php";
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
	$res=mysqli_query($con,"insert into medicamento values ('".$medicamento."',".$dosis.",'".$laboratorio."','".$tipo."');");
	echo $res;
}
$alarma_id=mysqli_fetch_array(mysqli_query($con,"select max(id_alarma) as cuenta from alarma"))["cuenta"]+1;
mysqli_query($con,"insert into alarma values (".$alarma_id.",'".$nombre."','".$medicamento."');");
mysqli_query($con,"insert into horario (hora,minuto,periodicidad,id_alarma) values (".$hora.",".$minuto.",".$periodicidad.",".$alarma_id.");");
mysqli_query($con,"insert into dia (fecha_inicio,fecha_final,id_alarma) values ('".$inicio."','".$fin."',".$alarma_id.");");

echo "<script>alert('Alerta guardada')</script>";
echo "<script>location.href='panel.php';</script>";
?>