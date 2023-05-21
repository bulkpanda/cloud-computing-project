library(shiny)
library(leaflet)
library(plotly)

cities <- data.frame(
  city = c("Canberra", "Sydney", "Melbourne", "Brisbane", "Adelaide", "Perth", "Hobart", "Darwin"),
  state = c("ACT", "NSW", "VIC", "QLD", "SA", "WA", "TAS", "NT"),
  lat = c(-35.2809, -33.8688, -37.8136, -27.4698, -34.9285, -31.9505, -42.8821, -12.4628),
  lng = c(149.1300, 151.2093, 144.9631, 153.0251, 138.6007, 115.8605, 147.3272, 130.8417)
)

ui <- fluidPage(
  tags$style(HTML("
    .container {
      display: flex;
      flex-direction: column;
      height: calc(100vh - 70px);
    }
    .container1 {
      # background-image: url('b2.gif');
      background-size: cover;
      background-position: center;
      background-color: black;
      display: flex;
      flex-direction: column;
      height: calc(100vh - 70px);
      margin-left:-15px;
      margin-right:-15px;
    }
    .map-container {
      flex: 2;
      position: relative;
      margin-bottom: 20px;
      margin-left:-100px;
      margin-right:-100px;
    }
    .map {
      width: 100%;
      height: 100%;
    }
    .charts-container {
      flex: 1;
      display: flex;
    }
    .bargraph-container {
      width: 50%;
      position: relative;
      margin:0;
    }
    .bargraph {
      width: 100%;
      height: 100%;
    }
    .piechart-container {
      width: 50%;
      position: relative;
      margin:0;
    }
    .piechart {
      width: 100%;
      height: 100%;
    }
    .heading {
      background-color: rgb(0,167,250);
      color: white;
      padding: 10px;
      font-size: 20px;
      font-weight: bold;
      text-align: center;
      margin-bottom: 20px;
      margin-left:-160px;
      margin-right:-160px;
    }
    .heading1 {
      color: white;
      padding: 50px;
      font-size: 30px;
      font-weight: bold;
      text-align: center;
      margin-bottom: 50px;
      text-decoration: underline;
    }
    .heading2 {
      color: white;
      padding: 5px;
      font-size: 20px;
      font-weight: bold;
      text-align: center;
      margin-bottom: 5px;
      text-decoration: underline;
    }
    .text {
    color: white;
    padding 3px;
    font-size:20px;
    text-align:center;
    margin-bottom:1px;
    }
    .navbar-default .navbar-nav > li > a {
      color: white;
    }
    .navbar-default {
      background-color: #02025f;
      border-color: blue;
    }
    .navbar {
    margin-bottom:0;
    height:120%;
    }
    .input {
    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content:center;
    }
    .input-container {
    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content:center;
    margin-top:-10px;
    margin-bottom:10px;
    }
  ")),
  # img(src="logo.png",height = 25,width = 30)
  navbarPage(
    title = div(""),
    id = "navbar",
    tabPanel("Home",
             div(class ="container1",
                 div(class="heading1","COMP90024: Cluster and Cloud Computing"),
                 div(class="heading2","Assignment 2"),
                 div(class="heading2","Team 46"),
                 div(class="text",HTML("Kunal<br>
                     Mayank<br>
                     Sophie<br>
                     Harsh<br>
                     Maxson"))
             )
    ),
    tabPanel("Covid Analysis",
             div(class = "container",
                 div(class = "heading", "Covid Analysis"),
                 div(class = "map-container",
                     div(class = "map",
                         div(class = "input",
                             selectInput("stateSelect", "Select State", choices = unique(cities$state)),
                             selectInput("citySelect", "Select City", choices = NULL)
                         ),
                         div(class = "input-container",
                             actionButton("resetBtn", "Reset Map")
                         ),
                         leafletOutput("map")
                     )
                 ),
                 div(class = "charts-container",
                     div(class = "bargraph-container",
                         plotlyOutput("bargraph")
                     ),
                     div(class = "piechart-container",
                         plotlyOutput("piechart")
                     )
                 )
             )
    ),
    tabPanel("Crime Rates Analysis",
             div(class = "container",
                 div(class = "heading", "Crime Rates Analysis"),
                 div(class = "map-container",
                     div(class = "map",
                         div(class = "input",
                             selectInput("stateSelect2", "Select State", choices = unique(cities$state)),
                             selectInput("citySelect2", "Select City", choices = NULL)
                         ),
                         div(class = "input-container",
                             actionButton("resetBtn2", "Reset Map")
                         ),
                         leafletOutput("map2")
                     )
                 ),
                 div(class = "charts-container",
                     div(class = "bargraph-container",
                         plotlyOutput("bargraph2")
                     ),
                     div(class = "piechart-container",
                         plotlyOutput("piechart2")
                     )
                 )
             )
    ),
    tabPanel("Education Analysis",
             div(class = "container",
                 div(class = "heading", "Education Analysis"),
                 div(class = "map-container",
                     div(class = "map",
                         div(class = "input",
                             selectInput("stateSelect3", "Select State", choices = unique(cities$state)),
                             selectInput("citySelect3", "Select City", choices = NULL)
                         ),
                         div(class = "input-container",
                             actionButton("resetBtn3", "Reset Map")
                         ),
                         leafletOutput("map3")
                     )
                 ),
                 div(class = "charts-container",
                     div(class = "bargraph-container",
                         plotlyOutput("bargraph3")
                     ),
                     div(class = "piechart-container",
                         plotlyOutput("piechart3")
                     )
                 )
             )
    ),
  )
)


server <- function(input, output, session) {
  observeEvent(input$stateSelect, {
    cities_filtered <- cities[cities$state == input$stateSelect, ]
    updateSelectInput(session, "citySelect", choices = c("", cities_filtered$city))
  })
  
  output$map <- renderLeaflet({
    leaflet() %>%
      addProviderTiles("OpenStreetMap.Mapnik") %>%
      setView(lng = 133.7751, lat = -25.2744, zoom = 4) %>%
      addMarkers(
        data = cities,
        lng = ~lng,
        lat = ~lat,
        label = ~city,
        popup = ~city
      )
  })
  
  observe({
    if (input$stateSelect != "") {
      cities_filtered <- cities[cities$state == input$stateSelect, ]
      
      leafletProxy("map") %>%
        clearMarkers() %>%
        setView(lng = mean(cities_filtered$lng), lat = mean(cities_filtered$lat), zoom = 7) %>%
        addMarkers(
          data = cities_filtered,
          lng = ~lng,
          lat = ~lat,
          label = ~city,
          popup = ~city
        )
    }
  })
  
  observeEvent(input$citySelect, {
    if (input$citySelect != "") {
      selected_city <- cities[cities$city == input$citySelect, ]
      
      leafletProxy("map") %>%
        clearMarkers() %>%
        setView(lng = selected_city$lng, lat = selected_city$lat, zoom = 10) %>%
        addMarkers(
          data = selected_city,
          lng = ~lng,
          lat = ~lat,
          label = ~city,
          popup = ~city
        )
    }
  })
  
  observeEvent(input$resetBtn, {
    leafletProxy("map") %>%
      clearMarkers() %>%
      setView(lng = 133.7751, lat = -25.2744, zoom = 4) %>%
      addMarkers(
        data = cities,
        lng = ~lng,
        lat = ~lat,
        label = ~city,
        popup = ~city
      )
  })
  
  output$bargraph <- renderPlotly({
    data <- data.frame(
      Cities = c("Melbourne", "Sydney", "Adelaide", "Brisbane", "Darwin", "Hobart", "Canberra", "Perth"),
      Cases = c(20, 30, 15, 25, 15, 12, 19, 23)
    )
    
    plot_ly(data, x = ~Cities, y = ~Cases, type = "bar") %>%
      layout(title = "Bar Graph")
  })
  
  output$piechart <- renderPlotly({
    data <- data.frame(
      Cities = c("Melbourne", "Sydney", "Adelaide", "Brisbane", "Darwin", "Hobart", "Canberra", "Perth"),
      Cases = c(20, 30, 15, 25, 15, 12, 19, 23)
    )
    
    plot_ly(data, labels = ~Cities, values = ~Cases, type = "pie") %>%
      layout(title = "Pie Chart")
  })
  
  
  observeEvent(input$stateSelect2, {
    cities_filtered <- cities[cities$state == input$stateSelect2, ]
    updateSelectInput(session, "citySelect2", choices = c("", cities_filtered$city))
  })

  output$map2 <- renderLeaflet({
    leaflet() %>%
      addProviderTiles("OpenStreetMap.Mapnik") %>%
      setView(lng = 133.7751, lat = -25.2744, zoom = 4) %>%
      addMarkers(
        data = cities,
        lng = ~lng,
        lat = ~lat,
        label = ~city,
        popup = ~city
      )
  })

  observe({
    if (input$stateSelect2 != "") {
      cities_filtered <- cities[cities$state == input$stateSelect2, ]

      leafletProxy("map2") %>%
        clearMarkers() %>%
        setView(lng = mean(cities_filtered$lng), lat = mean(cities_filtered$lat), zoom = 7) %>%
        addMarkers(
          data = cities_filtered,
          lng = ~lng,
          lat = ~lat,
          label = ~city,
          popup = ~city
        )
    }
  })

  observeEvent(input$citySelect2, {
    if (input$citySelect2 != "") {
      selected_city <- cities[cities$city == input$citySelect2, ]

      leafletProxy("map2") %>%
        clearMarkers() %>%
        setView(lng = selected_city$lng, lat = selected_city$lat, zoom = 10) %>%
        addMarkers(
          data = selected_city,
          lng = ~lng,
          lat = ~lat,
          label = ~city,
          popup = ~city
        )
    }
  })

  observeEvent(input$resetBtn2, {
    leafletProxy("map2") %>%
      clearMarkers() %>%
      setView(lng = 133.7751, lat = -25.2744, zoom = 4) %>%
      addMarkers(
        data = cities,
        lng = ~lng,
        lat = ~lat,
        label = ~city,
        popup = ~city
      )
  })

  output$bargraph2 <- renderPlotly({
    data <- data.frame(
      Cities = c("Melbourne", "Sydney", "Adelaide", "Brisbane", "Darwin", "Hobart", "Canberra", "Perth"),
      Crimes = c(20, 30, 15, 25, 15, 12, 19, 23)
    )

    plot_ly(data, x = ~Cities, y = ~Crimes, type = "bar") %>%
      layout(title = "Bar Graph")
  })

  output$piechart2 <- renderPlotly({
    data <- data.frame(
      Cities = c("Melbourne", "Sydney", "Adelaide", "Brisbane", "Darwin", "Hobart", "Canberra", "Perth"),
      Crimes = c(20, 30, 15, 25, 15, 12, 19, 23)
    )

    plot_ly(data, labels = ~Cities, values = ~Crimes, type = "pie") %>%
      layout(title = "Pie Chart")
  })
  
  
  observeEvent(input$stateSelect3, {
    cities_filtered <- cities[cities$state == input$stateSelect3, ]
    updateSelectInput(session, "citySelect3", choices = c("", cities_filtered$city))
  })
  
  output$map3 <- renderLeaflet({
    leaflet() %>%
      addProviderTiles("OpenStreetMap.Mapnik") %>%
      setView(lng = 133.7751, lat = -25.2744, zoom = 4) %>%
      addMarkers(
        data = cities,
        lng = ~lng,
        lat = ~lat,
        label = ~city,
        popup = ~city
      )
  })
  
  observe({
    if (input$stateSelect3 != "") {
      cities_filtered <- cities[cities$state == input$stateSelect3, ]
      
      leafletProxy("map3") %>%
        clearMarkers() %>%
        setView(lng = mean(cities_filtered$lng), lat = mean(cities_filtered$lat), zoom = 7) %>%
        addMarkers(
          data = cities_filtered,
          lng = ~lng,
          lat = ~lat,
          label = ~city,
          popup = ~city
        )
    }
  })
  
  observeEvent(input$citySelect3, {
    if (input$citySelect3 != "") {
      selected_city <- cities[cities$city == input$citySelect3, ]
      
      leafletProxy("map3") %>%
        clearMarkers() %>%
        setView(lng = selected_city$lng, lat = selected_city$lat, zoom = 10) %>%
        addMarkers(
          data = selected_city,
          lng = ~lng,
          lat = ~lat,
          label = ~city,
          popup = ~city
        )
    }
  })
  
  observeEvent(input$resetBtn3, {
    leafletProxy("map3") %>%
      clearMarkers() %>%
      setView(lng = 133.7751, lat = -25.2744, zoom = 4) %>%
      addMarkers(
        data = cities,
        lng = ~lng,
        lat = ~lat,
        label = ~city,
        popup = ~city
      )
  })
  
  output$bargraph3 <- renderPlotly({
    data <- data.frame(
      Cities = c("Melbourne", "Sydney", "Adelaide", "Brisbane", "Darwin", "Hobart", "Canberra", "Perth"),
      Schools = c(20, 30, 15, 25, 15, 12, 19, 23)
    )
    
    plot_ly(data, x = ~Cities, y = ~Schools, type = "bar") %>%
      layout(title = "Bar Graph")
  })
  
  output$piechart3 <- renderPlotly({
    data <- data.frame(
      Cities = c("Melbourne", "Sydney", "Adelaide", "Brisbane", "Darwin", "Hobart", "Canberra", "Perth"),
      Schools = c(20, 30, 15, 25, 15, 12, 19, 23)
    )
    
    plot_ly(data, labels = ~Cities, values = ~Schools, type = "pie") %>%
      layout(title = "Pie Chart")
  })
}

shinyApp(ui, server)