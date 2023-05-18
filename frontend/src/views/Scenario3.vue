<template>
	<div id ="header"><h1>Scenario 3: Sentiments towards covid vaccines</h1> </div>
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
		const map = L.map('map').setView([-51.2744, 130.7751], 4);
  
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
  #header{
   background-color:  rgb(0, 167, 250);
   text-align: center;
   opacity: 60%;
   z-index: 999;
   position: absolute;
    width: fit-content;
    right: 15%;
    height: 10%;
    margin-top: 25px;
  }
  h1{
    color: azure;
    text-shadow: 2px 2px 5px blue;
    font-family: 'Fira Sans', sans-serif;
    font-family: 'Fira Sans Condensed', sans-serif;
    padding: 15px;
  }

  </style>
  