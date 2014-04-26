{% load staticfiles %}

<html>
<h1>Testing</h1>
<body>
	
{% for image in recent_images %}
	<img src="{{ image.url }}" />
{% endfor %}

</body>

</html>
