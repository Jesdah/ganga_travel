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

### Playground Testing.
The Playground has been tested to ensure that it behaves as expected and that the player cannot cheat their way into a win.<br>
Steps to test:
1. Navigate to [Magic card.](https://jesdah.github.io/Memory-cards/)
2. Click on two cards:
   - First card: Mountain
   - Timer:Starts
   - Flip +1
   - Second card: Mountain
   - Flip: +1
   - Player text: You got a match!
3. Click on the same cards:
    - First card: Mountain
    - Timer: unaffected
    - Flip: unaffected
4. Click on two unmatched cards:
    - First card: Mountain
    - Timer:Starts
    - Flip +1
    - Second card:heart
    - Flip +1
    - Player text: No match
    - First and Second flipps back face down after 2 seconds.
5. Match all cards.
   - First card: Mountain
   - Timer:Starts
   - Flip +1
   - Second card: Mountain
   - Flip: +1
   - Player text: You got a match!
   * Match all cards
   - Timer: Stops
   - Flips: +16
   - Player text: All cards match!! Congratulations! 
<br>

### Expected:

Cards would flip over when clicked and cards that didn't match would flip back, the timer would start when the first card was clicked and stop when all cards were matched.

### Actual:

The game behaved as expected, the player cannot cheat their way through the game via loopholes.

### Footer
Tests have been done to ensure that the timer and Flip start counting and stop when they should.

They behaved as expected.

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
During most of the project I have not been able to get the icons to mix.
I solved it by creating a new id for each card.
Then a new problem was created that the card could not be matched. I solved it by creating a new span and putting the icons in there aswell. The last thing I did was set the font-size to 0 on the new span so that the user don't see the text but the match function can still read it, wich solved the problem.
### Unfixed Bugs
When using the website on an iPhone 13, the icons on the back disappear right after the cards have been turned over, which makes it difficult for the player to remember what the symbol is.
I have poor knowledge of IOS so I haven't been able to fix it.
### Deployment.
The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.<br>
```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.<br>
```git push``` - This command was used to push all committed code to the remote repository on github.
### Deployment to Github Pages
- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the menu on left select 'Pages'
  - From the source section drop-down menu, select the Branch: main
  - Click 'Save'
  - A live link will be displayed in a green banner when published successfully. 
The live link can be found here. https://jesdah.github.io/Memory-cards/
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