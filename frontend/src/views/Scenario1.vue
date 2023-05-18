<template>
	<div id="map" style="height: 400px;"></div>
  </template>
  
<script>
  import 'leaflet/dist/leaflet.css';
  import L from 'leaflet';
  
  export default {
	mounted() {
	  this.initializeMap();
	},
	methods: {
	  initializeMap() {
		// Create the map instance
		const map = L.map('map').setView([-56.2744, 250.7751], 4);
  
		// Add the tile layer (map tiles)
		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		  attribution: '&copy; OpenStreetMap contributors'
		}).addTo(map);
  
		// Add a marker at the center of Australia
		L.marker([-25.2744, 133.7751]).addTo(map);
	  }
	}
  };
  </script>
  
  <style>
  #map {
	width: 100%;
	padding-top: 100rem;
  }
  </style>
  