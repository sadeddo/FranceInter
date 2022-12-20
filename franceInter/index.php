            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="css/style.css">
                <title>Document</title>
            </head>
            <header>
            <img src="logo.png" alt="Logo esa">
            
            </header>
            <body>
                <div class="main"> 
            <div class="form"> 
                <form action="" method="post" enctype="multipart/form-data">
                    <div class="ecrituresform">
                    <label for="">Message à diffuser</label>
                    <input type="text" class="form-control" name="message" required>
                    <br>
                    <label for="">Image</label>
                    <input type="file" class="form-control" name="image" required>
                    <br>
                    <label for="">Le nombre max de personnes</label>
                    <input type="number" class="form-control" name="nombre" required>
                    <br>
                    <input type="submit" value="LANCER" style="margin-left: 30%;background-color:red;width: 130px;height: 40px;border-radius: 5px;" name="submit" required>
                    <br>
        </div>  
                </form>
                </div>

            <?php

            //// message et nombre ///

            if(isset($_REQUEST["message"])){
            $message = $_REQUEST["message"] ;
            }
            if(isset($_REQUEST["nombre"])){
            $number =  $_REQUEST["nombre"];
            }
            if(isset($_REQUEST["image"])){
            $image =  $_FILES["image"];
            }

            $fichier = "fichier.json";

            if(isset($_FILES['image'])){
                $FileName = ($_FILES['image']['name']);
                $cheminimageoriginal = ($_FILES['image']['tmp_name']);
                move_uploaded_file($cheminimageoriginal, "images/".$FileName);
            }
            //// fin image ////

            $contenufichier = file_get_contents($fichier);


            $jsonData = json_decode($contenufichier);
            if(isset($number, $message, $FileName)){
            $jsonData->nombre = $number;
            $jsonData->message = $message;
            $jsonData->image = $FileName;
            }

            file_put_contents($fichier, json_encode($jsonData));


            //// fin message et nombre ///


            if (isset($_REQUEST["submit"])){
                $test = shell_exec('python3 python.py');
                if ( $test == 'ok'){
                ?>
                
            <audio autoplay>
                <source src="audioFr.wav" type="audio/wav">
                <p>Votre navigateur est trop ancien pour lire ce fichier</p>
                </audio>

            </div>
            </body>
            </html>
            <?php }}  ?>


            <?php






            ?>




