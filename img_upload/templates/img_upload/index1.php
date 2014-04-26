{% load staticfiles %}

<html>
<h1>Testing</h1>
<body>
	
{% for image in recent_images %}
	<img src="media/{{ image.image }}" />
	<p>Hi</p>
	<p>image: {{image}}</p>
	<p>image path: {{ image.image }}</p>
	<p>url {{ image.url }} {{ url }} </p>
	<p>recent images: {{recent_images.url}}</p>
{% endfor %}

</body>

</html>
