#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#Author: Abhijit Jaiswal
#Date: 26th January 2018

library(shiny)
library(plotrix)
matches = read.csv("/Users/abhijitj/Downloads/ipl1/innings1.csv")  #Please replace this with actual path
#m = read.csv("/Users/abhijitj/Downloads/ipl/matches.csv")
m = read.csv("//Users/abhijitj/Downloads/ipl1/info2.csv")   #Please replace this with actual path
# Define UI for application that draws a histogram
ui <- fluidPage(
  titlePanel("IPL Historical Data"),
  sidebarLayout(position = "left",
                sidebarPanel("Selections: ",
                             selectInput(inputId = "year", label = "Season", 
                                         choices = unique(m$season)),
                             selectInput(inputId = "team1", label = "Team 1", 
                                         choices = ""),
                             selectInput(inputId = "team2", label = "Team 2", 
                                         choices = ""),
                             selectInput(inputId = "city", label = "City", 
                                         choices = ""),
                             radioButtons(inputId = "innings", label = "Select an innings",
                                          choices = c("1st innings", "2nd innings")),
                             sliderInput("over_range", "Over Range:",
                                         min = 0, max = 19,
                                         value = c(1,6)),
                             textInput(inputId = "matchid", label = "Match Id", value = ""),
                             selectInput(inputId = "bowler", label = "Choose a Bowler",
                                         choices = ""),
                             selectInput(inputId = "batsman", label = "Choose a Batsman",
                                         choices = "")),
                mainPanel("Output graphs",
                          fluidRow(
                            splitLayout(cellWidths = c("33%", "33%", "34%"), 
                                        plotOutput("plotgraph1"), 
                                        plotOutput("plotgraph2"), plotOutput("plotgraph3"))
                          ),
                          fluidRow(plotOutput("plt4"))
                )
                )
  )
# Define server logic required to draw a histogram
server <- function(session, input, output) {
  matches = read.csv("/Users/abhijitj/Downloads/ipl1/innings1.csv") #Please replace this with actual path
  #matches$
  observeEvent(input$select, updateSelectInput(session, "bowler", "Choose a bowler", 
               choices = unique(subset(matches, matches$match == input$select)$bowler)))
  observeEvent(input$year, updateSelectInput(session, "team1", "Team 1",
               choices = unique(subset(m, m$season == input$year)$team1)))
  observeEvent(input$year, updateSelectInput(session, "team2", "Team 2",
                choices = unique(subset(m, m$season == input$year)$team2)))
  observeEvent({input$team2
    input$team1  }, updateSelectInput(session, "city", "City", 
                 choices = unique(subset(m, m$season == input$year & 
                 ((m$team1 == input$team1 &
                  m$team2 == input$team2) |
                  (m$team1 == input$team2 &
                   m$team2 == input$team1) ))$city)))
  observeEvent({input$city
    input$team2
    input$team1}, updateTextInput(session, "matchid", "Match id", value = 
    as.character( ifelse(nrow(subset(m, m$season == input$year & (m$team1 == input$team1 &
    m$team2 == input$team2) & m$city == input$city)) == 0, subset(m, m$season == input$year & 
    (m$team1 == input$team2 & m$team2 == input$team1) & m$city == input$city)$match, 
    subset(m, m$season == input$year & (m$team1 == input$team1 &
    m$team2 == input$team2) & m$city == input$city)$match))
  ))
  'observeEvent({input$city
    input$team2
    input$team1}, updateSelectInput(session, "bowler", "Choose a bowler",
         choices = unique(subset(matches, matches$match == 
         ifelse(nrow(subset(m, m$season == input$year & (m$team1 == input$team1 &
         m$team2 == input$team2) & m$city == input$city)) == 0, subset(m, m$season == input$year & 
         (m$team1 == input$team2 & m$team2 == input$team1) & m$city == input$city)$match, 
         subset(m, m$season == input$year & (m$team1 == input$team1 &
         m$team2 == input$team2) & m$city == input$city)$match)
         )$bowler)))'
  
  observeEvent({input$city
    input$team2
    input$team1
    input$matchid}, updateSelectInput(session, "bowler", "Choose a Bowler",
    choices = unique(subset(matches, matches$match == input$matchid)$bowler))) 
  
  observeEvent({input$city
    input$team2
    input$team1
    input$matchid}, updateSelectInput(session, "batsman", "Choose a Batsman",
    choices = unique(subset(matches, matches$match == input$matchid)$batsman))) 
  
  output$plotgraph1 <- renderPlot({
    #mt <- subset(matches, matches$match == input$select)
    md <- subset(m, m$season == input$year & 
                   (m$team1 == input$team1 &
                      m$team2 == input$team2) | (m$team2 == input$team1 &
                      m$team1 == input$team2) & m$city == input$city)$match
    #print(md)
    mt <- subset(matches, matches$match == md)
    zeroes <- length(subset(mt, mt$runs_batsman == 0)$runs_batsman)
    ones <- length(subset(mt, mt$runs_batsman == 1)$runs_batsman)
    twos <- length(subset(mt, mt$runs_batsman == 2)$runs_batsman)
    threes <- length(subset(mt, mt$runs_batsman == 3)$runs_batsman)
    fours <- length(subset(mt, mt$runs_batsman == 4)$runs_batsman)
    fives <- length(subset(mt, mt$runs_batsman == 5)$runs_batsman)
    sixes <- length(subset(mt, mt$runs_batsman == 6)$runs_batsman)
    labs <- c("zeroes", "ones", "twos", "threes", "fours", "fives", "sixes")
    values <- c(zeroes, ones, twos, threes, fours, fives, sixes)
    temp <- c()
    temp_labs<- c()
    for(i in 1:length(values)){if(values[i] == 0){temp <- append(temp, values[i]); temp_labs <- append(temp_labs, labs[i])}}
    values <- values[!values %in% temp]
    labs <- labs[!labs %in% temp_labs]
    pie3D(values, radius = 0.9 , labels = labs, explode = 0.1, main="Overall Runs Distribution")
    #pie(values, labs, main="Runs Distribution", col = rainbow(length(values)))
    #legend("topright", labs, cex = 0.8,
    #       fill = rainbow(length(values)))
    #barplot(subset(matches, matches$match == input$select)$runs_batsman, col=rgb(0.2,0.4,0.6,0.6), border = "blue")
  })
  output$plotgraph2 <- renderPlot({
    #mt <- subset(matches, matches$match == input$select)
    #zeroes <- length(subset(mt, mt$runs_batsman == 0)$runs_batsman)
    #ones <- length(subset(mt, mt$runs_batsman == 1)$runs_batsman)
    #twos <- length(subset(mt, mt$runs_batsman == 2)$runs_batsman)
    #threes <- length(subset(mt, mt$runs_batsman == 3)$runs_batsman)
    #fours <- length(subset(mt, mt$runs_batsman == 4)$runs_batsman)
    #fives <- length(subset(mt, mt$runs_batsman == 5)$runs_batsman)
    #sixes <- length(subset(mt, mt$runs_batsman == 6)$runs_batsman)
    #labs <- c("zeroes", "ones", "twos", "threes", "fours", "fives", "sixes")
    #values <- c(zeroes, ones, twos, threes, fours, fives, sixes)
    #temp <- c()
    #temp_labs<- c()
    #for(i in 1:length(values)){if(values[i] == 0){temp <- append(temp, values[i]); temp_labs <- append(temp_labs, labs[i])}}
    #values <- values[!values %in% temp]
    #labs <- labs[!labs %in% temp_labs]
    #pie3D(values, radius = 0.9 , labels = labs, explode = 0.1, main="Runs Distribution")
    #pie(values, labs, main="Runs Distribution", col = rainbow(length(values)))
    #legend("topright", labs, cex = 0.8,
    #       fill = rainbow(length(values)))
    #barplot(subset(matches, matches$match == input$select)$runs_batsman, col=rgb(0.2,0.4,0.6,0.6), border = "blue")
    md <- subset(m, m$season == input$year & 
                   (m$team1 == input$team1 &
                      m$team2 == input$team2) | 
                   (m$team1 == input$team2 &
                      m$team2 == input$team1)
                 & m$city == input$city)$match
    mt_select = subset(matches, matches$match == md)
    bow = subset(mt_select, mt_select$bowler == input$bowler)
    print(subset(mt_select, mt_select$bowler == input$bowler)$runs_total)
    barplot(main="Runs given per delivery by Bowler", ylim=c(0, 7), subset(mt_select, mt_select$bowler == input$bowler)$runs_total, col=rgb(0.2,0.4,0.6,0.6), border = "blue")
  })
  output$plotgraph3 <- renderPlot({
    md <- subset(m, m$season == input$year & 
      (m$team1 == input$team1 &
       m$team2 == input$team2) | 
       (m$team1 == input$team2 &
       m$team2 == input$team1)
       & m$city == input$city)$match
    mt_select = subset(matches, matches$match == md)
    bow = subset(mt_select, mt_select$batsman == input$batsman)
    print(subset(mt_select, mt_select$batsman == input$bowler)$runs_batsman)
    barplot(main="Runs scored per delivery by batsman", ylim=c(0, 7), 
          subset(mt_select, mt_select$batsman == input$batsman)$runs_batsman, 
          col=rgb(0.2,0.4,0.6,0.6), border = "blue")
  })
  output$plt4 <- renderPlot({
    #print(input$over_range[1])
    #mor <- subset(matches, grepl(sprintf('^[%d-%d]\\.', 
    #            input$over_range[1],input$over_range[2]), matches$deliveries))
    mz = "mor"
    for(i in seq(input$over_range[1], input$over_range[2])){
      if(!exists(mz)){
      mor <- subset(matches, startsWith(as.character(matches$deliveries), sprintf('%d.', i)))}
      else{
        mor <- rbind(mor, subset(matches, startsWith(as.character(matches$deliveries), sprintf('%d.', i))))
      }
    }
    mor <- subset(mor, mor$match == input$matchid)
    mor <- subset(mor, mor$innings == input$innings)
    barplot(main = "Runs Scored in Over Range", 
            mor$runs_total, col=rgb(0.2,0.4,0.6,0.6), border = "blue")
  })
  
}

# Run the application 
shinyApp(ui = ui, server = server)

