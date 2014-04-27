{% load staticfiles %}

<html>
<h1>{{pageHeader}}</h1>
<body>
	
{% for event in recent_images %}
	<a href="{{event.image.get_image_file_loc}}">
		<img src="{{event.image.get_medium_image}}" />
	</a>
	
	<p>image title: {{event}}</p>
	<p>image path: {{ event.name }}</p>
	<p>Event Date: {{event.eDate}}</p>
	<p>tags: {{ event.tags_ }}</p>
	<p>Description: {{ event.description }}</p>
	<p>User: {{ event.user }}</p>
	<p>Attending: {{ event.attending_ }}</p>
	<ul>
		Image Properties
		<li>Medium fname : {{ event.image.get_medium_filename }}</li>
		<li>Image location : {{ event.image.get_image_file_loc }}</li>
		<li>Image dir: {{event.image.get_image_dir}}</li>
		<li>Image URL: {{event.image.get_image_url}}</li>
		<li>Image Path: {{event.image.get_image_path}}</li>

	</ul>
{% endfor %}

</body>

</html>
