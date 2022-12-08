# README - MENUETTE

## Team Information

- Chapin Alf
- Katelyn Donn
- Madeline Gilman
- Tyler Knohl

## Project Pitch 

Menuette is a restaurant review platform that focuses on menu-specific restaurant reviews and foodie communities. 
The app caters to food bloggers, restaurant owners, and everyday searchers. Through the app, 
users can filter through restaurants by their specific cravings and allergens to
find menu items that suit their needs. Users are also able to join communities that allow them to discuss their food
limitations, restaurant recommendations, and menu items. Restaurant owners within the app can promote their restaurant
with ads and engage with customers. Lastly, bloggers can explore new restaurants and write reviews on the restaurants
they visit.

## Project Overview

Menuette was designed for three different users, the restaurant owner, searcher, and blogger. 
Each of our users have their own routes from our database that corresponds to their pages in AppSmith. 
In order to connect our users with our app, we ran docker containers which create specific paths 
where user data goes to then be posted to AppSmith using Ngrok.

## Video Overview
https://drive.google.com/file/d/1brRFZxGpdbmN4P7buVN-bISn0yI6Bq7t/view?usp=share_link

## How to Run

1. Start docker and run the following commands in terminal:
2. docker compose build 
3. docker compose up 
4.  Once the containers are up, run the following command in a new terminal window
5. ngrok http 8001 
6. Open the AppSmith Menuete project and edit the "Main Datasource" with your generated ngrok link 
7. Deploy the application (https://appsmith.cs3200.net/app/menuette/home-6384f07cffea3148102aa7a8)


