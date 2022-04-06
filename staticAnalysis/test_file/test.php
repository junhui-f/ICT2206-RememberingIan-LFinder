<html>

<!--header content-->

<head>
    <title>About Us</title>
    <!--something about /../etc/passwd-->
    <!--or was it /../etc/not_a_password-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/bootstrap.min.css" type="text/css">
    <script defer src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <script defer src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js" integrity="sha384-6khuMg9gaYr5AxOqhkVIODVIvm9ynTT5J4V1cfthmT+emCG6yVmEZsRHdxlotUnm" crossorigin="anonymous"></script>
    <script defer src="js/main.js"></script>
</head>

<!--body content-->

<body>
    <!--navigation bar-->
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
        <a class="navbar-brand" href="index.html"><img src="images/LOGO.png" width="350" /></a>
    </nav>
    <div class="collapse" id="navbarToggleExternalContent">
        <div class="bg-dark p-4">
            <a class="navbar-brand" href="index.html">Home</a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="aboutus.php">About Us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="login.php">Login</a>
                </li>
            </ul>
        </div>
    </div>
    <nav class="navbar navbar-dark bg-dark">
        <button id="button" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
    </nav>
    <!--title-->
    <header class="jumbotron text-center">
        <h1 class="display-4">Welcome to World of Pets!</h1>
        <h2>Home of Singapore's Pet Lovers</h2>
    </header>
    <!--about us content-->
    <main class="container">
        <section id="about us">
            <div class="row">
                <?php

                // virtual
                $script_name = $_GET['test1.pl'];
                virtual($script_name);

                // include
                if (isset($_GET['fish'])) {
                    include($_GET['fish']);
                }
                $animal = $_POST['test2'];
                include($_POST['test2']);
                include($animal);

                // require
                $file = $_GET['test3'];
                require($file . ".php");

                // include_once
                $input = addslashes($_GET["test4"]);
                if (strpos($input, '../') === false) {
                    include_once('/path/to/php/files/'.$input);
                } else { echo('Invalid parameter!'); }

                // require_once
                if (isset($_GET['test5']))
                {
                    $which = $_GET['test5'];
                    require_once($which.'noparenthesis.php');
                }

                // file_get_contents
                $id = $_GET['test6'];
                echo(file_get_contents("template/data/".$id));

                // file_put_contents
                $image = $_GET['test7'];
                file_put_contents("folder\\".$image.".PNG");

                // show_source
                $item = $_GET['test8'];
                show_source($item);

                // fopen
                $accountfile = $_GET['test9'];
                fopen($accountfile, "r");

                // file
                $web = $_GET['http://www.google.com/test10'];
                file($web);

                // fpassthru
                $filename = $_GET['test11'];
                $fp = fopen($filename, 'rb');
                fpassthru($fp);

                // gzopen
                $gzopenfile = $_GET['test12.gz'];
                gzopen($gzopenfile, "r");

                // gzpassthru
                $gzpassthrufile = gzopen('test13.gz', 'r');
                gzpassthru($gzpassthrufile);

                // DirectoryIterator
                $iterator = $_GET['C:\test14\\'];
                new DirectoryIterator($iterator);

                // stream_get_contents
                $stream = ssh2_exec('test15', 'cmd');
                stream_get_contents($stream);

                // copy
                $copyfile = $_GET['test16.txt'];
                copy($copyfile, 'newfile.txt');

                ?>
            </div>
        </section>
    </main>
</body>

</html>
