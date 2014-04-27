{% load staticfiles %}
<!DOCTYPE html>
<html lang="en-US">
<head>
	<link rel="stylesheet" href="{% static "billboard/CSS/layout.css" %}" type="text/css" media="screen" charset="utf-8">
	<link rel="stylesheet" href="{% static "billboard/CSS/style.css" %}" type="text/css" media="screen" charset="utf-8">
	<link rel="stylesheet" href="{% static "billboard/CSS/elements.css" %}" type="text/css" media="screen" charset="utf-8">
	<title>My BC Billboard - Home</title>
</head>

<body>

<!-- redo with jQuery -->
<div id = "sidr" class="side-menu">
	<center><h1>Menu</h1></center>
	<ul>
		<li>Home</li>
		<li>Filters</li>
		<li>MyBC Evaluations</li>
		<li>Contact Us</li>
		<li>OPTION 5</li>
		<h1>Find Club</h1>
	</ul>
	<form>
		<input type="text" placeholder="Search..."
	</form>
</div>

<!-- BEGIN PAGE -->
<div id = "page-container">
	<!-- Top Menu -->
	<div id = "top-box">
		<div id = "nav-bar" class="centerInFrame">
			<!-- DO CLICK WITH jQuery to change image to pressed while down -->
			<a id = "side-menu" class="nav-item" href="#sidr"><div id = "menu-button" class="button"></div></a>
			<div class="nav-item logo">My BC Billboard</div>
			<a href="/admin"><div id="login-button" class="nav-item button"></div></a>
		</div>
		
	</div>
	
	<!-- Application -->
	<div id = "AppContainer" style="">

		<div class="Grid">
			<div id = "AppContentPad" class="centerInFrame varHeight">
				<div id="container" class="isoContain">
				
					<!-- BEGIN IMAGES -->
					{% for a in "123" %}
						{% for event in recent_images %}
						<div class="item {{event.image.get_image_dimensions}}">
							<a href="{{event.image.get_image_file_loc}}">
								<img src="{{event.image.get_medium_image}}" />
							</a>
						</div>
						{% endfor %}

					{% endfor %}
					<div class="item"><img src="http://www.wahoowire.com/wp-content/uploads/2011/11/lm5wm3c5s9lg0i1gvrfjiugdf1.gif"/></div>
					<div class="item w2 h2"><img src="http://2.bp.blogspot.com/-p4Ajeyc2wIw/T0cRaVpbLyI/AAAAAAAAAH4/2tVTzPjlVyc/s1600/dorm.JPG"/></div>
					<div class="item"><img src="https://www2.bc.edu/~ruddyka/%20Images/28_boston_college.jpg"/></div>
					<div class="item"><img src="http://poetsandquants.com/wp-content/uploads/2010/12/BostonCollege.jpg"/></div>
					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSvZKYhh5ZC6rvVqyaboCwsHscw6gr-wBMiHbgD5tifvnECzMS2"/></div>
					<div class="item h2"><img src="http://webbtrans.com/wp-content/uploads/brighton.jpg"/></div>
					<div class="item"><img src="http://cdn.lightgalleries.net/4bd5ec0a86209/images/landscaping_nb_07-2.jpg"/></div>
					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR9_s_RGV3uvo_yG_EOXtLPjxnFu7HZmnE-zUQm7AacRTSe2r_L"/></div>
					<div class="item"><img src="http://www.sentinellimo.com/Portals/162442/images/boston-college-limo.jpg"/></div>
					<div class="item h2"><img src="http://0.tqn.com/d/collegeapps/1/0/6/V/-/-/conte-forum-boston-college.jpg"/></div>
					<div class="item w2"><img src="http://kippywinston.files.wordpress.com/2011/12/bc-bapst-library.jpg"/></div>
					<div class="item"><img src="http://3.bp.blogspot.com/-CsaEWhWJBOk/TcN_ozjVHII/AAAAAAAAANo/_l2aOsNh0XU/s1600/Boston+College+Spring.JPG"/></div>
					<div class="item"><img src="http://www.wahoowire.com/wp-content/uploads/2011/11/lm5wm3c5s9lg0i1gvrfjiugdf1.gif"/></div>
					<div class="item w2 h2"><img src="http://2.bp.blogspot.com/-p4Ajeyc2wIw/T0cRaVpbLyI/AAAAAAAAAH4/2tVTzPjlVyc/s1600/dorm.JPG"/></div>
					<div class="item"><img src="https://www2.bc.edu/~ruddyka/%20Images/28_boston_college.jpg"/></div>
					<div class="item"><img src="http://poetsandquants.com/wp-content/uploads/2010/12/BostonCollege.jpg"/></div>
					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSvZKYhh5ZC6rvVqyaboCwsHscw6gr-wBMiHbgD5tifvnECzMS2"/></div>
					<div class="item h2"><img src="http://webbtrans.com/wp-content/uploads/brighton.jpg"/></div>
					<div class="item"><img src="http://cdn.lightgalleries.net/4bd5ec0a86209/images/landscaping_nb_07-2.jpg"/></div>
					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR9_s_RGV3uvo_yG_EOXtLPjxnFu7HZmnE-zUQm7AacRTSe2r_L"/></div>
					<div class="item"><img src="http://www.sentinellimo.com/Portals/162442/images/boston-college-limo.jpg"/></div>
					<div class="item h2"><img src="http://0.tqn.com/d/collegeapps/1/0/6/V/-/-/conte-forum-boston-college.jpg"/></div>
					<div class="item w2"><img src="http://kippywinston.files.wordpress.com/2011/12/bc-bapst-library.jpg"/></div>
					<div class="item"><img src="http://3.bp.blogspot.com/-CsaEWhWJBOk/TcN_ozjVHII/AAAAAAAAANo/_l2aOsNh0XU/s1600/Boston+College+Spring.JPG"/></div>
					<div class="item"><img src="http://www.wahoowire.com/wp-content/uploads/2011/11/lm5wm3c5s9lg0i1gvrfjiugdf1.gif"/></div>
					<div class="item w2 h2"><img src="http://2.bp.blogspot.com/-p4Ajeyc2wIw/T0cRaVpbLyI/AAAAAAAAAH4/2tVTzPjlVyc/s1600/dorm.JPG"/></div>
					<div class="item"><img src="https://www2.bc.edu/~ruddyka/%20Images/28_boston_college.jpg"/></div>
					<div class="item"><img src="http://poetsandquants.com/wp-content/uploads/2010/12/BostonCollege.jpg"/></div>
					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSvZKYhh5ZC6rvVqyaboCwsHscw6gr-wBMiHbgD5tifvnECzMS2"/></div>
					<div class="item h2"><img src="http://webbtrans.com/wp-content/uploads/brighton.jpg"/></div>
					<div class="item"><img src="http://cdn.lightgalleries.net/4bd5ec0a86209/images/landscaping_nb_07-2.jpg"/></div>
					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR9_s_RGV3uvo_yG_EOXtLPjxnFu7HZmnE-zUQm7AacRTSe2r_L"/></div>
					<div class="item"><img src="http://www.sentinellimo.com/Portals/162442/images/boston-college-limo.jpg"/></div>
					<div class="item h2"><img src="http://0.tqn.com/d/collegeapps/1/0/6/V/-/-/conte-forum-boston-college.jpg"/></div>
					<div class="item w2"><img src="http://kippywinston.files.wordpress.com/2011/12/bc-bapst-library.jpg"/></div>
					<div class="item"><img src="http://3.bp.blogspot.com/-CsaEWhWJBOk/TcN_ozjVHII/AAAAAAAAANo/_l2aOsNh0XU/s1600/Boston+College+Spring.JPG"/></div>
					<div class="item"><img src="http://www.wahoowire.com/wp-content/uploads/2011/11/lm5wm3c5s9lg0i1gvrfjiugdf1.gif"/></div>
					<div class="item w2 h2"><img src="http://2.bp.blogspot.com/-p4Ajeyc2wIw/T0cRaVpbLyI/AAAAAAAAAH4/2tVTzPjlVyc/s1600/dorm.JPG"/></div>
					<div class="item"><img src="https://www2.bc.edu/~ruddyka/%20Images/28_boston_college.jpg"/></div>
					<div class="item"><img src="http://poetsandquants.com/wp-content/uploads/2010/12/BostonCollege.jpg"/></div>
<!-- 					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSvZKYhh5ZC6rvVqyaboCwsHscw6gr-wBMiHbgD5tifvnECzMS2"/></div>
					<div class="item h2"><img src="http://webbtrans.com/wp-content/uploads/brighton.jpg"/></div>
					<div class="item"><img src="http://cdn.lightgalleries.net/4bd5ec0a86209/images/landscaping_nb_07-2.jpg"/></div>
					<div class="item w2"><img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR9_s_RGV3uvo_yG_EOXtLPjxnFu7HZmnE-zUQm7AacRTSe2r_L"/></div>
					<div class="item"><img src="http://www.sentinellimo.com/Portals/162442/images/boston-college-limo.jpg"/></div>
					<div class="item h2"><img src="http://0.tqn.com/d/collegeapps/1/0/6/V/-/-/conte-forum-boston-college.jpg"/></div>
					<div class="item w2"><img src="http://kippywinston.files.wordpress.com/2011/12/bc-bapst-library.jpg"/></div>
					<div class="item"><img src="http://3.bp.blogspot.com/-CsaEWhWJBOk/TcN_ozjVHII/AAAAAAAAANo/_l2aOsNh0XU/s1600/Boston+College+Spring.JPG"/></div> -->
					<!-- END IMAGES -->
					
				</div>
				<!--{#  Django Code goes here! #}-->
			</div>
		</div>	
	</div>
</div>

<script type="text/javascript" src = "{% static "billboard/js/jquery-2.1.0.js" %}"></script>
<script type="text/javascript" src = "{% static "billboard/js/jquery-ui-1.10.4.js" %}"></script>
<script type="text/javascript" src = "{% static "billboard/js/isotope.pkgd.min.js" %}"></script>
<script src="{% static "billboard/js/isoAction.js" %}"></script>
<script src="{% static "billboard/js/jquery.sidr.min.js" %}"></script>
<script type="text/javascript">
$(document).ready(function() {
  $('#side-menu').sidr();
});


</script>
</body>
</html>