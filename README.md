# Fabrizio's Project Portfolio 4
[Link for the IamResponsive]()
### Introduction

This README file is the collection and description of the features, decisions and funcionalities that are comprised in this project. It is divided into sections and sub-sections for easy reading. This file will cover everything from the inception of the project idea to the final steps of deployement and future features to be included.

## User Experience
### Strategy Plane

This project involves one of the most classic type of sofware/websites in today's market, a restaurant website. In particular this website is a mock website that includes many funcionalities. The idea behind this product is to create a platform for a high-end restaurant in a somewhat remote location. In addition to that the restaurant depicted has two main features: the use of seasonal and local supply and the development and employment of local personnel. Both of these decisions have been taken to highlight the underlying issue of "restoration of the native environment". This concept is based on the idea that the local supply of seasonal produce is the key to reduce the carbon footprint due to extensive farming and the cost and emissions of the logistics chain implied in the usual restaurant setting that we're all used to. Overall the Strategy was to create a platform that would invite users and then customers to the restaurant and also give them the possibility to discover the local cuisine rivisited using modern techniques and futuristic recipes. All in a environment conscious setting.

## Scope Plane

In order to obtain the result wanted for this product it was imperative that the deleopment process followed an Agile approach. Mostly because an Agile methodology would have allowed me to be more flexible with my schedule and with the objectives and features I wanted to develop. What I wanted to do with this website is to add enough features so that the users would be able to have an account on the webiste which would in return allow them to browse through all the reservations that they had made in the past. Based on previous experience and a small research conducted within the circle of people close to me I decided that another feature to add was the possibility of booking a table even WITHOUT having a profile on the website. This is because it has been found during the research that the majority of people usually don't dine at the same restaurant, even within the span of a couple of months. Hence the decision on having an unrestricted access to the reservations system even for random users. Some other necessary features born of the research on multiple other hogh end restaurants are a reference to the position of the location through the use of a map in a dedicated area of the website and a main page with detailed information on some key aspects of the restaurant like the menu, the main goal of the enterprise and and the chef leading the kitchen. 

## Structure Plane 

As a restaurant platform the development process for the structure was based on the possibility of letting the user decide to access all the content as a subscribed user of the website or as a simple visitor. The innformation is on the website is mostly text based and the navigation for the fucntionalities is guaranteed by various links. The main function of the structure is to eventually redirect the user the booking page, whether it be for the users or for the occasional guest. Once on the booking system the user is prompted to fill out the required data in the form necessary for the submission of the form. Once the information is sent the back-end takes care of the reservation storing it in the appropriate database. 

## Skeleton Plane

This plane is the one that most of all has been influenced by the standard practices of the conteporary environment. The navigation through the various pages is guaranteed by the many links present. Most of these links are placed in the navigation bar at the top of the page as to always allow a quick method to move through the functionalities. In the pages dedicated to the users' reservations the link added to access the "delete" and "update" functionalities are only accessible on that specific page as it would have been a poor user experience in my opinion to place them anywhere else. The footer constitutes an evergreen in terms of social engagement for a restaurant website. Through the links in the footer section it is possible to access the major social media platforms in order to let the user stay up to date with the latest news from the restaurant without having to rely to the classic and somewhat invasive newsletter. 

## Surface Plane 

The work on this particular plane had something different comapared to all the others. for this plane I decided to explore other Michelin starred restaurants' websites. I did this in order to get a better grasp of what a high end restaurant website looked like. What I discovered is that mainly these pages rely on simplicity and minimalism which I believe is somewhat linked to today's concept of modern cuisine. It is worthy of notice that many of these restaurants don't actually have a proprietary booking system and mainly rely on third parties' apps or simple email. This initial research has led me to develop a similar solution. In the website there are big images in the landing page, accompanied by some small, abstract text. I did this in order to create curiosity in the user and push themm to investigate the website further. The pages dedicated to the reservation system are intentionally kept simple since I want to let the user only focus on completing the reservation succesfully.


## Project Goal

The main objective for this project was to create a restaurant website that would serve as a platform for the potential customer to explore the story and the main offer of the kitchen. In addition to that I also felt that it would be profitable to highlight the history and culinary education of the lead chef in the kitchen. As additional features this project also offers the possibility of booking a table at the restaurant both as a website member and as a simple first time visitor. All the users registered to the website have also the chance to update or delete reservation made. 

### Target Audience

Clearly a restaurant as physical entity barely poses a limit when it comes to admittance. That being said, we must consider which type of customer a high end restaurant could attract. Usually these types of dining experiences are structured as to subtly invite a more sophisticated customer base. The typical michelin starred restaurant customer reserves a table knowing full well that they are preparing for a service and tasting event out of the ordinary. The cost factor is almost always present but it should necesseraliy constitute an entry barrier as there are many excellent kitchens around the world with prices that most if not any can afford. Given this initial information we need to take a step back and analize our customer base when it comes to traffic to the website. In this case the website doesn't initially filter any particular type of potential customer because everyone that can afford an internet connection can visit the website. The audience filtering will only begin once the guest will browse the website and most importantly the filtering will be passive as there are no pay-walls or subscription for the services provided by this project. Essentially the customer once they realize which type of offer this restaurant provides, are going to decide if they want to book a table or leave the page. Compared to other types of web pages, this method surely doesn't the best ROI in terms of traffic, but no high-end restaurant would make that a strategy. 

## Interactions and Features

### Future Features

Although the website fullfills the tasks required by a normal restaurant website there are some features and functionalities that could be included as add-ons, in particular:
- Adding a system that would send discounts to registered users
- Adding a Twitch live-stream of the kitchen (this is the reason behind the Twitch link in the footer)
- Adding a personalized and effectie newsletter service that would distinguish itself from all the other newsletter services 





tech used:
- cloudinary
- django allauth library
- django
- gunicorn
- elephantsql
- figma
- lucid chart
- postgresql
- django-datetime-picker
- Google Maps with the link from the share link in google maps