# Get My Tattoo


For the third Milestone Project I decided to design a website where tattoo artists can register and add their profile to a database. Users (customers) can then search the database without registering and find their ideal tattoo artist.
I had this idea since it not easy to find a tattoo artist that does exactly what we want. It is a research that might take a considerable amount of time, and people nowadays have always less free time. People need to find information easily and fast.
The structure of the website is divided into two: one area is visible to all users, and one area is visible only to registered users.

View the live project here. [Get My Tattoo](https://getmytattoo.herokuapp.com/get_artists)


### Base Page

The base page has elements that all the pages have in common, which are a sticky navbar with collapsible toggler and a search box, plus a footer.

### Home Page

The home page welcomes the users and explains briefly what the website is about.
Then a section with four cards shows some tattoo styles to inspire users, but also to guide them through the navigation. Many times users don’t have a clear idea in mind and need a guidance to help them starting the navigation.
Right after this section I repeated the search box, and an area with the last tattoo artists that added or updated their profile.
All users can access this page and search freely the database.


### Search Page


The search page displays  the results of the user's research.

For each result there is a row with a profile picture of the tattoo artist (on the left), an information section (on the center) displaying the name of the artist and his/her biography, and a carousel (on the right) with three pictures of the artists’s tattoos.
In this way the user can understand in a glance if the tattoo artist might be of interest, or not. 
In case the user wants to know more about one tattoo artist, there is a link at the bottom of the central information section that leads directly to the artist page.


### Show Styles


### Show Artist Page

This page displays all the information about a single artist.
Here users cand find the address, the contact area, information about the languages that the artist speaks, the style he/she has, and a gallery with up to six images showing some of the best work of art the artist made.
A bottom at the end of the page takes the user back to the home page. 


### Register - if the user is a tattoo artist

The register page has a image on the background of a bearded tattooed man that looks in the direction of the form.
The form has two fields: username (that accept letters from the Latin alphabet and numbers) and password (with a length between 5 and 20 char).
A small text under the section has a link to the log in page for those users that already have an account.


### Log In - only for tattoo artists

This page repeats the same structure of the register page.
If a user writes a wrong username or a wrong password, a message tells that there is some mistake.


### Add profile - only for tattoo artists

This page is visible only after a user registered his/her profile and is not available from the menu.
That because a user is allowed to have only one profile.

A form with all the fields needed is shown. Here the tattoo artist can add:
* name
* address
* city
* state
* profile picture (url)
* phone number
* email
* link to Facebook
* link to Instagram
* languages spoken
* tattoo style
* up to six images (url)

A button let the user save the profile.


### Edit profile - only for tattoo artists

This page takes the same layout of the “Add profile”, but instead of having empty fields it shows the values that the user already added before.
Clicking on the fields, the user can delete the content and type something new.
At the bottom of the page there are two buttons: one allows the user to save the changes, the other one allows to cancel the changes without saving.


### Delete profile - only for tattoo artists

This page allows the tattoo artist to delete his/her profile.
However, to prevent unintentional deleting, I added an extra step. 
The page asks for a confirmation: if the user really wants to delete the profile, then a button cancel the profile and takes the user back to the general home page.
If the user changes his/her mind and wants to go back, a button guide him/her to the profile page.

### My profile - only for tattoo artists

This page shows the artist’s page with the information that he/she provided.
A button allows to edit the profile (linking to the “Edit profile” page, and one button to delete it (linking as I mentioned before to the “Delete” page.


---

## User Experience (UX)


* **Strategy Plane**

The website should help tattoo artists getting in touch with new customers.
It should be a window for artists to show their abilities, and at the same time allows users to find their ideal tattoo.

When a person is looking for a new tattoo, he/she wants to find a person that is able to transform the idea into a permanent design. Not all tattoo artists do the same things, they are always specialized in some particular styles. 

Moreover, it is always better when customer and artist speak the same language. They can communicate properly and share ideas, feelings, etc.
We live in a world where immigration is a common thing, we have around people coming from all over the world and language is not always the same (or at the same level). This is something that I experienced directly, as an Italian living in Sweden.
Also, we live in a society where it is easy to move from one city to another, but also from one country to another: it happens often that customers are willing to travel just to have the tattoo done by a specific person. 

There are two big websites that have a great database for tattoo artists: [Tattodoo](https://www.tattoodo.com/) and [Inkstinct](https://inkstinct.co/). They have very rich search options, but they are missing the language thing and they are too confusing. They don’t go straight to the point as my website wants to do.

According to an article appeared on [Medium](https://medium.com/daliaresearch/who-has-the-most-tattoos-its-not-who-you-d-expect-1d5ffff660f8), the average person nowadays that has tattoo is a person with high education, with a good income, that lives in a urban area.
The idea of the tattooed person which is an “outsider” is no more actual and I think that the design of the website should reflect this aspect. It should be intuitive, modern and with a strong personality.
That also should convey an idea of credibility and reliability.
The user (customer) can contact the tattoo artist in many ways: with a phone call, with an email, connecting through Facebook or Instagram.


* **Scope Plane**

It is very important that the tattoo artist can have his/her own virtual window as a showcase of his/her job.
To have the maximum focus on the artist it is of fundamental importance that every single artist has his/her own page with no distractions around.
Links that allow connections between artist and customer are also of fundamental importance.
To help the tattoo artist editing and updating the profile anytime, there must be a functionality to do it independently.
Also, to keep the informations on the website consistent for all the tattoo artists, it should not be allowed for a tattoo artist to add extra fields. In this way, everyone has equal instruments to reach and attract customers.


* **Structure Plane**

The sticky navbar allows users to navigate easily on the website without going back and forth wasting time.
The search bar, fundamental feature, is placed on the navbar and is also repeated on the home page.
All the buttons have a glowing effect on hover, to add focus and attract the user.
A smooth scrolling effect add some extra class and modernity.


* **Skeleton Plane**



* **Surface Plane**



### User stories

#### First Time Visitor Goals


#### Returning Visitor Goals

#### Frequent User Goals


### Design



### Colour Scheme



### Typography



### Imagery


### Wireframes



### Features



### Features to implement


---

## Technologies Used

### Languages Used
* HTML5
* CSS3
* Javascript

### Frameworks, Libraries & Programs Used

* Bootstrap 4.5.0.
* Google Fonts
* Font Awesome 4.7.0.
* Git
* GitHub
* GitPod
* Heroku
* Chrome DevTools
* Favicon.ico

---

## Testing

### Functionality Testing 



### Usability Testing


#### First Time Visitor Testing


#### Returning Visitor Testing


#### Frequent User Testing

### Compatibility Testing


### Performance Testing




### Bugs



---

## Deployment




---

## Credits

### Code


### Media



### Acknowledgements

