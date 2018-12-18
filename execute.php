<?php
if(isset($_POST['choose']))
{   
    $output=shell_exec("python3 directory_set.py");
    
    header('location:set_directory.html');
}
?>

