{% load staticfiles %}

<html>
<h1>Testing</h1>
<body>
	
{% for event in recent_images %}
	<img src="media/{{ event.image }}" />
	<p>image title: {{event}}</p>
	<p>image path: {{ event.image }}</p>
	<p>url: {{ event.url }} {{ url }} </p>
	<p>eDate: {{event.eDate}}</p>
	<p>tags: {{ event.tags_ }}</p>
	<p>Description: {{ event.description }}</p>
	<p>User: {{ event.user }}</p>
	<p>Attending: {{ event.attending_ }}</p>
	<p>Image prop: {{ event.image.get_medium_filename }}</p>
{% endfor %}

</body>

</html>
