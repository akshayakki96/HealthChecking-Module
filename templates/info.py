INFORMATION_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
    /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
    .row.content {height: 550px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      background-color: #f1f1f1;
      height: 1000px;
    }
        
    /* On small screens, set height to 'auto' for the grid */
    @media screen and (max-width: 767px) {
      .row.content {height: auto;} 
    }
  </style>
</head>
<body>

<nav class="navbar navbar-inverse visible-xs">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#">CLARITY</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Dashboard</a></li>
        
      </ul>
    </div>
  </div>
</nav>

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav hidden-xs">
      <h2>CLARITY</h2>
      <ul class="nav nav-pills nav-stacked">
        <li class="active"><a href="#section1">Dashboard</a></li>
      </ul><br>
    </div>
    <br>
    
    <div class="col-sm-9">
      <div class="well">
        <h4>Service</h4>
        <p>Query Engine</p>
      </div>
      <div class="row">
        <div class="col-sm-3">
          <div class="well">
            <h4>Docker Image</h4>
            <p>3b6def36e987-develop-117</p> 
          </div>
        </div>
        <div class="col-sm-3">
          <div class="well">
            <h4>Requests</h4>
            <p>100 Million</p> 
          </div>
        </div>
        <div class="col-sm-3">
          <div class="well">
            <h4>Sessions</h4>
            <p>10 Million</p> 
          </div>
        </div>
        <div class="col-sm-3">
          <div class="well">
            <h4>Bounce</h4>
            <p>30%</p> 
          </div>
        </div>
      </div>
      <div class="row">
        
        <div class="col-sm-4">
          
        </div>
      </div>
      <div class="row">
        
      </div>
    </div>
  </div>
</div>

</body>
</html>

"""

health_check_template = """
<html>
<head>
<style>
table { 
border-collapse: collapse; 
width: 99%;
}
table, td, th { 
border: 2px solid black;
}
td,th{
width: 70px;
height: 70px;
}
td a{
display:block;
width:100%;
height:100%;
}
body {
background-image: url("http://wallpapercave.com/wp/EfV6fGy.jpg");} 
</style>
</head>
<body>
<h1><CENTER><u> SERVICE ANALYZER </u></CENTER></h1>
<marquee>The following table checks the status of the services being provided to each server :</marquee>
<br><br><br><br>
<table align="center">
<tr>
%for j in data['columns']:
<th>{{data['columns'][j]}}</th>
% end
</tr>
 %for i in data['servers']:
 <tr>
 %for j in data['columns'] :
 %if j=="0":
 <td align="center">{{data['servers'][i][j]}}</td>
 %else:
 <td bgcolor="{{data['servers'][i][j]}}"><a href="./info"></a></td> 
 % end
 %end
</tr> 
%end
</table>
</body>
</html>

"""
