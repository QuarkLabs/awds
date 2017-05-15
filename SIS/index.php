<?php
    require ('db_connect.php');

    $farmerID = 100;
    $cropID1 = 1000;
    $cropID2 = 1001;

    //Query for the temperature for crop 1
    $temp_sql1 = "SELECT temperature FROM crop_condition WHERE farmer_has_crop_farmer_id = '$farmerID' and farmer_has_crop_crop_id = '$cropID1'";
    //Query for the temperature for crop 2
    $temp_sql2 = "SELECT temperature FROM crop_condition WHERE farmer_has_crop_farmer_id = '$farmerID' and farmer_has_crop_crop_id = '$cropID2'";

    //Query for the water level for crop 1
    $water_sql1 = "SELECT SUM(rec_water) AS waterlvl1 FROM crop_condition WHERE farmer_has_crop_farmer_id = $farmerID and farmer_has_crop_crop_id = $cropID1 AND calculated_date BETWEEN '2017-05-03 00:00:00' AND '2017-05-14 00:00:00'";
    //Query for the temperature for crop 2
    $water_sql2 = "SELECT SUM(rec_water) AS waterlvl2 FROM crop_condition WHERE farmer_has_crop_farmer_id = $farmerID and farmer_has_crop_crop_id = $cropID2 AND calculated_date BETWEEN '2017-05-03 00:00:00' AND '2017-05-14 00:00:00'";

    //temp values
    $temp1 = mysqli_query($conn, $temp_sql1);
    $temp_val1 = mysqli_fetch_assoc($temp1);
    $temp2 = mysqli_query($conn, $temp_sql2);
    $temp_val2 = mysqli_fetch_assoc($temp2);
    //water values
    $water1 = mysqli_query($conn, $water_sql1);
    $water_val1 = mysqli_fetch_assoc($water1);
    $water2 = mysqli_query($conn, $water_sql2);
    $water_val2 = mysqli_fetch_assoc($water2);

?>
<!DOCTYPE html>
<html>
<head>
  <title>Smart Irrigation System - Dashboard</title>

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <?php include ('include/css.php'); ?>

</head>
<body>
  <div class="app app-default">

    <?php include ('include/nav.php'); ?>

<script type="text/ng-template" id="sidebar-dropdown.tpl.html">
  <div class="dropdown-background">
    <div class="bg"></div>
  </div>
  <div class="dropdown-container">
    {{list}}
  </div>
</script>
<div class="app-container">

  <?php include ('include/nav-mobile.php'); ?>

<div class="row">
  <div class="col-xs-6">
    <!-- chart 1-->
    <div class="card card-banner card-chart card-green no-br">
      <div class="card-header">
        <div class="card-title">
          <div class="title">Water Consumption Chart - Paddy</div>
        </div>
        <ul class="card-action">
          <li>
            <a href="/">
              <i class="fa fa-refresh"></i>
            </a>
          </li>
        </ul>
      </div>
      <div class="card-body">
        <div class="ct-chart-sale2"></div>
      </div>
    </div>
  </div>
  <!-- chart 2-->
  <div class="col-xs-6">
    <div class="card card-banner card-chart card-green no-br">
      <div class="card-header">
        <div class="card-title">
          <div class="title">Water Consumption Chart - Tomato</div>
        </div>
        <ul class="card-action">
          <li>
            <a href="/">
              <i class="fa fa-refresh"></i>
            </a>
          </li>
        </ul>
      </div>
      <div class="card-body">
        <div class="ct-chart-sale"></div>
      </div>
    </div>
  </div>
</div>
<!-- tabs -->
<div class="col-md-12">
  <div class="card card-tab card-mini">
    <div class="card-header">
      <ul class="nav nav-tabs">
        <li role="tab1" class="active">
          <a href="#cropA" aria-controls="cropA" role="tab" data-toggle="tab">Paddy</a>
        </li>
        <li role="tab2">
          <a href="#cropB" aria-controls="cropB" role="tab" data-toggle="tab">Tomato</a>
        </li>
        <li role="tab3">
          <a href="form-backup.php" aria-controls="" role="" data-toggle=""><i class="icon fa fa-plus fa-2x"></i></a>
        </li>
      </ul>
    </div>
    <div class="card-body tab-content no-padding">
      <!-- tab 1 -->
      <div role="tabpanel" class="tab-pane active" id="cropA">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
              <a class="card card-banner card-green-light">
          <div class="card-body">
            <i class="icon fa fa-tachometer fa-4x"></i>
            <div class="content">
              <div class="title">Current Temp.</div>
              <div class="value"><span class="sign">&#8451;</span><?php echo $temp_val1['temperature']; ?></div>
              <!-- &#8451; says celcius -->
            </div>
          </div>
          </a>
          </div>
          <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
              <a class="card card-banner card-blue-light">
          <div class="card-body">
            <i class="icon fa fa-umbrella fa-4x"></i>
            <div class="content">
              <div class="title">Total Water Volume for the Week</div>
              <div class="value"><span class="sign">Ltrs.</span><?php echo $water_val1['waterlvl1']; ?></div>
            </div>
          </div>
        </a>

          </div>
          <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
              <a class="card card-banner card-yellow-light">
          <div class="card-body">
            <i class="icon fa fa-clock-o fa-4x"></i>
            <div class="content">
              <div class="title">Estimated Days to Crop to Harvest</div>
              <div class="value"><span class="sign">Days</span>12</div>
            </div>
          </div>
        </a>

          </div>
        </div>
      </div>
      <!-- tab 2 -->
      <div role="tabpanel" class="tab-pane" id="cropB">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
              <a class="card card-banner card-green-light">
          <div class="card-body">
            <i class="icon fa fa-tachometer fa-4x"></i>
            <div class="content">
              <div class="title">Current Temp.</div>
              <div class="value"><span class="sign">&#8451;</span><?php echo $temp_val2['temperature']; ?></div>
              <!-- &#8451; says celcius -->
            </div>
          </div>
          </a>
          </div>
          <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
              <a class="card card-banner card-blue-light">
          <div class="card-body">
            <i class="icon fa fa-umbrella fa-4x"></i>
            <div class="content">
              <div class="title">Total Water Volume for the Week</div>
              <div class="value"><span class="sign">Ltrs.</span><?php echo $water_val1['waterlvl1']; ?></div>
            </div>
          </div>
        </a>

          </div>
          <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
              <a class="card card-banner card-yellow-light">
          <div class="card-body">
            <i class="icon fa fa-clock-o fa-4x"></i>
            <div class="content">
              <div class="title">Estimated Days to Crop to Harvest</div>
              <div class="value"><span class="sign">Days</span>8</div>
            </div>
          </div>
        </a>

          </div>
        </div>
    </div>
  </div>
</div>
</br>

<!-- other stuff -->
<!-- <div class="row">
  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <div class="card card-mini">
      <div class="card-header">
        <div class="card-title">Last StatuSIS</div>
        <ul class="card-action">
          <li>
            <a href="/">
              <i class="fa fa-refresh"></i>
            </a>
          </li>
        </ul>
      </div>
      <div class="card-body no-padding table-responsive">
        <table class="table card-table">
          <thead>
            <tr>
              <th>Products</th>
              <th class="right">Amount</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>MicroSD 64Gb</td>
              <td class="right">12</td>
              <td><span class="badge badge-success badge-icon"><i class="fa fa-check" aria-hidden="true"></i><span>Complete</span></span></td>
            </tr>
            <tr>
              <td>MiniPC i5</td>
              <td class="right">5</td>
              <td><span class="badge badge-warning badge-icon"><i class="fa fa-clock-o" aria-hidden="true"></i><span>Pending</span></span></td>
            </tr>
            <tr>
              <td>Mountain Bike</td>
              <td class="right">1</td>
              <td><span class="badge badge-info badge-icon"><i class="fa fa-credit-card" aria-hidden="true"></i><span>Confirm Payment</span></span></td>
            </tr>
            <tr>
              <td>Notebook</td>
              <td class="right">10</td>
              <td><span class="badge badge-danger badge-icon"><i class="fa fa-times" aria-hidden="true"></i><span>Cancelled</span></span></td>
            </tr>
            <tr>
              <td>Raspberry Pi2</td>
              <td class="right">6</td>
              <td><span class="badge badge-primary badge-icon"><i class="fa fa-truck" aria-hidden="true"></i><span>Shipped</span></span></td>
            </tr>
            <tr>
              <td>Flashdrive 128Mb</td>
              <td class="right">40</td>
              <td><span class="badge badge-info badge-icon"><i class="fa fa-credit-card" aria-hidden="true"></i><span>Confirm Payment</span></span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <div class="card card-tab card-mini">
      <div class="card-header">
        <ul class="nav nav-tabs tab-stats">
          <li role="tab1" class="active">
            <a href="#tab1" aria-controls="tab1" role="tab" data-toggle="tab">Market details</a>
          </li>
          <li role="tab2">
            <a href="#tab2" aria-controls="tab2" role="tab" data-toggle="tab">Climate Foracast</a>
          </li>
          <li role="tab2">
            <a href="#tab3" aria-controls="tab3" role="tab" data-toggle="tab">Inquires</a>
          </li>
        </ul>
      </div>
      <div class="card-body tab-content">
        <div role="tabpanel" class="tab-pane active" id="tab1">
          <div class="row">
            <div class="col-sm-8">
              <div class="chart ct-chart-browser ct-perfect-fourth"></div>
            </div>
            <div class="col-sm-4">
              <ul class="chart-label">
                <li class="ct-label ct-series-a">Google Chrome</li>
                <li class="ct-label ct-series-b">Firefox</li>
                <li class="ct-label ct-series-c">Safari</li>
                <li class="ct-label ct-series-d">IE</li>
                <li class="ct-label ct-series-e">Opera</li>
              </ul>
            </div>
          </div>
        </div>
        <div role="tabpanel" class="tab-pane" id="tab2">
          <div class="row">
            <div class="col-sm-8">
              <div class="chart ct-chart-os ct-perfect-fourth"></div>
            </div>
            <div class="col-sm-4">
              <ul class="chart-label">
                <li class="ct-label ct-series-a">iOS</li>
                <li class="ct-label ct-series-b">Android</li>
                <li class="ct-label ct-series-c">Windows</li>
                <li class="ct-label ct-series-d">OSX</li>
                <li class="ct-label ct-series-e">Linux</li>
              </ul>
            </div>
          </div>
        </div>
        <div role="tabpanel" class="tab-pane" id="tab3">
        </div>
      </div>
    </div>
  </div>
</div> -->
  <footer class="app-footer">
  <div class="row">
    <div class="col-xs-12">
      <div class="footer-copyright">
        Copyright © 2017 <b>Team Void </b>
      </div>
    </div>
  </div>
</footer>
</div>

  </div>

    <?php include ('include/js.php'); ?>

</body>
</html>
