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
### *Summary*


### *Changes since Milestone 1*


### *Future Plans*


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
  |  Documentation | Created necessary folders for the Milestone II. <br> Separated the markdown file into sections and filled up the `API` section. |  1 hour | [#303](https://github.com/bounswe/bounswe2022group8/issues/303)|
    
  > Implementation tasks involve documentation with Swagger, testing the functionality on both local and Dockerized version of the application.
</details>

<details>
    <summary> Doğukan Türksoy </summary>
    



</details>


<details>
    <summary> Mustafa Cihan </summary>
    


</details>


## 3. Status of Deliverables

## 4. Progress According to Requirements

## 5. API Endpoints
**Author: Karahan Sarıtaş**

* You can find the documentation of our API endpoints here: http://34.125.134.88:8000/api/v1/swagger/schema/ 
We used Swagger to document our APIs and provide exemplary inputs/outputs for other teams. Please notice that you have to authorize yourself in order to test some of the APIs (since these can be called only by logged-in users in our application - not by guest users).
* There is this button called ```Authorize``` on the right corner in Swagger page. We have to use it to test APIs that require authorization. For example, in order to test the ```logout``` API, first you have to log in to the application and have a token with you. Try the ```login``` endpoint first, copy paste the token returned to you and click on the ```Authorize``` button. Input the token in the following format: "Token xxx". Replace `xxx` with the token and don't forget to put a space between the first word and your token. You can refer to this [PR](https://github.com/bounswe/bounswe2022group8/pull/245) for more details if you want.
* By using Swagger, you can test any API you want either with the example input we provided or some other input that complies with the specification.
* Let me provide the Postman Collection [here](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_2/CmpE451%20API.postman_collection.json). `{{prod}}` stands for `34.125.134.88`.

## 6. User Interface and User Experience

## 7. Annotations

## 8. Standards

## 9. Individual Reports 

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
* Implementation of profile related APIs (x3 APIs in total).
* Updating login and signup error messages.
* PR Review: Reset Password API
* PR Review: Comment related APIs
* PR Review: CI/CD Integration
* Configuration of `.env` and `.production.env` files to hide all of our secret information including AWS credentials, database credentials, email information and S3 bucket information, for both development and production sites.
* Generation of the class diagram fron Django using `graphviz`.
* Updating the class diagram. Filling up the `API` section of the Milestone II document.


### Main Contributions
Already listed all of my responsibilities and contributions above. Overall, I worked so hard to pushed the team forward, handled some of the challenging tasks in our path and guided people throughout the procedure. Critically reviewed pull requests of other team members. I showed uttermost respect to the mutual agreements we did in the meetings and therefore did my best to meet all the deadlines specified for our tasks. Unfortunatelly I couldn't see the same respect from others though.
    
**Code Related Issues**
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
* [hotfix/BE-14](https://github.com/bounswe/bounswe2022group8/pull/255)
* [feature/BE-21](https://github.com/bounswe/bounswe2022group8/pull/270)
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/271)
* [feature/BE-22 #1](https://github.com/bounswe/bounswe2022group8/pull/274)
* [feature/BE-22 #2](https://github.com/bounswe/bounswe2022group8/pull/291)
* [feature/BE-24](https://github.com/bounswe/bounswe2022group8/pull/294)
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
    

</details>