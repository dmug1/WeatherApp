from django.shortcuts import render


def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=380EB5C4-750F-4897-B7BA-DC8DDD241D5A")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."


	return render(request, 'home.html', {'api': api} )
	

def about(request):
	return render(request, 'about.html', {})

