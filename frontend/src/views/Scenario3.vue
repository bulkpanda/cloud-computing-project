<template>
  
  
    <div id="map" style="height: 400px;"></div>
    <div id="header">
      <h1>Scenario 3: Happiness index</h1> </div><br>
      <div id="dropdown">
      <h2>Select City: {{ selectedCity }}</h2>
      <select v-model="selectedCity" @change="zoomToCity">
        <option value="">Select a city</option>
        <option v-for="city in cities" :value="city.label" :key="city.label">{{ city.label }}</option>
      </select>
    
   
  </div>
    
    
    
  
</template>

<script>
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

export default {
  data() {
    return {
      selectedCity: '',
      cities: [
        { label: 'Melbourne', coordinates: [-37.875, 144.9631] },
        { label: 'Sydney', coordinates: [-33.8798, 150.987] },
        { label: 'Brisbane', coordinates: [-27.5698, 153.0251] },
      ],
      map: null,
    };
  },
  mounted() {
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      // Create the map instance
      this.map = L.map('map').setView([-51.2744, 133.7751], 4);

      // Add the tile layer (map tiles)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
      }).addTo(this.map);
    },
    zoomToCity() {
      const selectedCity = this.cities.find(city => city.label === this.selectedCity);
      if (selectedCity) {
        this.map.flyTo(selectedCity.coordinates, 13); // Zoom to selected city coordinates
      }
    },
  },
};
</script>

<style>
#map {
  width: 100%;
  padding-top: 100rem;
}

#header {
  background-color:  rgb(0, 167, 250);
   text-align: center;
   opacity: 70%;
   z-index: 999;
   position: absolute;
    width: fit-content;
    left: 20%;
    height: 10%;
    margin-top: 10px;
}

h1 {
  color: azure;
  text-shadow: 2px 2px 5px blue;
  font-family: 'Fira Sans', sans-serif;
  font-family: 'Fira Sans Condensed', sans-serif;
  padding: 15px;
  margin: 0;
}

h2 {
  color: azure;
  text-shadow: 2px 2px 5px blue;
  font-family: 'Fira Sans', sans-serif;
  font-family: 'Fira Sans Condensed', sans-serif;
  padding: 15px;
  margin: 0;
}

#dropdown {
  background-color:  rgb(0, 167, 250);
   text-align: center;
   opacity: 60%;
   z-index: 999;
   position: absolute;
    width: fit-content;
    right: 15%;
    height: 10%;
    margin-top: 20px;
}
</style>
