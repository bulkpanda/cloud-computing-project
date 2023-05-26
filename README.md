
### COMP90024 Project 2: Covid and Profanity tweets alongside toot analysis in Australia
# CCC Group 46 
Team Members:

Sophie Von Doussa - 1064884  <br>
Kunal Patel - 1291822 <br>
Mayank Yadav - 1403092  <br>
Harsh Mangla - 1418017 <br>
Maxson Mathew - 1428525 <br>

This is the Assignment 2 for COMP90024 (Cluster and Cloud Computing) from the University of Melbourne.

The	goal of this project is to develop a	Cloud-based	solution	that	exploits	virtual	machines	(VMs)	on the	UniMelb Research	Cloud	for	harvesting	and	processing	Mastodon	toots.	The	teams	should	produce	a	solution that	can	be	run	(in	principle)	across	any	node	of	 the	UniMelb Research	Cloud	 to	harvest	and	store	social	 media data and	 scale	 up/down	 as	 required with	 the	 data	 being	 harvested,	 processed	 and incorporated	into	the	existing (running) CouchDB	database.

For more details, please check the [project report](https://github.com/bulkpanda/cloud-computing-project/blob/master/Team_46_report.pdf).

### 1. The Architecture and Website Demo

In this project, six virtual machines (Ubuntu) were built on the [Nectar](https://nectar.org.au/) cloud platform, three of which deployed [CouchDB](http://couchdb.apache.org/) clusters, one with backup server, one deployed the mastodon harvesters using ansible for automated deployment and one deployed dashboard via R shiny. Collect toots from harvesters, store them into CouchDB, use the relevant Python libraries for sentiment and profanity analysis, and visualize the front end of the results.

#### 1.1. The Architecture**

<img src="https://github.com/bulkpanda/cloud-computing-project/blob/master/images/architecture.png" alt="architecture" width="50%">

#### 1.2. The Website Demo
<img src="https://github.com/bulkpanda/cloud-computing-project/blob/master/images/covid_analysis_page.png" alt="architecture" width="50%">
<img src="https://github.com/bulkpanda/cloud-computing-project/blob/master/images/profanity_analysis_page.png" alt="architecture" width="50%">
<img src="https://github.com/bulkpanda/cloud-computing-project/blob/master/images/mastodon_analysis_page.png" alt="architecture" width="50%">

### 2. Some Relevant Technology Stacks

* **WebServer** - webserver built by [Rshiny](https://www.rdocumentation.org/packages/shiny/versions/1.7.4)
* **Automation** - [Ansible playbook](https://www.ansible.com/)
* **Harvest** - Setting up mastodon harvesters
* **CouchDB** - [CouchDB](http://couchdb.apache.org/) cluster and [Map-Reduce](https://docs.couchdb.org/en/stable/ddocs/views/intro.html)
* **Data Analysis** - a _Python module_ [vaderSentiment](https://vadersentiment.readthedocs.io/en/latest/) for sentiment analysis
* **Data Visualization** - Plotly, leaflet, ggplot2
* **Website** - Based on R shiny.
