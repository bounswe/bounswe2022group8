# Group 8 - Milestone 2 - Group Review

### Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [A Summary of work performed by each team member](#2-summary-of-work)
3. [Status of deliverables of Milestone 1](#3-status-of-deliverables)
4. [Progress according to requirements](#4-progress-according-to-requirements)
5. [API Endpoints](#5-api-endpoints)
6. [User Interface / User Experience](#6-user-interface-and-user-experience)
7. [Annotations](#7-annotations)
8. [Standards](#8-standards)
9. [Individual Reports](#9-individual-reports)

## 1. Executive Summary
### *Description*
We are a group of Bogazici University students who are taking the CMPE451 course in the Fall 2022 semester. We are developing an Art Community Platform where users can share their art items, interact with other users via comments, exhibitions and do much more. Users can view different art items through the feed on the home page. Registered users, can upload their own art items, share personal information through their profile and discover others’ art through the discover/recommendation page. They can also participate in exhibitions, share the geolocation of their exhibition, and interact with other users via comments. Registered users can even sell and make offers on art items through our app. 

### *Changes since Milestone 1 (Current Status)*

As you might know, at the first milestone stage we had already implemented the register and sign-in functionality, along with the initial versions of the homepage both for web and mobile. Since then, we have added several main features to our app which I will list below for ease of reading.
#### Backend
*	Art item model updated, CRUD APIs implemented.
*	User Profile upload/update APIs implemented.
*	Comments model updated, CRUD APIs implemented.
*	Forgot password + password update APIs implemented. Email for the application created/configured.
*	Tag CRUD APIs implemented.
*	User delete API implemented(may need update).
*	Like/unlike artitems/comments APIs _partially_ implemented.
*	Follow model updated, CRUD APIs implemented.
*	Amazon S3 integration is done for the image storage.
*	Swagger integration is done for the documentation of APIs.
*	We also created workflows for automated build and push of dockerfiles using Github Actions and Github Packages.
#### Web frontend
*	Profile page created, connected.
*	Settings/profile update page created, connected.
*	Discover page implemented, connected for users and art items.
*	Static exhibition page created.
*	Art item page created, connected(+upload art item).
*	Comments for the art item implemented.
*	Password update through settings.
#### Mobile
*	Profile page created, connected.
*	Settings/profile update page created, connected.
*	Styling updated to match web.
*	Art item page created, connected (+upload art item).
*	Comments for the art item implemented.
*	Home page created.
*	Forgot password + password update functionality implemented/connected.

### *Future Plans*

From this point onward, we plan on adding several more functionalities to our app. First off, we will supply frontend-backend connections for the APIs that were created but not yet used (such as tags and forgot password and follow). Simultaneously, we will continue with annotation research (standards, libraries) and get to implementing as soon as possible. We have also held a general meeting and went over the remaining tasks. Revised the priority of each task and allocated our resources accordingly (which systems we wanted to start implementing first etc.). And consequently, we have made some updates to our project plan as well. On a more practical level you may expect to see annotations, exhibition and bidding systems implemented very soon. We’re looking forward to making it to the finish line.

**Note:** Our current project plan can be found [here](https://github.com/bounswe/bounswe2022group8/wiki/CmpE-451-Project-Plan).




## 2. Summary of Work

<details>
    <summary> Serdar Akol </summary>



</details>

<details>
    <summary> Elif Bayraktar </summary>



</details>

<details>
    <summary> Metehan Dündar </summary>



</details>


<details>
    <summary> Mustafa Emre Erengül </summary>
    



</details>

<details>
    <summary> Sinem Koçoğlu </summary>
    
|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
 |  :----:        |  :----:   |  :----: |  :----: |
 |  Meeting |  Attended weekly meeting #5.    |  1 hour  |  [Weekly Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
 |  Meeting - FE |  Attended Week 5 FE Meeting.    |  40 minutes |  [Week 5 FE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Frontend-Meeting-Notes-2) |
  |  Meeting |  Attended Week 9 Meeting #6.   |  2 hours  |  [Week 9 Meeting #6](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
  |  Meeting - FE |  Attended Week 7 FE Meeting.   |  2 hours  |  [Week 7 FE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-7-Frontend-Meeting-Notes-3)|
 | Implementation | First view of profile page created on branch feature/FE-10 | 7 hour |  [Issue: #241](https://github.com/bounswe/bounswe2022group8/issues/241) |
|Research|Study different settings pages to discuss in lab session with frontend team |3 hours||
|Implementation|Improved profile page |3 hours|[Issue:#241](https://github.com/bounswe/bounswe2022group8/issues/241)|
 | Implementation | First view of recommendation page created on branch feature/FE-15 | 7 hour|[Issue:#267](https://github.com/bounswe/bounswe2022group8/issues/267) |
| Implementation | Research and improvements on recommendation page | 4 hour |[PR](https://github.com/bounswe/bounswe2022group8/pull/304)|
| Implementation | Adding logo and correcting typos on frontend.| 30 min | [Issue:#305](https://github.com/bounswe/bounswe2022group8/issues/305) and [PR](https://github.com/bounswe/bounswe2022group8/pull/309) |
 | Implementation | Working on branch feature/FE-17 to satisfy tasks stated in issues | 7 hour| [Issue:#306](https://github.com/bounswe/bounswe2022group8/issues/306) and [Issue:#307](https://github.com/bounswe/bounswe2022group8/issues/307) but not completed due to health issues. |
</details>

<details>
    <summary> Sena Mumcu </summary>
    



</details>

<details>
    <summary> Karahan Sarıtaş </summary>

|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
 |  :----:        |  :----:   |  :----: |  :----: |
 |  Meeting |  Attended weekly meeting #5.    |  1 hour  |  [Weekly Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
 |  Meeting - BE |  Attended backend weekly meeting #2.    |  45 minutes |  [Week 5 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-5--BE-Meeting-%232-(02.11.2022)) |
  |  Meeting |  Attended Week 9 Meeting #6.   |  2 hours  |  [Week 9 Meeting #6](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
  |  Meeting - BE |  Attended Week 7 BE Meeting.   |  2 hours  |  [Week 7 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-7-BE-Meeting-%233-(15.11.2022))|
 |  Meeting - BE |  Attended Week 9 BE Meeting.   |  2 hours  |  [Week 9 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-9--BE-Meeting-%234-(29.11.2022))|
| Research + Implementation | Swagger Integration for API documentation and testing | 3 hours | [#244](https://github.com/bounswe/bounswe2022group8/issues/244), [PR](https://github.com/bounswe/bounswe2022group8/pull/245) |
| Research + Implementation | AWS S3 Integration | 3 hours | [#246](https://github.com/bounswe/bounswe2022group8/issues/246), [PR](https://github.com/bounswe/bounswe2022group8/pull/247) |
| Research + Documentation | Research and documentation about the <br>image storage architecture from frontend to backend. | 45 minutes | [#246](https://github.com/bounswe/bounswe2022group8/issues/246)|
| Implementation | Implementation of ```GET``` user profile API. <br>Purpose of this API is to return profile information of a user by id. | 2 hours | [#248](https://github.com/bounswe/bounswe2022group8/issues/248), [PR](https://github.com/bounswe/bounswe2022group8/pull/249)|
| Implementation | Implementation of ```GET``` currently logged-in user profile API + Testing. <br>Purpose of this API is to return the profile information of the currently logged-in user in the session (doesn't ask for the ID). | 1 hour | [#248](https://github.com/bounswe/bounswe2022group8/issues/248), [PR](https://github.com/bounswe/bounswe2022group8/pull/249)|
| Implementation | Implementation of ```PUT``` API for profile update + AWS S3 Integration + Testing | 3 hours| [#248](https://github.com/bounswe/bounswe2022group8/issues/248), [PR](https://github.com/bounswe/bounswe2022group8/pull/249)|
 |  Implementation |  Updated login and signup error messages + integration with frontend.    |  2 hours  |  [PR](https://github.com/bounswe/bounswe2022group8/pull/252)|
 |  Implementation |  Hotfix for Swagger documentation.   |  15 minutes  |  [PR](https://github.com/bounswe/bounswe2022group8/pull/255)|
 |  Review | Reviewed a PR related to reset password API.  |  30 minutes  |  [PR](https://github.com/bounswe/bounswe2022group8/pull/259)|
| Implementation | Implementation of ```GET``` Art Item by ID API. | ~1 hour | [#250](https://github.com/bounswe/bounswe2022group8/issues/250), [PR](https://github.com/bounswe/bounswe2022group8/pull/251) | 
| Implementation | Implementation of ```GET``` art items of followed users API.<br> Purpose of this API is to feed the Just For You section. | ~1 hour  | [#250](https://github.com/bounswe/bounswe2022group8/issues/250), [PR](https://github.com/bounswe/bounswe2022group8/pull/251) | 
| Implementation | Implementation of ```DELETE``` art item API. | ~1 hour  | [#250](https://github.com/bounswe/bounswe2022group8/issues/250), [PR](https://github.com/bounswe/bounswe2022group8/pull/251) | 
| Implementation | Implementation of ```POST``` art item API. <br> Purpose of this API is to enable registered users upload art items to the application.  |~1 hour  | [#250](https://github.com/bounswe/bounswe2022group8/issues/250), [PR](https://github.com/bounswe/bounswe2022group8/pull/251) | 
| Implementation |  Implementation of ```GET``` art item by username  API. | ~1 hour  | [#250](https://github.com/bounswe/bounswe2022group8/issues/250), [PR](https://github.com/bounswe/bounswe2022group8/pull/251) | 
| Implementation |  Implementation of ```GET```all art items of a specific user by ID API. <br> Purpose of this API is to display all the art items of a user in his profile page. |~1 hour | [#250](https://github.com/bounswe/bounswe2022group8/issues/250), [PR](https://github.com/bounswe/bounswe2022group8/pull/251) | 
 | Implementation |  Implementation of ```GET``` art item by username  API. | ~20 minutes  | [#250](https://github.com/bounswe/bounswe2022group8/issues/250), [PR](https://github.com/bounswe/bounswe2022group8/pull/251) | 
 |  Implementation |  Configured `.production.env` for the production side and tested it. <br>This way we hide all of our information from public including the AWS credentials, database credentials, email information and S3 bucket information.  |  1 hour  | [#269](https://github.com/bounswe/bounswe2022group8/issues/269), [PR](https://github.com/bounswe/bounswe2022group8/pull/249)|
 |  Implementation & Review | Worked on the integration of profile page with the backend APIs with Furkan. | ~6 hours  |  [PR](https://github.com/bounswe/bounswe2022group8/pull/271)|
| Implementation | Updated how we store the image path and corresponding fields. | 30 minutes | [#269](https://github.com/bounswe/bounswe2022group8/issues/269), [PR](https://github.com/bounswe/bounswe2022group8/pull/271) | 
| Review & Implementation | Reviewed the comment related APIs in depth - Made small corrections. | 1 hour | [#261](https://github.com/bounswe/bounswe2022group8/issues/261), [PR](https://github.com/bounswe/bounswe2022group8/pull/262) | 
|Implementation | Implementation of ```GET``` followers of the currently logged-in user API. |  ~45 minutes | [#272](https://github.com/bounswe/bounswe2022group8/issues/272), [PR](https://github.com/bounswe/bounswe2022group8/pull/274) | 
|Implementation |Implementation of ```GET``` followings of the currently logged-in user API. |  ~45 minutes | [#272](https://github.com/bounswe/bounswe2022group8/issues/272), [PR](https://github.com/bounswe/bounswe2022group8/pull/274) | 
|Implementation | Implementation of ```GET``` followers of any user with ID API. |  ~45 minutes | [#272](https://github.com/bounswe/bounswe2022group8/issues/272), [PR](https://github.com/bounswe/bounswe2022group8/pull/274) | 
|Implementation |  Implementation of ```GET``` followings of any user with ID API. |  ~45 minutes | [#272](https://github.com/bounswe/bounswe2022group8/issues/272), [PR](https://github.com/bounswe/bounswe2022group8/pull/274) | 
|Implementation | Implementation of a ```POST``` API to follow a user with ID. |  ~45 minutes | [#272](https://github.com/bounswe/bounswe2022group8/issues/272), [PR](https://github.com/bounswe/bounswe2022group8/pull/274) | 
|Implementation | Implementation of a ```DELETE``` API to unfollow a user with ID. |  ~45 minutes | [#272](https://github.com/bounswe/bounswe2022group8/issues/272), [PR](https://github.com/bounswe/bounswe2022group8/pull/274) | 
|Review| Reviewed the a task related to our labels and provided possible improvements. |  15 minutes | [#273](https://github.com/bounswe/bounswe2022group8/issues/273)|
 |  Implementation |  Added an extension to generate class diagram of our Django models. |  15 minutes  | [#293](https://github.com/bounswe/bounswe2022group8/issues/293), [PR](https://github.com/bounswe/bounswe2022group8/pull/294)|
 |  Review |  Reviewed CI/CD pr, tested the Github packages and our docker-compose file. |  30 minutes  | [#209](https://github.com/bounswe/bounswe2022group8/issues/209), [PR](https://github.com/bounswe/bounswe2022group8/pull/215)|
 |  Implementation | Upon requests, updated the profile related GET APIs to return number of followers/followings. |  30 minutes  | [PR](https://github.com/bounswe/bounswe2022group8/pull/291)|
  |  Documentation | Updated our class diagram. |  30 minutes | [#303](https://github.com/bounswe/bounswe2022group8/issues/303)|
  |  Documentation | Created necessary folders for the Milestone II. <br> Separated the markdown file into sections and filled up the `API` section. |  1 hour | [#295](https://github.com/bounswe/bounswe2022group8/issues/295)|
  |  Implementation | Updated existing APIs and serializers to return requested information to frontend and mobile. | 30 minutes | [#321](https://github.com/bounswe/bounswe2022group8/issues/321), [PR](https://github.com/bounswe/bounswe2022group8/pull/320)|
   |  Review | Reviewed a PR related to like/unlike APIs. |  hours? |  [PR](https://github.com/bounswe/bounswe2022group8/pull/315)|
  > Implementation tasks involve documentation with Swagger, testing the functionality on both local and Dockerized version of the application.
</details>

<details>
    <summary> Doğukan Türksoy </summary>
    



</details>


<details>
    <summary> Mustafa Cihan </summary>
    
 |  Task Type   | Task Description |Related Link(s) |
 |  :----:        |  :----:   |  :----: |
 | Implementation | Redesigning landing page | [MOB-6: Revising Landing Page](https://github.com/bounswe/bounswe2022group8/issues/238)|
 | Implementation | Creating Art Item Pages | [MOB-8: Creating Art Item Pages](https://github.com/bounswe/bounswe2022group8/issues/282)|
 | Implementation | Revise Signup and Login page | [MOB-13: Revise Signup and Login page](https://github.com/bounswe/bounswe2022group8/issues/287)|
 | Implementation | Revising Homepage | [MOB-14: Revising Homepage](https://github.com/bounswe/bounswe2022group8/issues/289)|
 | Implementation | Static Comment Page| [MOB-15: Static Comment Page](https://github.com/bounswe/bounswe2022group8/issues/315)|
 | Implementation | Connecting Comment Page| [MOB-16: Connecting Comment Page](https://github.com/bounswe/bounswe2022group8/issues/316)|
 
    
</details>


## 3. Status of Deliverables

## 4. Progress According to Requirements

The requirements page of the application [here](https://github.com/bounswe/bounswe2022group8/wiki/Requirements).

### 1.1. User Requirements

<details>
    <summary> 1.1.1. Registration/Login </summary>
    
* 1.1.1.1. Users shall be able to register to the application providing their e-mail, username and password.
    * 1.1.1.1.1. Both e-mail and username shall be unique for each account.
    * 1.1.1.1.2. Username of the user must start with a letter, cannot end with an underscore, must have at least 6 characters and can consist of letters, numbers or underscores.
    * 1.1.1.1.3. Passwords of the user must have at least 10 characters, cannot be similar to his e-mail or username and cannot be a common password.
* 1.1.1.2. Users shall be able to log in to the application using their credentials, (username or e-mail), and password.
* 1.1.1.3. Logged-in users shall be able to safely log out.
* 1.1.1.4. Registered users shall be able to reset their passwords when logged in from profile settings.
    
</details>

<details>
    <summary> 1.1.2. Guest Users </summary>
    
* 1.1.2.1. Guest users shall be able to view the publicly visible art items on the platform.
* 1.1.2.2. Guest users shall be able to zoom in to an art item to examine it more closely.
* 1.1.2.3. Guest users shall be able to read the comments.
</details>

<details>
    <summary> 1.1.3. Profile Management </summary>
     
* 1.1.3.1. Registered users shall be able to edit their personal information shown on their profile pages.
    * 1.1.3.1.1. Registered users shall be able to add short descriptions about themselves on their profile pages.
    * 1.1.3.1.2. Registered users shall be able to provide name, surname, age and location.
    * 1.1.3.1.3. Registered users shall be able to upload/change their profile picture.
        
</details>
        
<details>
    <summary> 1.1.4. User Interaction </summary>

* 1.1.4.3. Registered users shall be able to upload and share art items.
    * 1.1.4.3.3. Registered users shall be able to add a title to the art item they upload.
    * 1.1.4.3.5. Registered users shall be able to add a description to the art item they upload.
* 1.1.4.5. Registered users shall be able to make comments on art items.
</details>

### 2.6 Security

* 2.6.1. User passwords shall be at least 10 characters long and cannot consist entirely of letters.
* 2.6.2. User passwords shall be stored in a database using PBKDF2 algorithm with a SHA256 hash.
    
## 5. API Endpoints
**Author: Karahan Sarıtaş**

* You can find the documentation of our API endpoints here: http://34.125.134.88:8000/api/v1/swagger/schema/ 
We used Swagger to document our APIs and provide exemplary inputs/outputs for other teams. Please notice that you have to authorize yourself in order to test some of the APIs (since these can be called only by logged-in users in our application - not by guest users).
* There is this button called ```Authorize``` on the right corner in Swagger page. We have to use it to test APIs that require authorization. For example, in order to test the ```logout``` API, first you have to log in to the application and have a token with you. Try the ```login``` endpoint first, copy paste the token returned to you and click on the ```Authorize``` button. Input the token in the following format: "Token xxx". Replace `xxx` with the token and don't forget to put a space between the first word and your token. You can refer to this [PR](https://github.com/bounswe/bounswe2022group8/pull/245) for more details if you want.
* By using Swagger, you can test any API you want either with the example input we provided or some other input that complies with the specification.
* Let me provide the Postman Collection [here](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_2/CmpE451%20API.postman_collection.json). `{{prod}}` stands for `34.125.134.88`.

## 6. User Interface and User Experience
<details>
    <summary>Web</summary>
    
#### Home Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Home.js)
* UI: 
    ![home1](https://user-images.githubusercontent.com/98259272/206314671-eb4af8f4-8797-4566-bda5-080aaa9887b0.png)
    ![home2](https://user-images.githubusercontent.com/98259272/206314697-bda8a10b-5ae5-4067-9288-fba2c832e600.png)
    ![home3](https://user-images.githubusercontent.com/98259272/206314712-4f061c77-5682-43dc-a6df-b2e7f52e8bc3.png)
#### Login Pop-up
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/LoginModal.js) 
* UI:
    ![login](https://user-images.githubusercontent.com/98259272/206314720-4d8d4686-a2ed-4e5f-bedc-91f47cd60b48.png)

#### Sign up Pop-up
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/SignupModal.js)
* UI:
    ![sign up](https://user-images.githubusercontent.com/98259272/206314739-5d915561-841c-4fc1-aa34-1ae606aba007.png)
    
#### Reset Password Pop-up
    
 * [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/ResetPasswordModal.js)
 * UI:
    ![forgotpassword](https://user-images.githubusercontent.com/98259272/206521742-d41bf4a8-331b-4567-ae2a-d8400b53404a.png)

#### Profile Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Profile.js)
* UI:
    ![profile1](https://user-images.githubusercontent.com/98259272/206314750-01434d05-cfbe-4665-9478-928f66405e6f.png)
    ![profile2](https://user-images.githubusercontent.com/98259272/206314761-bdcd97c6-105f-4d72-8c8e-9b87b9487b0d.png)
    ![profile3](https://user-images.githubusercontent.com/98259272/206314774-7a50be9b-33b4-4e5f-ae02-8ebdd6a6d493.png)
  
#### Art Item Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/ArtItem.js)
* UI:
    ![artitem](https://user-images.githubusercontent.com/98259272/206314832-ea8251b1-3b17-41ee-9b25-50a5fba2421b.png)
   
#### Sidebar
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/layout/Sidebar.js)
* UI:
    ![sidebar](https://user-images.githubusercontent.com/98259272/206314785-ed9f93fb-f379-48f5-ac3b-1b85ceb3b849.png)
  
#### Discover Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Recommendation.js)
* UI:
    ![discover1](https://user-images.githubusercontent.com/98259272/206314854-f91c8f4a-a42b-49fb-a3c2-eb628a1a99fa.png)
    ![discover2](https://user-images.githubusercontent.com/98259272/206316175-3c63bd4c-4123-4f04-93b7-de8eedaa3de6.png)
    ![discover3](https://user-images.githubusercontent.com/98259272/206314894-b96a2ae9-78cc-4409-a868-575e7a25bbcf.png)
    
#### Discover Art Items Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/RecommendedPages/RecommendedArtitems.js)
* UI:
    ![discoart1](https://user-images.githubusercontent.com/98259272/206316819-9e98f960-58d1-4c23-988d-01ffd9522637.png)
    ![discoart2](https://user-images.githubusercontent.com/98259272/206316825-56c4fd40-2ab5-48dc-bded-b3e1dea11277.png)

#### Discover Users Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/RecommendedPages/RecommendedUsers.js)
* UI:
    ![discouser](https://user-images.githubusercontent.com/98259272/206316838-56189929-9b02-49ab-9f6f-955735e23b14.png)    
    
#### Settings Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Settings.js) 
* UI:
    ![settings1](https://user-images.githubusercontent.com/98259272/206314803-0b12152a-c167-4cc4-8b89-373c2ef5c228.png)
    ![settings2](https://user-images.githubusercontent.com/98259272/206314814-b4355a4a-b507-4bf0-b828-a7f4b9c68880.png)

</details>   

<details>
    <summary>Mobile</summary>
</details> 

## 7. Annotations
Although we don't have an annotation implementation yet, we are aware of the importance of annotations and annotation implementation is at the top of our to-do list until the next milestone. As a result of the notes we took during the Milestone 2 presentations and the research we did, we decided to use @recogito/recogito-js and @recogito/annotorious react libraries for text annotations and image annotations respectively. Also, on the backend, we have already started setting up the annotation server.

## 8. Standards

During the implementation process of our project, as a whole team, we took great care to comply with W3C standards and we tried to research and comply with best practices, especially in accessibility, security and privacy issues. The parts we paid particular attention to can be categorized under the following items:

* All passwords were hashed with the sha256 hashing algorithm and all data exchanges involving passwords took place over the encoded versions of these passwords. Of course, they are also encrypted in our database.

* Since we are an art application, images are the most important part of our application. That's why we paid special attention to the security of the images. Our images are stored in AWS S3 private bucket in a very secure way with Amazon assurance. These images cannot be accessed without the key of the bucket. So even if someone accesses the url of any user's image, they will not be able to open it directly. Most importantly, we have not hard coded any key in the code and we have always tried to implement best practices for security in general. 

* In the whole process of writing the application, we took care to get minimum data from our users. We made many things such as name and location optional. Each registered user has a unique and encrypted authentication token specific to the session and this token is stored in local storage. Except for this information, we have not kept any information about the user in local storage so far.

* We made sure to provide metadata in our application. We used alt attribute in almost every image and we used aria-label tag in many of our interactive elements.

* We tried not to write the whole application as a bunch of meaningless divs. We did our best to increase tag diversity by using different HTML tags for different purposes. 

## 9. Individual Reports 

<details>
    <summary> Mustafa Cihan </summary>
I am Mustafa Cihan a member of group 8. I am working on mobile application of our project.

### Responsibilities
I am responsible for mobile application. For this milestone I worked on mobile application. I redesigned landing page, login page, signup page and home page. In addition to these redesigns, I designed and implemented art item page, comment structure and comment page, post structure and post. 

### Main Contributions
I mainly worked on mobile app so I gave all of my effort to develop mobile application.<br/>

**Code Related Issues**
* [MOB-16: Connecting Comment Page](https://github.com/bounswe/bounswe2022group8/issues/316)
* [MOB-15: Static Comment Page](https://github.com/bounswe/bounswe2022group8/issues/315)
* [MOB-14: Revising Homepage](https://github.com/bounswe/bounswe2022group8/issues/289)
* [MOB-13: Revise Signup and Login page](https://github.com/bounswe/bounswe2022group8/issues/287)
* [MOB-8: Creating Art Item Pages](https://github.com/bounswe/bounswe2022group8/issues/282)
* [MOB-6: Revising Landing Page](https://github.com/bounswe/bounswe2022group8/issues/238)
  
**Management Related Issues**
* Unfortunatelly, I don't have any management related issues.

**Pull Requests**
* [feature/MOB-6](https://github.com/bounswe/bounswe2022group8/pull/239)
* [Feature/MOB-13](https://github.com/bounswe/bounswe2022group8/pull/314)
* [feature/MOB-20](https://github.com/bounswe/bounswe2022group8/pull/331)
</details>

<details>
    <summary> Sinem Koçoğlu </summary>
    
I am Sinem Koçoğlu and I am member of group 8 frontend team.

### Responsibilities
* Creation of the first design of profile page.
* Study different settings pages to discuss in lab session with Furkan Keskin.
* Improvement on profile page and first design of art item page.
* Creation and design of recommendation pages.
* Logo integration and typo correction on frontend.
* PR Review: hotfix/FE-20
* PR Review: feature/FE-23
* Adding user interfaces for web to the Milestone II document.
* Taking notes during Week#10 Meeting#7
* Providing follow functionality on frontend. (not completed due to health issues)
* Providing hover over text annotation on frontend. (not completed due to health issues)

### Main Contributions
I have created the first design of profile page. Then, worked on design of settings page but I couldn't create a good design. That's why, Furkan Keskin took the responsibility of it and I created the first view of art item page that was improved by Furkan Keskin later. Then, I took the responsibility of creation of recommendation pages of frontend. I made changes according to the feedback we got in Milestone I presentation. I couldn't complete my tasks due to some health issues. They will be provided until final milestone.
    
**Code Related Issues**
* [FE-10](https://github.com/bounswe/bounswe2022group8/issues/241)
* [FE-15](https://github.com/bounswe/bounswe2022group8/issues/267)
* [FE-16](https://github.com/bounswe/bounswe2022group8/issues/305)
* [FE-17](https://github.com/bounswe/bounswe2022group8/issues/307)

**Management Related Issues**
* [GEN-36](https://github.com/bounswe/bounswe2022group8/issues/336)


**Pull Requests**
* [feature/FE-16](https://github.com/bounswe/bounswe2022group8/pull/309)
* [feature/FE-15](https://github.com/bounswe/bounswe2022group8/pull/304)


**Unit Tests**

You can find frotend unittests [here](https://github.com/bounswe/bounswe2022group8/tree/master/App/frontend/src/components/__test__)

My unittests:
    
* SignupModal.test.js
* SettingsProfilePopUp.test.js
* SettingsPasswordPopUp.test.js


**Additional**
    
PR reviews:
* [hotfix/FE-20](https://github.com/bounswe/bounswe2022group8/pull/337)
* [feature/FE-23](https://github.com/bounswe/bounswe2022group8/pull/339)


</details>


<details>
    <summary> Karahan Sarıtaş </summary>
    
I am [Karahan Sarıtaş](https://github.com/bounswe/bounswe2022group8/wiki/Karahan-Sar%C4%B1ta%C5%9F), a member of group 8. I'm working in the backend team.

### Responsibilities
* Integration of Swagger to the backend for API documentation and testing.
* AWS S3 Bucket Integration for both development and production.
* Research on how we can transfer the images from frontend to backend - and store them properly. As a result of my research, I provided a detailed description of the architecture [here](https://github.com/bounswe/bounswe2022group8/issues/246), implemented the backend part of the system.
* Integration of Profile Page with backend APIs with Furkan from frontend team.
* Implementation of art item related APIs (x7 APIs in total).
* Implementation of follow/unfollow related APIs (x6 APIs in total).
* Implementation of profile related APIs (x4 APIs in total).
* Communication with frontend for the integration stage.
* Updating login and signup error messages.
* PR Review: Reset Password API
* PR Review: Comment related APIs
* PR Review: CI/CD Integration
* PR Review: Like/Unlike API
* Frontend PR Reviews: API Integrations
* Configuration of `.env` and `.production.env` files to hide all of our secret information including AWS credentials, database credentials, email information and S3 bucket information, for both development and production sites.
* Generation of the class diagram fron Django using `graphviz`.
* Updating the class diagram. Filling up the `API` section of the Milestone II document.


### Main Contributions
Already listed all of my responsibilities and contributions above. Overall, I worked so hard to pushed the team forward, handled some of the challenging tasks in our path and guided people throughout the procedure. Critically reviewed pull requests of other team members. I showed uttermost respect to the mutual agreements we did in the meetings and therefore did my best to meet all the deadlines specified for our tasks. Unfortunatelly I couldn't see the same respect from others though.
    
**Code Related Issues**
* [BE-29: [API] Follow&Profile and Comment Enhancement](https://github.com/bounswe/bounswe2022group8/issues/321)
* [BE-24: Generate Class Diagram from Django](https://github.com/bounswe/bounswe2022group8/issues/293)
* [BE-22: [API] Implementation of Follow Action APIs](https://github.com/bounswe/bounswe2022group8/issues/272)
* [BE-21: Add Image Storage Path and Production Settings](https://github.com/bounswe/bounswe2022group8/issues/269)
* [BE-17: [API] Implementation of Art Item Related APIs - 1](https://github.com/bounswe/bounswe2022group8/issues/250)
* [BE-16: [API] Implementation of Profile Related APIs - 1](https://github.com/bounswe/bounswe2022group8/issues/248)
* [BE-15: Configure AWS S3 Bucket for Image Storage](https://github.com/bounswe/bounswe2022group8/issues/246)
* [BE-14: Add Swagger Integration](https://github.com/bounswe/bounswe2022group8/issues/244)


**Management Related Issues**
* [MIL-8: Milestone 2 Group Review](https://github.com/bounswe/bounswe2022group8/issues/295)
* [MIL-9: Software Requirements Specification](https://github.com/bounswe/bounswe2022group8/issues/298)
* [MIL-11:  Milestone 2 Deliverables](https://github.com/bounswe/bounswe2022group8/issues/300)
* [MIL-12: Update Class Diagram](https://github.com/bounswe/bounswe2022group8/issues/303)


**Pull Requests**
* [feature/BE-14](https://github.com/bounswe/bounswe2022group8/pull/245)
* [feature/BE-15](https://github.com/bounswe/bounswe2022group8/pull/247)
* [feature/BE-16](https://github.com/bounswe/bounswe2022group8/pull/249)
* [feature/BE-17](https://github.com/bounswe/bounswe2022group8/pull/251)
* [feature/BE-18](https://github.com/bounswe/bounswe2022group8/pull/252)
* [bugfix/BE-17](https://github.com/bounswe/bounswe2022group8/pull/311)
* [hotfix/BE-14](https://github.com/bounswe/bounswe2022group8/pull/255)
* [feature/BE-21](https://github.com/bounswe/bounswe2022group8/pull/270)
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/271)
* [feature/BE-22 #1](https://github.com/bounswe/bounswe2022group8/pull/274)
* [feature/BE-22 #2](https://github.com/bounswe/bounswe2022group8/pull/291)
* [feature/BE-24](https://github.com/bounswe/bounswe2022group8/pull/294)
* [feature/BE-29](https://github.com/bounswe/bounswe2022group8/pull/320)
* [hotfix/BE-11](https://github.com/bounswe/bounswe2022group8/pull/301)

**Unit Tests**
* You can find my unittests from the related [folder](https://github.com/bounswe/bounswe2022group8/tree/master/App/backend/api/tests).
* `test_artitem_creation`
* `test_artitem_deletion_cascaded`
* `test_artitem_deletion`
* `test_follow_creation`
* `test_follow_deletion_cascaded`
* `test_follow_artitems`
* `test_username_syntax`


> I hit the database from these functions, therefore they are not technically unit-tests but maybe integration tests. However, in CmpE352, we were requested to test our APIs and that was called unittest (that was indeed wrong but I guess the aim was to make us familiar with the concept of unittest and also testing our APIs?). So, I assumed that flexibility still holds, and included some very basic database operations in my unittests. For your information.

**Additional**
    
PR reviews:<br>
* [feature/BE-20](https://github.com/bounswe/bounswe2022group8/pull/262)
* [feature/BE-19](https://github.com/bounswe/bounswe2022group8/pull/259)
* [feature/BE-11](https://github.com/bounswe/bounswe2022group8/pull/215) 
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/271) (We worked as pair on this)
* [feature/FE-20](https://github.com/bounswe/bounswe2022group8/pull/322)
* [feature/BE-28](https://github.com/bounswe/bounswe2022group8/pull/315) (I've lost so much time with this PR due to the errors and couldn't even merge it yet. I don't know why but the guy literally opened it without running the application)
    

</details>
