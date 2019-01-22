<?php
session_start();
include_once "conexion.php";
$usu= $_POST["usuario"];
$pwd= $_POST["clave"];

$logueo= mysqli_query($con,"SELECT COUNT(*) As total FROM login WHERE usuario='".$usu."' AND password='".$pwd."';");
if(mysqli_fetch_array($logueo)["total"]==1)
{
$_SESSION["usuario"]=$usu;

echo"<script>location.href='panel.php';</script>";
}
else
{
echo "<script>alert('usuario o clave incorrectos')</script>";
echo "<script>location.href='index.php';</script>";
}
mysqli_close($con);
?>