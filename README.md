# BOOK MANAGER

[Visit the website here](https://flask-book-manager-f03e235c4fb6.herokuapp.com)

![screenshot](documentation/mockup.png)

This project was created as a web app application using Python, Flask framework, MongoDB non-relational database system and Heroku Cloud platform. It was made for educational purposes only.

The business goals for this website are:

1. To boost the Book Manager brand awareness and interact with its users
2. To achieve higher reachability and get more leads
3. To build database of users
4. To increase sales from new and returning customers

The user goals of this website are:

1. As a first-time visitor, I want to be able to register on the page, sign-in and add a book to the book manager
2. As a recurring or first-time visitor, I want to be able to find the books in the book manager and search through them, find the information about them and possibly buy them
3. As a recurring visitor, I want to be able to access the book I uploaded on the website and be able to delete or edit it
4. As an administrator, I should be able to manage categories of the books
5. As an administrator, I should be able to have access to the database

## UX

### **Strategy**

Considering the core UX principles, as first I started to think about the strategy for this website and defined who the target users would be and what features/technologies they would want.

Book Manager target users are:

* Aged 01-99
* Book lovers, anyone who loves to read and want to share it
* Would like to meet new people
* Would like to get inspired by others recommendations

What these users would be looking for:

* Clear information on how to follow through the website and easy-to-use navigation
* Good & simple-looking design which makes the website look desirable
* Possibility to register and share their ideas
* Possibility to search through books by author, book or category name
* Access to social media links to follow the news

This project has been built to offer all of these things. An effort was taken to provide as intuitive interaction as possible for every user visiting the webpage.

### **Scope**

To achieve the desired user and business goals, the following features will be included in this release:

* Simple 'Home' section with logo, navigation panel and information below, including footer with social media links as well
* 'Books' page where the user can search through the book manager by author, book or category name, and see already posted books by other members
* Every book contains information such as author name, book name, image, category, a brief book summary and which user posted it
* Every book includes button 'Buy Here' which will lead the user to Amazon marketplace where the book can be bought
* If the user has already registered, signed in and posted a book to the book manager, he can edit or delete it by clicking on the buttons located on the card of the book
* If the user has not yet been registered, he can do so in the 'Register' page
* The user can sign in to the book manager in the 'Sign In' page
* The user can sign out from the book manager clicking on the 'Sign Out' button in the navigation menu

### **Structure**

The app's Back End has been built using Python, especially routing and template method with Flask framework to be more flexible and less time wasting. All data are saved on MongoDB and fully accessible through the provided dashboard. Connection to database has been coded through Python. Passwords are put through hashing algorithm for basic security hygiene. Routing has also been used to create 404 and 500 response pages.

The website is made up of multiple pages which change accordingly to interaction of the user. After the first opening appears 'Home' page with navigation menu for: 'Home', 'Books', 'Sign In' and 'Register' pages. After logging in, a visitor can see 'Add Book' or 'Sign Out' as well. The navigation is always visible and accessible.

It's important to mention that I used Materialize for its design principles and grid system to make sure that responsiveness is on point.

A special user called 'admin' can access the categories and manage them after logging in. Only he can add, edit or delete any category. All the currently available categories are shown on the 'Home' page.

All important actions gives feedback to the user in form of Flash messages built on Python, for example after registration, adding a book or signin in.

### **Skeleton**

As this project is mostly about Back End and database connection with CRUD system, I decided to focus more on that part and kept design as simple as possible.

I intentionally used CSS styling to make interaction with this web apllication handy, for example with text styling, shadow and hovering effect on buttons, card designs or forms.

Last but not least, I worked on responsiveness to allow users using the book manager on different devices without any additional errors.

I felt that all mentioned above helps to provide the best User Experience and highlight the purpose of this project.

### Color Scheme

I chose a color palette based around white & black as these colors are elegant and simple to implement into the design. I added teal and beige color for buttons and headings. Additionally, I chose to use other colors for hover effects and box shadowing, but the main palette has been around these colors:

* `#000000` used for primary text or background
* `#ffffff` used for secondary text
* `#f9fbe7` used for primary highlights
* `#00838f` used for secondary highlights
* `#29b6f6` and `#e57373` used for buttons

I used [coolors.co](https://coolors.co/ffffff-000000-f9fbe7-00838f-29b6f6-e57373) to help me generate my color palette.

![screenshot](documentation/coolors.png)

The colors has been mainly used with the help of Materialize.

### Typography

I decided to use Google font 'Lato' with different font weights throughout the project thanks to its elegance. I left the font 'sans-serif' as a backup font style if anything goes wrong with the Google link. Secondly, I used Google font 'Skranji' for logo of the website and footer.

* [Lato](https://fonts.google.com/specimen/Lato)

* [Sans-serif](https://fonts.google.com/knowledge/glossary/sans_serif)

* [Skranji](https://fonts.google.com/specimen/Skranji)

## Features

Due to the wide age group of the users, it is assumed that most users will be viewing the site not only on their mobile phones but also on their tablets or computers. Therefore, creating something responsive is integral to the design.

### Existing Features

* **Home Page**

'Home Page' contains the navigation menu on the top with the logo, the information for the user to follow, and the footer which contains the social media links. Information for the user shows the steps to follow and the book categories which are currently available in the book manager - this part is connected to the database and can be updated by administrator. That means that any changes in categories can be seen here.

All of the next pages looks similar thanks to the Python template method.

![screenshot](documentation/home_page.png)

* **Books Page**

This page is the most important one of the whole project. It shows in order all the uploaded books to the database. The user can see image of the book, name of the book, category, author, short book summary and which user added it. There is an additional button provided which will lead the user to the Amazon Marketplace (with faketag).

![screenshot](documentation/books_page.png)

* **Search Bar on Books Page**
  
Almost on the top of the 'Books Page' is placed search bar which is meant to help people to search through by book, author or category name. In the example below, I tried to find the category name 'Novel' and it actually found me only these books that have this category name. This feature is helpful for anyone and useful when many books are added into the book manager.

![screenshot](documentation/novel.png)
![screenshot](documentation/novel_search_page.png)

* **Register Page**

On this page, user can simply register to our book manager by typing their username and password. All of the information will be shared to our database. As part of the deffensive programming, I chose to limit the required characters to 5-15 and added password to database is hashed using Python (Werkzeug) to add security.

![screenshot](documentation/register_page.png)

* **Sign In Page**

When user is already registered, he can sign in to our book manager using this page.

![screenshot](documentation/sign_in_page.png)

* **Add Book Page**

By clicking the 'Add New Book' button on the navigation panel, user will be redirected to this page where he can add the book to our book manager.

![screenshot](documentation/add_book_page.png)
![screenshot](documentation/added_book_by_user.png)

* **Edit Book Page**
![screenshot](documentation/edit_book_page.png)

* **Sign Out Page**
![screenshot](documentation/sign_in_page.png)

* **Manage Categories Page**
![screenshot](documentation/manage_categories_page.png)

* **Add Category Page**
![screenshot](documentation/add_category_page.png)

* **Edit Category Page**
![screenshot](documentation/edit_category_page.png)

* **404 Error Message**

When anything goes wrong with the links of the website, the 404 page pops up to make sure it leads the user to the 'Home Page' by clicking on the button. Alternatively, user can use the navigation panel to visit another part of tthe website.

![screenshot](documentation/404_page.png)

* **Flash Message**
![screenshot](documentation/flash_message.png)

* **Favicon**

As a rule of thumb, I added the Favicon which relates to the topic of the project.

![screenshot](documentation/favicon.png)

### Future Features
