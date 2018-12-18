<?php
if(isset($_POST['update']))
{   
    
    $output=shell_exec('python3 choose_file.py');
    
    
    header('location:set_directory.html');
}
?>