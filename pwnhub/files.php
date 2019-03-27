<!DOCTYPE HTML>
<html>
    <head>
        <title> files</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="cc.css">
    </head>
    <body><div id="main">
        <!-- a welcome message -->
        <h1>Welcome <?php
            error_reporting(0);
            session_start();
            if (!isset($_SESSION['userName'])) {
                header("Location: please.php");
                exit;
            }
            echo $_SESSION['userName'];
        ?></h1><br />
        <!-- the uploading section -->
        <form enctype="multipart/form-data" action="uploader.php" method="POST">
            <p>
                <input type="hidden" name="MAX_FILE_SIZE" value="20000000" />
                <label for="uploadfile_input">Choose a file to upload:</label> <input name="file" type="file" id="uploadfile_input" />
            </p>
            <p>
                <input type="submit" name="submit" value="Upload File" />
            </p>
        </form>
        <br><br>
        <!-- show the file index as a tabel-->
        <!-- provide three buttons for file operations -->
        <?php
        function listDir($dir){
            if(!is_dir($dir)){
                return '';
                echo "ERROR!";
            }
            $dirList = array('dirNum'=>0,'fileNum'=>0,'lists'=>'');
            if (!$dirHandle = opendir($dir)){
                echo "ERROR!Can't open Dir. <br>";
            }
            $i = 1;
            while($file = readdir($dirHandle)){
                if(!is_dir($file)){
                    $dirList['lists'][$i]['name'] = $file; 
                    $dirList['lists'][$i]['isDir'] = false;
                    $dirList['fileNum'] += 1;
                    $i += 1;
                }                            
            }
            closedir($dirHandle);
            return $dirList;
        }
        
        session_start();
        $userName = $_SESSION['userName'];
        $dir = "./users_file_system/".$userName."/";
        $DirectoryList = listDir($dir);
        if ($DirectoryList['fileNum'] == 0) {
            echo "<p>Empty</p>";
        }
        else {
            echo "<table>
                    <tr>
                        <th>File Name</th>
                        <th>Operations</th>
                    </tr>";
            for($i = 1; $i <= $DirectoryList['fileNum']; $i++ ){
                $currentFile = $DirectoryList['lists'][$i]['name'];
                $currentFileDir = $dir.$currentFile;
                 echo "<tr>";
                echo "<td>" . $currentFile ."</td>";
                echo "<td> <form action= \"do_operation.php\" method=\"POST\">";
                echo "<input type=\"hidden\" name=\"file\" value =". $currentFile.">";
                echo "<input type=\"submit\" name=\"action\" value=\"Delete\"> ";
                echo "</form>";
                echo "</td>";
                echo "</tr>";
            }      
            echo "</table>";
        }
        ?>
        <br><br><br>
        <!-- the log out section -->
        <form action="logout.php">
            <input type="submit" value="logout">
        </form>
    </div></body>
</html>
