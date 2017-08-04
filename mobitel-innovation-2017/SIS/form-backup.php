<!DOCTYPE html>
<html>
<head>
  <title>Smart Irrigation System</title>

  <meta name="viewport" content="width=device-width, initial-scale=1">

  <?php include('include/css.php'); ?>

</head>
<body>
  <div class="app app-default">

  <?php include('include/nav.php'); ?>

<script type="text/ng-template" id="sidebar-dropdown.tpl.html">
  <div class="dropdown-background">
    <div class="bg"></div>
  </div>
  <div class="dropdown-container">
    {{list}}
  </div>
</script>
<div class="app-container">

  <?php include('include/nav-mobile.php'); ?>

  <div class="row">
  <div class="col-md-12">
    <div class="card">
      <div class="card-header">
        Add Crop
      </div>
      <div class="card-body">
        <form class="form form-horizontal">
  <div class="section">
    <div class="section-title">Information</div>
    <div class="section-body">
      <div class="form-group">
        <label class="col-md-3 control-label">Crop Name</label>
        <div class="col-md-9">
          <input type="text" class="form-control" placeholder="">
        </div>
      </div>
      <div class="form-group">
        <label class="col-md-3 control-label">Crop ID</label>
        <div class="col-md-9">
          <input type="text" class="form-control" placeholder="">
        </div>
      </div>
      <div class="form-group">
        <label class="col-md-3 control-label">Crop Type</label>
        <div class="col-md-9">
          <div class="input-group">
            <select class="select2">
              <option value="Paddy">Paddy</option>
              <option value="Pumpkin">Pumpkin</option>
              <option value="Potato">Potato</option>
              <option value="Tomato">Tomato</option>
            </select>
            <span class="input-group-addon">Crop</span>
          </div>
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-3">
          <label class="control-label">Price</label>
          <p class="control-label-help">( Per Squre Feet )</p>
        </div>
        <div class="col-md-9">
          <div class="input-group">
            <span class="input-group-addon">$</span>
            <input type="number" class="form-control" aria-label="Amount (to the nearest dollar)">
          </div>
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-3">
          <label class="control-label">Description</label>
          <p class="control-label-help">( short detail of the crop )</p>
        </div>
        <div class="col-md-9">
          <textarea class="form-control"></textarea>
        </div>
      </div>
      <div class="form-group">
        <label class="col-md-3 control-label">Crop Area</label>
        <div class="col-md-9">
          <div class="input-group">
            <input type="number" class="form-control" placeholder="">
            <span class="input-group-addon">Sq. Feets</span>
          </div>
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-3">
          <label class="control-label">Location</label>
          <p class="control-label-help">( Input the standard city name )</p>
        </div>
        <div class="col-md-9">
          <input type="text" class="form-control" placeholder="">
        </div>
      </div>
    </div>
  </div>
  <div class="form-footer">
    <div class="form-group">
      <div class="col-md-9 col-md-offset-3">
        <button type="submit" class="btn btn-primary">Add Crop</button>
        <button type="button" class="btn btn-default">index.html</button>
      </div>
    </div>
  </div>
</form>
        </div>
      </div>
    </div>
  </div>
</div>

  </div>

  <?php include('include/js.php'); ?>

</body>
</html>
