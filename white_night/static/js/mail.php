<?php
echo 'test';
$recepient = "artem.pif@mail.ru";
$sitename = "whitenight";

$name = trim($_POST["name"]);
$phone = trim($_POST["phone"]);
$date = trim($_POST["date"]);
$time_from = trim($_POST["time_from"]);
$time_to = trim($_POST["time_to"]);
$details = trim($_POST["details"]);

$message = "Имя: $name \nТелефон: $phone Дата: $date \n Звонить с $time_from  до $time_to  \nПодробности: $details";

file_put_contents('test_work_php.txt', $message);

$pagetitle = "Новая заявка с сайта \"$sitename\"";
mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");
?>