# Recipe-Workshop

[Recipe Workshop](http://recipeworkshop.herokuapp.com/) is an interactive and responsive website that allows users to create an account, browse recipes, upload and share their own cooking recipe creations.

The website has been built with CRUD functionality in mind and allows users access to Create recipes and accounts, Read recipes that have been uploaded, Update recipes and their account details, and Delete their recipes from the website.

I have created this website to cater to all users with an emphasis on those who are looking to either find a recipe to try out and bake or looking to share their latest creation with the world.

I have used HTML, CSS, [Bootstrap Framework](https://getbootstrap.com/), [jQuery](https://jquery.com/), Python, [Flask](https://palletsprojects.com/p/flask/), and [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) to build this project. This forms part of my ongoing portfolio of work.

![Preview of Recipe Workshop](https://res.cloudinary.com/andy-osborne/image/upload/v1594915079/Recipe_Workshop/Responsive_glyerl.png)

## Demo

A live demo of the website is hosted through Heroku and can be found [here](http://recipeworkshop.herokuapp.com/).

## __UX__

### User stories

As a user:

- I want the landing page of the website to be visually appealing to me as this sets my expectation for the rest of the website.

- I want to be able to see the most liked recipe on the landing page of the website so I am able to try this recipe out for myself.

- I want to be able to see recently added recipes on the landing page as these can give me inspiration of what I can search for, or even try them out myself.

- I want to be able to navigate myself around the site with ease and with as little guidance as necessary.

- I want the website to be responsive and adjust accordingly to the screen I am viewing it on.

- I want to be able to view and search for recipes that have been uploaded to the website.

- I want to be able to search for different recipes whether it is by name, ingredient or dish type.

- I want to be able to rate the recipes that I have tried so others know that the recipe is good and to share my appreciation with the author.

- I want to be able to create an account on the website which will allow me to edit recipes that I have created.

- I want to ensure that when I create an account, my password is only known to me and cannot be seen by the website admin.

- I want to be able to update my password or email address.

- I want to be able to upload my own recipes for other users to try.

- I want to be able to upload a picture for my recipe.

- I want to be able to manage my recipe, or even delete it from the website.

- I want to be able to create a profile page and upload an image of myself and an introduction for other users to see when they view my recipes.

## Design Choices

### Colours

- **Navbar** - I decided to use ``#6EBDC7``(Glacier) I chose this colour as it really stood on the site as the psychology from blue can imprint on visitors that of quality, wisdom, productivity and calmness. Whilst there are negative sides to blue depending on the shade used with food-related websites, I feel the shade used avoids.

- **Navbar and Primary User Interaction Buttons** - I decided to use ``#EA9C76``(Dark Salmon) as this not only stood out well against either a White or Glacier Blue background, it also complimented those colours and stood out to the user.

- **Font Colour** - I decided to use the default colour for the fonts as this suited the simple approach of a recipe website and I felt it didn't need to change.

- **Link Colours**
    1) For the links when in hover state I used ``#EA9C76``(Dark Salmon) as mentioned before, this colour really stood out without being to garish and complimented the overall site colour scheme.

    2) For the profile link from a recipe page, I used ``#947232``(Buttered Rum) for the standard colour as I felt that it complimented the sites overall colour scheme and it didn't contrast too heavily compared to the black text to instantly make the user lose focus on what they were reading.

### Fonts

- [**Averia Serif Libre**](https://fonts.google.com/specimen/Averia+Serif+Libre) - I used this font for the site headers as it reminded me of the typography you would see in recipe books which aids in helping the user feel at "home" on this recipe website.

- [**PT Sans**](https://fonts.google.com/specimen/PT+Sans) - I used this font for the text within modals as it had a great quirky feel to it that complimented Spicy Rice.

### Wireframes

- The wireframes for the initial layout of the website were created using [whimsical](https://whimsical.com/) and you can view the wireframes for Recipe Workshop [here](https://github.com/Andy-Osborne/Recipe-Workshop/tree/master/wireframes).

- The wireframes include a design layout for Desktop, as well as portrait and landscape designs for Tablet and Mobile.

## Technologies Used

1. [HTML](https://en.wikipedia.org/wiki/HTML) - This was used for the overall structure of the website.

2. [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This was used for the overall and bespoke styling of elements on the website.

3. [jQuery](https://jquery.com/)- This was used to create overall logic and interactivity of the website, including the use of Ajax for the account management options.

4. [Python](https://www.python.org/) - This was used for all the backend coding of the website.

5. [Flask](https://palletsprojects.com/p/flask/) - The flask microframework was used to aid in the construction of the website and its built-in tools like Jinja templating.

6. [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - This was used to connect to the NoSQL database, MongoDB.

7. [passlib.hash](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) - This was used for salting and hashing user passwords.

8. [MongoDB Atlas](https://www.mongodb.com/) - This was used as the NoSQL database that stores all user recipes, profiles, etc.

9. [Bootstrap Framework](https://getbootstrap.com/) - This was used to create the overall responsiveness of the website through the use of their flexible grid layout.

10. [Cloudinary](https://cloudinary.com/) - This was used to not only host the images used on the website but also allowed users to upload/delete their images through the use of their API.

11. [Google Fonts](https://fonts.google.com/) - I used Google Fonts to obtain the fonts used on the website which are "Averia Serif Libre" and "PT Sans".

12. [GitHub](https://github.com/) - I used to store my repository for the project and record all my commits.

13. [Heroku](https://www.heroku.com/) - I used Heroku to deploy the live version of my site.

14. [Autoprefixer](https://autoprefixer.github.io/) - I used this project to make sure all CSS prefixes were used where required to ensure cross-browser compatibility.

15. [Visual Studio Code](https://code.visualstudio.com/) - I used this to write the code for my site.
