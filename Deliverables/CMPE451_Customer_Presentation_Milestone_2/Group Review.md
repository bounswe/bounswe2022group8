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
