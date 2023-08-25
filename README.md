![screenshot of the site on different devices](/assets/images/memory-amiresponsive.png)
# Ganaga|Travel 
## Your personal travel planner, create an adventure and add destinations with information for your travel party to share!

In Ganga Travel you can create adventures and plan them by creating destinations within your adventures and commenting on the content.
Users can create, modify and delete content to which they are authorized.

### Adventures/home.
![screenshot of Modal screen](/assets/images/memory-modal.png)
On the adventure page, which is the home page, the user is met by a header, page content and a footer.
<br>
The content of the page consists of various cards with images which are then partially covered by text and buttons.
<br>
The purpose of the image is to be a teaser image and not show too much, the text explains the title of the adventure (which also acts as a link to the next page), who created it, the date and the two buttons represent edit and delete.
<br>
At the bottom there is a button to be able to add a new adventure, these three buttons are only visible to the user who is authorized to use these functions.

### Add Adventure.
![screenshot of the play-ground](/assets/images/memory-playground.png)
The user clicks on New Adventure and is welcomed by a form where the user must fill in the name of the adventure, the date and possibly choose a picture. if no image is selected, a default image is used instead. When the user is finished, he or she presses the send button and is sent back to the homepage.

### Edit Adventure.
![Screenshot of No match text](/assets/images/memory-nomatch-playertext.png)<br>
![Screenshot of You got a match text](/assets/images/memory-yougotamatch-playertext.png)<br>
![Screenshot of all cards match text](/assets/images/memory-allcardsmatch-playertext.png)<br>

If the user presses Edit, the user is greeted by a form, it is already filled in, but the user can delete or add text or an image. When the user is satisfied with the changes, he or she presses send and is sent back to the homepage.

### Delete Adventure.
![Screenshot of the footer with flip counter and timer](/assets/images/memory-footer.png)
If the user presses Delete, a pop-up window appears asking the user if they want to delete this adventure, if the user presses yes, the adventure is deleted, if the user presses no, the process is canceled.

### Destinations.
When the user has pressed one of the titles on the adventure page, they are welcomed by the destination page. Here you can see the title of the adventure so that the user does not forget which one they are in.
The different destinations are presented in different cards with an image, title, text box, when it was created, when it was last updated and two buttons for edit and delete.
<br>
Here I have chosen to use large and complete images because I want users to be able to see these images and really feel excitement and longing for the trip they are going to take with their friends or family.
<br>
Further down the page is the comment section, they are sorted from oldest to newest to create a conversation and it shows which user has written the comment. Users can delete comments, but only those that you have written yourself. And at the bottom there is a button to add new destinations. All buttons are only visible to users who are authorized to use these functions.

### Add Destination.
If the user clicks on a new destination, a pop-up window appears at the bottom of the destination page.
<br>
This form is already filled in and the user can add or remove title, text or image, the user then presses send and the box closes down. Should the user regret it, the form will be closed if the user presses anywhere outside the box.

### Edit Destination.
When the user has pressed edit, a form is displayed that has already been filled in, here you can change the title, text or image. When the user is satisfied with the changes, they press send and are sent back to the destination page.

### Delete Destination.
If the user presses Delete, a pop-up window appears asking the user if they want to delete this destination, if the user presses yes, the destination is deleted, if the user presses no, the process is canceled.

### Add Comment.
When the user presses add comment, a page opens that allows the user to fill in what he wants to say, when finished, the user presses send and is sent back to the destination page.

### Delete Comment.
If the user presses Delete, a pop-up window appears asking the user if they want to delete this comment, if the user presses yes, the comment is deleted, if the user presses no, the process is canceled.

### Header.
The header contains a title and links to the home page and log out. If a user is not logged in, links for logging in or registering an account are visible.
<br>
I have copied the style for the header from the code institute's walkthrough project because I thought it was neat and clean, but I have added my own logo.
<br>
The header is identical on all pages.

### Footer.
I have copied the style for the footer from the code institute's walkthrough project because I thought it was neat and clean.
<br>
The footer is identical on all pages.

### Existing features.
* Responsive design
* Views 
* Models
* Forms
* modal
* Authentication
* sign in/sign out
* sign up
* Add data
* Change data
* Delete data

### Features left to implement.


### Technologies.
* HTML
    * The structure of the Website was developed using HTML as the main language.
* CSS
    * The website was styled using css in a seperate file.
* Git
    * Used to commit and push code during the development of the Website
* Git hub
    * Source code is hosted on GitHub and delpoyed using Git Pages.
* JavaScript
    * The site was scripted using JavaScript.
* Django
    * The site was built using Django as a framework.
* Bootstrap
    * The site was styled and made responsive using Bootstap as a framewok.
* Python
    * The site was developed using Python.
* [Fontawesome](https://fontawesome.com/)
    * Is used to download icons used.

# Testing.

## Auto Test.

## Manual Test.
### Responsivenes.
The site were tested to ensure responsiveness on screen sizes from 320px and upwards on Chrome and Edge.
### Steps to test:
1. Open browser and navigate to [Magic cards](https://jesdah.github.io/Memory-cards/).
2. Open the developer tools (right click and inspect)
3. Set to responsive and decrease width to 320px
4. Set the zoom to 50%
5. Click and drag the responsive window to maximum width
### Expected:
Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.
### Actual:
Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.
### Website was also opened on the following devices and no responsive issues were seen:
* Samsung S22
* Iphone 13
* Lenovo ideapad S340
## Lighthouse Testing.
![screenshot of lighthouse score](/assets/images/memory-lighthouse.png)<br>

## Adventure Testing.
Adventure's page has been tested to ensure that users can add, change and delete without problems, without error messages.<br>
Steps to test:
1. Navigate to [Magic card.](https://jesdah.github.io/Memory-cards/)
2. Add Adventure:
   - Click: New Adventure
   - Render: add_adventure.html
   - Fill in the form
        - Name: New Adventure
        - Date: 2023-08-31
        - Featured_image: image
   - Click: Send
   - New Adventure is added to adventure page.
   - Render Django message "New Adventure created"
3. Edit Adventure:
    - Click: The blue Edit button.
    - Render: edit_adventure.html
    - Fill in the form
            - Name: New Adventure to Edited Adventure
            - Date: 2023-08-31 to 2023-08-28
            - Featured_image: image to image2
    - Click: Send
    - New Adventure is changed to Edited Adventure.
    - Render Django message "Adventure Changed"
4. Delete Adventure:
    - Click: The red Delete button.
    - Render popup: Are you sure you want to delete Edited Adventure?
    - Press Cancel:
        - The delete function is canceled.
    - Press OK:
        - Edited Adventure is deleted.
    - Render adventure page.
    - Render Django message "Adventure deleted" 
<br>
## Destination Testing.
Destination's page has been tested to ensure that users can add, change and delete without problems, without error messages.<br>
Steps to test:
1. Navigate to [Magic card.](https://jesdah.github.io/Memory-cards/)
2. Add Destination:
   - Click: New Destination
   - Render: post_form
   - Fill in the form
        - Title: New Destination
        - Content: This is a Destination
        - Featured_image: image
   - Click: Send
   - New Destination is added to destination page.
   - Render Django message "New Destination created"
3. Edit Destination:
    - Click: The blue Edit button.
    - Render: edit_post.html
    - Fill in the form
        - Title: New Destination to Edited Destination
        - Content: This is a Destination to This is a Edited Destination
        - Featured_image: image to image2
    - Click: Send
    - New Destination is changed to Edited Destination.
    - Render Django message "Destination Changed"
4. Delete Destination:
    - Click: The red Delete button.
    - Render popup: Are you sure you want to delete Edited Destination?
    - Press Cancel:
        - The delete function is canceled.
    - Press OK:
        - Edited Destination is deleted.
    - Render Destination page.
    - Render Django message "Destination deleted" 
<br>
## Comment Testing.
Comment section has been tested to ensure that users can add and delete without problems, without error messages.<br>
Steps to test:
1. Navigate to [Magic card.](https://jesdah.github.io/Memory-cards/)
2. Add Comment:
   - Click: Comment
   - Render: add_comment.html
   - Fill in the form
        - Body: This is a comment!
   - Click: Send
   - New Comment is added to destination page.
   - Render Comment:
        - Body: This is a comment!
        - Comment author: Admin
3. Delete Comment:
    - Click: The red Delete button.
    - Render popup: Are you sure you want to delete this Comment?
    - Press Cancel:
        - The delete function is canceled.
    - Press OK:
        - comment is deleted.
    - Render Destination page.
<br>
## Create, modify and delete as a non-authorized user.
1. Log in as Jesper with authorization: Creator.
    - Jesper can create, modify and delete data.
    - All buttons is visible for this user.

2. Log in as David with authorization: Fellow traveler.
    - David can create, modify and delete destinations.
    - Only buttons on Destination page is visible for this user.
* Break in and add adventure or Edit adventure.
    * Input: https://ganga-travel-5947dd277fb2.herokuapp.com/add/1/
        result: Empty screen.
    * input: https://ganga-travel-5947dd277fb2.herokuapp.com/edit/5/1/
        result: Empty screen.
3. Log in as Peter with authorization: Guest.
    - Peter can view content and add comments.
    - Only comment button is visible for this user.
* Break in and add adventure or Edit adventure.
    * Input: https://ganga-travel-5947dd277fb2.herokuapp.com/add/1/
        result: Empty screen.
    * input: https://ganga-travel-5947dd277fb2.herokuapp.com/edit/5/1/
        result: Empty screen.
* Break in and Edit adventure.
    * Input: https://ganga-travel-5947dd277fb2.herokuapp.com/edit_post/6/5/1/
        result: Empty screen.
### Expected:
The expectation has been that the site works as it should without broken links and that the user receives feedback in all situations and that unauthorized users cannot get in the back way and change or add data.

### Actual:
The site works as expected

### Validator Testing
- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org)
  ![validator result index.html](/assets/images/memory-html-validator.png)<br>

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org)
  ![validator result style.css](/assets/images/Memory-css-validator.png)<br>

  - No errors were found when passing through the official [Jshint linter](https://jshint.com/)
  ![Jshint result script.js](/assets/images/memory-jshint-validator.png)
### Bugs.
When I open the app locally, everything works as expected, but when I open the app in heroku, javascript is not loaded, so some functions do not work.

I solved it by entering the script at the bottom of the relevant HTML page.
### Unfixed Bugs
No unfixed bugs.
### Deployment.
The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.<br>
```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.<br>
```git push``` - This command was used to push all committed code to the remote repository on github.

### Deployment
- Use the following steps to deploy the poject to Heroku:
1. Use the "pip freeze -- local > requirements.txt" command in the gitPod terminal; to save any libraries that need to be installed to the project files in Heroku.
2. Login or create a Heroku account.
3. Click the "New" button in the upper right corner and select "Create New App".
4. Choose an app name and your region and click "Create App". Note: the app name must be unique.
5. Go to the "Settings" tab, add the python build pack and then the node.js build pack. This is to ensure the project functions correctly with the Code Institute pre-installed template.
6. Create a "Config VAR" with the 'CREDS' key and the enter the value of the creds.json file.
7. Create a second "Config VAR" with the key of 'PORT' and value of '8000'
8. Go to the "Deploy" tab and pick GitHub as a deployment method.
9. Search for a repository to connect to.
10. Click enable automatic deploys and then deploy branch.
11. Wait for the app to build and then click on the "View" link. 

The live link can be found [here](https://minesweeper-project3.herokuapp.com/).

### Clone the Repository Code Locally
Navigate to the GitHub Repository you want to clone to use locally:
- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal
The project will now been cloned on your local machine for use.
### Credit.
* The code structure for shuffeling the cards was taken from: https://github.com/swapnilsparsh/30DaysOfJavaScript/blob/master/27%20-%20Memory%20Matching%20Game/script.js

* The code structure for flip function and match function was taken from: https://stackoverflow.com/questions/75882658/memory-game-check-for-match-with-javascript

* The this===first code to ensure that the player couldnt click the same card multible times to win the game was taken from: https://marina-ferreira.github.io/tutorials/js/memory-game/

* I have used [w3schools](https://www.w3schools.com/) a lot for inspiration and tips and tricks

* The code stucture for the timer start and stop funtion was take from: https://stackoverflow.com/questions/5517597/plain-count-up-timer-in-javascript

* The code for the modal was taken from: https://www.w3schools.com/howto/howto_css_modals.asp

* For icons on the cards I have used: [Fontawesome](https://fontawesome.com/)

* To align the cards in 4x4 I have used code from: https://www.codingnepalweb.com/build-memory-card-game-html-javascript/

* To make the cards act responsive when the user clicks them I have used code from: https://marina-ferreira.github.io/tutorials/js/memory-game/