<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Moisture Calculator</title>
  <!-- Compiled and minified CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.2/css/materialize.min.css">

  <!-- Compiled and minified JavaScript -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.2/js/materialize.min.js"></script>
  <script src="http://s.codepen.io/assets/libs/modernizr.js" type="text/javascript"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
  <link rel="stylesheet" href="css/style.css">


</head>

<body>
<div class="row">
  <div class="col 6s" style="padding-left: 30%">
    <div id="container" >
      <div class="pour"></div>
      <div id="beaker">
        <div id="liquid">
          <div class="bubble bubble1"></div>
          <div class="bubble bubble2"></div>
          <div class="bubble bubble3"></div>
          <div class="bubble bubble4"></div>
          <div class="bubble bubble5"></div>
        </div>
      </div>
    </div>
    <h3>Water level for Crop1</h3>
  </div>
  <div class="col 6s ">
    <div id="container2" >
      <div class="pour"></div>
      <div id="beaker2">
        <div id="liquid2">
          <div class="bubble bubble1"></div>
          <div class="bubble bubble2"></div>
          <div class="bubble bubble3"></div>
          <div class="bubble bubble4"></div>
          <div class="bubble bubble5"></div>
        </div>
      </div>
    </div>
    <h3>Water level for Crop2</h3>
  </div>
</div>
<script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

<script src="js/index.js"></script>

</body>
</html>
