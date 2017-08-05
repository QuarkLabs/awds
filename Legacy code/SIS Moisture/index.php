<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Moisture Calculator</title>

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.2/css/materialize.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="js/jquery-3.2.0.min.js"></script>
    <script src="js/index.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.2/js/materialize.min.js"></script>
    <!--<script src="http://s.codepen.io/assets/libs/modernizr.js" type="text/javascript"></script>-->

    <style>
        .container{
            margin-top: 100px;
        }
    </style>
</head>

<body>
<nav>
    <div class="nav-wrapper green" style="padding-top:10px; ">
        <a href="#" class="brand-logo center ">Smart Irrigation System</a>
    </div>
</nav>
<div id="home" class="container" >
    <div class="form_container">
        <form class="col s12" action = "bottle.php" method = "GET">
            <div class="row">

                <div class="input-field col s6">
                    <input placeholder="Moisture amount of Crop 1" id="moisture1" name="moisture1" type="number" class="validate">
                </div>

                <div class="input-field col s6">
                    <input placeholder="Moisture amount of Crop 2" id="moisture2" name="moisture2" type="number" class="validate">
                </div>
            </div>
            <div class="row">
                <div class=" col s12 center">
                    <button type="submit" class="btn waves-effect waves-light" id="btnSend" formmethod="get">Send Data</button>
                </div>
            </div>
            <div class="row">
                <div class=" col s12 center">
                    <button type="reset" class="btn waves-effect waves-light">Reset Data</button>
                </div>
            </div>
        </form>
    </div>
</div>
</body>
<body>
</body>
</html>
