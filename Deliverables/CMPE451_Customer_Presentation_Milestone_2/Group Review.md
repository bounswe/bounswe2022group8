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

|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
 |  :----:        |  :----:   |  :----: |  :----: |
 |  Meeting |  Attended weekly meeting #5.    |  1 hour  |  [Weekly Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
 |  Meeting - BE |  Attended backend weekly meeting #2.    |  45 minutes |  [Week 5 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-5--BE-Meeting-%232-(02.11.2022)) |
  |  Meeting |  Attended Week 9 Meeting #6.   |  2 hours  |  [Week 9 Meeting #6](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
  |  Meeting - BE |  Attended Week 7 BE Meeting.   |  2 hours  |  [Week 7 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-7-BE-Meeting-%233-(15.11.2022))|
 |  Meeting - BE |  Attended Week 9 BE Meeting.   |  2 hours  |  [Week 9 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-9--BE-Meeting-%234-(29.11.2022))|
| PR Review | Reviewing the Follow related APIs | 40 minutes | [feature/BE-22](https://github.com/bounswe/bounswe2022group8/pull/274)|
| PR Review | Reviewing the Art item related APIs | 40 minutes | [feature/BE-17](https://github.com/bounswe/bounswe2022group8/pull/251)|
| Backend Repository Review | Reviewing the whole backend hierarchy, implementations and tests |  ~5 hours | - |
| Implementation | Implementing the Account/User deletion APIs | ~2 hours | [Issue BE-27](https://github.com/bounswe/bounswe2022group8/issues/276) [PR feature/BE-27](https://github.com/bounswe/bounswe2022group8/pull/319)|
| Implementation | Implementing the Like/Unlike Art item and comment APIs | ~10 hours | [Issue BE-28](https://github.com/bounswe/bounswe2022group8/issues/302), [PR feature/BE-28](https://github.com/bounswe/bounswe2022group8/pull/315)|


</details>

<details>
    <summary> Elif Bayraktar </summary>
    
|  Week 6 |              |  |
|  :----:       |  :----:   |  :----: |
|  1 hour 15 minutes  |  review   |  Reviewed the Swagger PR. [feature/BE-14](https://github.com/bounswe/bounswe2022group8/pull/245) |
|   5 hours      |  research/coding   |  Researched for and coded the Reset Password APIs. Researched for sending automated emails through the app. Tested through the terminal. [PR:Feature/be 19 ](https://github.com/bounswe/bounswe2022group8/pull/259), [Issue:#254](https://github.com/bounswe/bounswe2022group8/issues/254) |
|   20 minutes      |  review   |  Reviewed the hotfix PR. [hotfix/BE-14](https://github.com/bounswe/bounswe2022group8/pull/255)  |
|   5 hours      |  research/coding   |  Researched alternative ways for Reset Password APIs (django-otp), implemented password update API. [PR:Feature/be 19 ](https://github.com/bounswe/bounswe2022group8/pull/259)  |
|   4 hours      |  research/coding   |  Updated comment model using django-mptt. Implemented Comment APIs. [PR:Feature/be 20](https://github.com/bounswe/bounswe2022group8/pull/262), [Issue:#261](https://github.com/bounswe/bounswe2022group8/issues/261)  |
|   1 hour      |  coding/documentation   |  Added swagger documentaton for comment APIs.  |

| Week 7  |             |  |
|  :----:       |  :----:   |  :----: |
|  2.5 hours   |  coding   |  Updated comment get APIs to not require login.  [related comment](https://github.com/bounswe/bounswe2022group8/pull/262#issuecomment-1318972368) | 

|  Week 8 |              |  |
|  :----:       |  :----:   |  :----: |
|  1h+ hour   |  coding   |  Configured production email settings, solved merge conflicts and and merged. [related comment](https://github.com/bounswe/bounswe2022group8/pull/259#issuecomment-1319093869)  |
|  6.5 hours   |  devops/coding   |  Created Github Workflow for building and pushing docker images to Github Packages. [PR:Feature/BE11](https://github.com/bounswe/bounswe2022group8/pull/215), [issue](https://github.com/bounswe/bounswe2022group8/issues/209) |
|  2 hours   |  research   |  Researched annotation.  |



| Week 9|             |  |
|  :----:       |  :----:   |  :----: |
|  1 hour   |  review   |  Reviewed,fixed account deletion API PR. [PR:feature/BE-27 Account deletion API](https://github.com/bounswe/bounswe2022group8/pull/319)  |
|  1 hour   |  research   |  Researched annotation.  |
|  0.5 hour   |  research/upkeep   |  Investigated frontend code to add quasi-static content for milestone demo.  |



| Week 10  |              |  |
|  :----:       |  :----:   |  :----: |
|  2 hours   |  documentation   |  Wrote executive summary for milestone2 report. [#295](https://github.com/bounswe/bounswe2022group8/issues/295) |
|  2 hours   |  documentation   |  Wrote the timesheet.  |
  * I also participated in all of the General and Backend meetings.   


| Weekly meetings  |              |  |
|  :----:       |  :----:   |  :----: |
|  Meeting |  Attended weekly meeting #5.    |  1 hour  |  [Weekly Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
|  Meeting - BE |  Attended backend weekly meeting #2.    |  45 minutes |  [Week 5 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-5--BE-Meeting-%232-(02.11.2022)) |
|  Meeting |  Attended Week 9 Meeting #6.   |  2 hours  |  [Week 9 Meeting #6](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
|  Meeting - BE |  Attended Week 7 BE Meeting.   |  2 hours  |  [Week 7 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-7-BE-Meeting-%233-(15.11.2022))|
|  Meeting - BE |  Attended Week 9 BE Meeting.   |  2 hours  |  [Week 9 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-9--BE-Meeting-%234-(29.11.2022))|



</details>

<details>
    <summary> Metehan Dündar </summary>

|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
|  :----:        |  :----:   |  :----: |  :----: |
|  Meeting - GEN |  Read Week 5 GEN Meeting Notes on Discord.    |  20 minutes|  [Week 5 GEN Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5)|
|  Meeting - BE |  Read Week 5 BE Meeting Notes on Discord.    |  20 minutes|  [Week 5 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-5--BE-Meeting-%232-(02.11.2022))|
|  Meeting - BE |  Attended Week 7 BE Meeting.    |  2 hours|  [Week 7 BE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-7-BE-Meeting-%233-(15.11.2022))|
|  Meeting - MOB |  Attended Week 7 MOB Meeting.   | 1 hours  |  [Week 7 MOB Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-7--MOB-Meeting-%233-(16.11.2022))|
|  Meeting - MOB |  Attended Week 8 MOB Meeting.   |  2 hours  |  [Week 8 MOB Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-8-MOB-Meeting-%234-(26.11.2022))|
|  Meeting - GEN |  Attended Week 9 General Meeting.   |  1 hour  |  [Week 9 GEN Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022))|
|  Meeting - GEN |  Read Week 10 GEN Meeting Notes on Discord.    |  20 minutes|  [Week 10 GEN Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-10-Meeting-%237-(07.12.2022))|
| Documentation | Changing Label Systems | 45 minutes | [Issue GEN-33](https://github.com/bounswe/bounswe2022group8/issues/273)|
| Design | Creating Several Logo Designs | 8 hours | [Issue GEN-32](https://github.com/bounswe/bounswe2022group8/issues/268)|
| Presentation | Preparing for Milestone 2 Customer Presentation  |  1 hour | - |
| Implementation | Implementing the Forgot and Confirm Password Pages | 6 hours | [Issue MOB-21](https://github.com/bounswe/bounswe2022group8/issues/350) [PR feature/MOB-16](https://github.com/bounswe/bounswe2022group8/pull/329)|
| Review | Reviewing the Issue | 15 minutes | [Issue GEN-35](https://github.com/bounswe/bounswe2022group8/issues/290)|
| Documentation | Documenting Milestone 2 Deliverables | 1.5 hours | - |

</details>


<details>
    <summary> Mustafa Emre Erengül </summary>
    
|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
 |  :----:        |  :----:   |  :----: |  :----: |
 |  Planning  |  Attended Week5 Group Meeting.    |  1 hour  |  [Week5- Group Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
 |  Planning  |  Attended Week5 Mobile Meeting.     |  1 hour  |  [Week5- MOB Meeting #2](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Mobile-Meeting-Notes-2) |
 |  Planning  |  Review the plan for the second milestone during the lab time.     |  1 hour  |   |
 |  Planning  |  Attended Week7 Mobile Meeting.     |  1 hour  |  [Week7- MOB Meeting #3](https://github.com/bounswe/bounswe2022group8/wiki/Week-7--MOB-Meeting-%233-(16.11.2022)) |
| Research | Research about how to implement the page navigations. | 60 minutes | 
| Implementation | Profile page with the header widget is created. | 180 minutes | [feature/MOB-7(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/280)  |
| Implementation | Tabs are added and profile page is completed. | 180 minutes | [feature/MOB-7(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/280)  |
|  Planning  |  Attended Week8 Mobile Meeting.     |  2 hours  |  [Week8- MOB Meeting #4](https://github.com/bounswe/bounswe2022group8/wiki/Week-8-MOB-Meeting-%234-(26.11.2022)) |
| Implementation | Art item upload page is implemented. | 240 minutes | [feature/MOB-8(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/288)  |
|  Planning  |  Attended Week9 Group Meeting.    |  1 hour  |  [Week9- Group Meeting #9](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
| Implementation | Profile settings  page is implemented. | 180 minutes | [feature/MOB-8(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/288)  |
| Implementation | Profile photo change page is implemented. | 150 minutes | [feature/MOB-9(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/327)  |
| Implementation | Change password page is implemented. | 180 minutes | [feature/MOB-9(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/327)  |



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
    
|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
 |  :----:        |  :----:   |  :----: |  :----: |
| Meeting | Attended weekly meeting #5 | 1 hour | [Weekly Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
| Meeting | Attended weekly meeting #6 | 1 hour | [Weekly Meeting #6](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
| Meeting - BE| Attended backend weekly meeting #2 | 45 minutes | [Weekly BE Meeting #2](https://github.com/bounswe/bounswe2022group8/wiki/Week-5--BE-Meeting-%232-(02.11.2022)) |
| Meeting - BE| Attended backend weekly meeting #3 | 2 hours | [Weekly BE Meeting #3](https://github.com/bounswe/bounswe2022group8/wiki/Week-7-BE-Meeting-%233-(15.11.2022)) |
| Meeting - BE| Attended backend weekly meeting #4 | 2 hours | [Weekly BE Meeting #4](https://github.com/bounswe/bounswe2022group8/wiki/Week-9--BE-Meeting-%234-(29.11.2022)) |
| Documentation | Took notes during the weekly backend meeting #3 and documented them in wiki | 30 minutes | Related [issue](https://github.com/bounswe/bounswe2022group8/issues/264)| 
| Documentation | Took notes during the general meeting #6 and documented them in wiki | 30 minutes | Related [issue](https://github.com/bounswe/bounswe2022group8/issues/296)| 
| Documentation | Took notes during the backend meeting #4 and documented them in wiki | 30 minutes | Related [issue](https://github.com/bounswe/bounswe2022group8/issues/297)| 
| Research | Did a research on Django user flags to use in the implementation of the APIs | 2 hours | Related [issue](https://github.com/bounswe/bounswe2022group8/issues/278)|
| Implementation | Implemented and tested tag related API endpoints and documented them using Swagger | 5 hours | Related [issue](https://github.com/bounswe/bounswe2022group8/issues/277) and [PR](https://github.com/bounswe/bounswe2022group8/pull/292) |
| MIL2 | Reviewed requirements and documented the requirements addressed in the second milestone | 2 hours | Related issues [here](https://github.com/bounswe/bounswe2022group8/issues/298) and [here](https://github.com/bounswe/bounswe2022group8/issues/299) |
| MIL2 | Prepared and presented the artist use case scenario during the Customer Review 2 |  1 hour | Related discussion can be seen [here](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
| Review | Reviewed the PR involving the updated class diagram. | 30 minutes | Reviewed [PR](https://github.com/bounswe/bounswe2022group8/pull/294) |
| Review | Reviewd the PR for the `UserProfileSerializer` | 30 minutes | Reviewed [PR](https://github.com/bounswe/bounswe2022group8/pull/291) |
| Review | Reviewed the PR for the Swagger and AWS S3 integration | 45 minutes | Reviewed [PR](https://github.com/bounswe/bounswe2022group8/pull/249) |
| Review | Reviewed the PR for the AWS S3 integration with our application | 40 minutes | Reviewed [PR](https://github.com/bounswe/bounswe2022group8/pull/247) |

</details>

<details>
    <summary> Furkan Keskin </summary>
    
|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
|  :----:        |  :----:   |  :----: |  :----: |    
|  Meeting |  Attended weekly meeting #5.    |  1 hour  |  [Weekly Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
|  Meeting - FE |  Attended Week 5 FE Meeting.    |  40 minutes |  [Week 5 FE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Frontend-Meeting-Notes-2) |
|  Meeting |  Attended Week 9 Meeting #6.   |  2 hours  |  [Week 9 Meeting #6](https://github.com/bounswe/bounswe2022group8/wiki/Week-9-Meeting-%236-(29.11.2022)) |
|  Meeting - FE |  Attended Week 7 FE Meeting.   |  2 hours  |  [Week 7 FE Meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-7-Frontend-Meeting-Notes-3)|
|  Documentation | Took notes during the weekly meeting #5 and documented them in wiki   |  30 minutes |  [#235](https://github.com/bounswe/bounswe2022group8/issues/235)  |
|  Documentation | Took notes during the frontend meeting #2 and documented them in wiki   |  30 minutes |  [#236](https://github.com/bounswe/bounswe2022group8/issues/236)  |
|  Documentation | Took notes during the frontend meeting #3 and documented them in wiki   |  30 minutes |  [#265](https://github.com/bounswe/bounswe2022group8/issues/265)  |
|  Implementation  | Solved the cache bug  |  5 hours  |  [#232](https://github.com/bounswe/bounswe2022group8/issues/232)  |
|  Implementation  | Parameterized the URLs | 40 minutes| [#233](https://github.com/bounswe/bounswe2022group8/issues/233)  | 
|  Implementation/Research | Handled the frontend side of the image upload | 8.5 hours | [#266](https://github.com/bounswe/bounswe2022group8/issues/266), [PR](https://github.com/bounswe/bounswe2022group8/pull/271) |   
| Research | Researched art related web sites' profile pages, settings, art item pages, post areas, grid systems etc.  | 4 hours | [#241](https://github.com/bounswe/bounswe2022group8/issues/241)    |    
| Implementation | Improved Sinem's profile page interface considerably and connected to backend | 8 hours  |  [#241](https://github.com/bounswe/bounswe2022group8/issues/241) |
| Implementation | Designed and implemented a Settings page interface and connected to backend | 5 hours  | [#257](https://github.com/bounswe/bounswe2022group8/issues/257), [PR](https://github.com/bounswe/bounswe2022group8/pull/271)    |
| Implementation | Designed and implemented a Forgot Password pop up | 1 hours | [#260](https://github.com/bounswe/bounswe2022group8/issues/260), [PR](https://github.com/bounswe/bounswe2022group8/pull/271)  |
| Implementation | Designed and implemented an interface for art item upload from the user profile page. Created a loading interface as well. Also made the necessary API calls. | 7 hours |  [#241](https://github.com/bounswe/bounswe2022group8/issues/241), [PR](https://github.com/bounswe/bounswe2022group8/pull/322)   | 
| Implementation  | Designed and implemented the art item page interface. Connected it to backend. Art item page includes comment interface as well. Comments are connected to the backend too. |  10 hours  | [#310](https://github.com/bounswe/bounswe2022group8/issues/310), [PR](https://github.com/bounswe/bounswe2022group8/pull/322)   |
| Implementation   | Interface for tags are designed and implemented; however not connected yet.  | 1.5 hours  | [PR](https://github.com/bounswe/bounswe2022group8/pull/322)   |
| Implementation  | Created an interface for first upload | 2 hours | [PR](https://github.com/bounswe/bounswe2022group8/pull/330)     |
| Implementation  | Fixed some of the warnings in the application | 30 minutes | [PR](https://github.com/bounswe/bounswe2022group8/pull/330) |
| Implementation  | Created some loading screens and notification pop-ups for a better user experience | 3 hours | [PR](https://github.com/bounswe/bounswe2022group8/pull/322)  |
| Implementation  | Connected the home and discover pages to the backend |  1 hour | [PR](https://github.com/bounswe/bounswe2022group8/pull/334)  |
| Testing | Wrote unit tests for some components | 1 hour | [#338](https://github.com/bounswe/bounswe2022group8/issues/338), [PR](https://github.com/bounswe/bounswe2022group8/pull/339)  |
| Planning   | Updated our project plan in line with the meetings  | 30 minutes |   |
| Review | Reviewed the following PRs: [feature/BE-18](https://github.com/bounswe/bounswe2022group8/pull/252), [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/256), [feature/BE-21](https://github.com/bounswe/bounswe2022group8/pull/270) |  1 hour |   |
| Presentation  | Created a sample gallery for the presentation | 45 minutes  |     |
| MIL2 |  Filled in the Annotations section in the Milestone 2 report  | 30 minutes   |  [#341](https://github.com/bounswe/bounswe2022group8/issues/341)  |
| MIL2 |  Filled in the Standards section in the Milestone 2 report  | 1.5 hours   |  [#342](https://github.com/bounswe/bounswe2022group8/issues/342)  |



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
|Deliverable|Status|Changes| 
|-----|:--------:|:------:| 
|Software Requirements Specification | Changed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Requirements)|
|Software Design (UML):Use-Case Diagram | Changed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Use-case-diagram)|
|Software Design (UML):Class Diagram | Changed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Class-Diagram)|
|Software Design (UML):Sequence Diagram | Changed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Practice-App---Sequence-Diagrams)|
|[Scenario: Art Follower User](https://github.com/bounswe/bounswe2022group8/wiki/Scenario:-Art-Follower-User) | No changes | - |
|[Scenario: Verified User/Artist Scenario](https://github.com/bounswe/bounswe2022group8/wiki/Scenario-2) | No changes | - |
|[Scenario: Collaboration Scenario](https://github.com/bounswe/bounswe2022group8/wiki/Scenario-3) | No changes | - |
|[Project Plan](https://github.com/bounswe/bounswe2022group8/wiki/CmpE-451-Project-Plan)| No changes | - |
|Individual Contribution Reports | Changed | [Latest version](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_2/Group%20Review.md#9-individual-reports)|
|[Web App](http://34.125.134.88/#) | No changes | - |
|Mobile App - APK | Changed | [Latest version]()|
|Group Review | Changed | [Latest version](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_2/Group%20Review.md)|


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
* You can use the button below to test any functionality you want. All inputs are already prepared for you - you just have to sign-in or register to the application and use the generated token for authentication-required APIs. <br>
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/1409a4435fe689ab34fa?action=collection%2Fimport)
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
    
![WhatsApp Image 2022-12-08 at 17 02 24 (1)](https://user-images.githubusercontent.com/63647591/206468755-0e058571-7d0e-429f-89ed-99805534b118.jpeg)

* [Art Item Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/artitem_page.dart)

![WhatsApp Image 2022-12-08 at 17 02 24](https://user-images.githubusercontent.com/63647591/206468808-e494c652-2304-49cb-b135-35c53e8e6a88.jpeg)

* [Home Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/home_page.dart)

![WhatsApp Image 2022-12-08 at 17 02 22 (3)](https://user-images.githubusercontent.com/63647591/206469044-d4fe0297-d7ac-44d5-9a83-1e8d6a378f13.jpeg)

* [Comment Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/comment_page.dart)

![WhatsApp Image 2022-12-08 at 17 02 23 (1)](https://user-images.githubusercontent.com/63647591/206468920-495ab94f-48e9-4804-9b32-205a62c259ac.jpeg)

* [Landing Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/landing_page.dart)

![WhatsApp Image 2022-12-08 at 17 02 21](https://user-images.githubusercontent.com/63647591/206469185-678ae22a-5dbf-40e6-98fe-6f6279fc967f.jpeg)

* [Forgot Password Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/forgot_password.dart)

![WhatsApp Image 2022-12-08 at 17 02 22](https://user-images.githubusercontent.com/63647591/206469169-97c4a5cf-dc6c-46eb-a093-79f3eb83369b.jpeg)

* [Signup Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/signup_page.dart)

![WhatsApp Image 2022-12-08 at 17 02 22 (1)](https://user-images.githubusercontent.com/63647591/206469155-4dd0b650-80de-4a0a-af7e-deea3cd879da.jpeg)

10

![WhatsApp Image 2022-12-08 at 17 02 23](https://user-images.githubusercontent.com/63647591/206470476-c5052cae-bae4-42e4-af34-96adc1dfbaf9.jpeg)
11
![WhatsApp Image 2022-12-08 at 17 02 24 (2)](https://user-images.githubusercontent.com/63647591/206470543-919bc932-28e3-484d-88ab-d229083fc049.jpeg)

![WhatsApp Image 2022-12-08 at 17 03 40](https://user-images.githubusercontent.com/63647591/206470594-2e111062-cb08-4dbe-8105-a51ed192b2c9.jpeg)

* [Profile Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/profile_page.dart)

![WhatsApp Image 2022-12-08 at 17 02 24 (3)](https://user-images.githubusercontent.com/63647591/206470617-afc23bbf-8071-4c0d-80a5-4a1971f4c2c6.jpeg)

* [Login Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/login_page.dart)

![WhatsApp Image 2022-12-08 at 17 02 22 (2)](https://user-images.githubusercontent.com/63647591/206471187-d4f020ca-f54c-47ca-85c3-6826817a1754.jpeg)

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
    <summary> Serdar Akol </summary>
I am Serdar Akol a member of group 8. I used to work on mobile application side of the project, after Milestone 1 report I have been transferred
to the backend side of the project.

### Responsibilities
I am responsible for backend side of the project. 
* Following the implementations of my team.
* Reviewing the PRs of my team members.
* Implementing Like/Unlike feature for Art items. 
* Implementing Like/Unlike feature for comments. 
* Implementing Account/User deletion API. 


### Main Contributions
My main contributions are also the ones listed above. Since, I have been transferred to backend team after the first milestone report. I have struggled to addopt to the team at first. But thanks to Karahan and all my other backend team, I could catch the team up. <br/>

**Code Related Issues**
* [Issue BE-27](https://github.com/bounswe/bounswe2022group8/issues/276)
* [Issue BE-28](https://github.com/bounswe/bounswe2022group8/issues/302)
  
**Management Related Issues**
* Unfortunatelly, I don't have any management related issues.

**Pull Requests**
* [feature/BE-27](https://github.com/bounswe/bounswe2022group8/pull/319)
* [feature/BE-28](https://github.com/bounswe/bounswe2022group8/pull/315)

**Additional**
    
PR reviews:
* [feature/BE-22](https://github.com/bounswe/bounswe2022group8/pull/274)
* [feature/BE-17](https://github.com/bounswe/bounswe2022group8/pull/251)    

</details>


<details>
    <summary> Sena Mumcu </summary>

I am Sena Mumcu, a member and the communicator of group 8. I am working in the backend subgroup of our team. 
    
### Responsibilities
I am responsible for the backend side of our developments.
* Implementing the Tag related API endpoints.
* Testing the API endpoints I have written and documenting them using Swagger.
* Reviewing and testing my backendteam-members' PRs.
* Researching user flags in Django to implement tag creation and deletion APIs.
* Presenting the artist use case scenario during the second customer review. 
* Helping the new backend team member get onboard.
    
### Main Contribution

My main contributions include coding API endpoints as well as supporting the team in management related issues. I tried to review my teammates's work quickly as possible to help the team progress and did my best to implement API endpoints.
    
**Code Related Issues**
* [BE-23: [API] Tag Managing](https://github.com/bounswe/bounswe2022group8/issues/277)
* [BE-25: Research on Moderator Flags](https://github.com/bounswe/bounswe2022group8/issues/278)
* [BE-26: [API] Semantic and Lexical Search](https://github.com/bounswe/bounswe2022group8/issues/279)

**Management Related Issues**
* [MIL-10: Milestone 2 Requirements](https://github.com/bounswe/bounswe2022group8/issues/299)
* [Meeting Notes: Week 9 BE Meeting 4](https://github.com/bounswe/bounswe2022group8/issues/297)
* [Week 9 - Meeting #6(29.11.2022)](https://github.com/bounswe/bounswe2022group8/issues/296)
* [GEN-35: Application Name and Logo](https://github.com/bounswe/bounswe2022group8/issues/290)
* [BE-31: Meeting Notes: Week 7 Backend-Meeting #3](https://github.com/bounswe/bounswe2022group8/issues/264)
    
### Pull Requests
* [Feature/BE-23 Tag APIs](https://github.com/bounswe/bounswe2022group8/pull/292)
    
### Unit Tests
* Unfortunately I didn't write any unit tests.
    
### Additional Information
**PR reviews** 
* [feature/BE-24](https://github.com/bounswe/bounswe2022group8/pull/294#issuecomment-1331032342)
* [feature/BE-22](https://github.com/bounswe/bounswe2022group8/pull/291#issuecomment-1331030915)
* [feature/BE-16](https://github.com/bounswe/bounswe2022group8/pull/249#issuecomment-1318197777)
* [feature/BE-15](https://github.com/bounswe/bounswe2022group8/pull/247#issuecomment-1318189615)
    
</details>

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
    <summary> Furkan Keskin </summary>
I'm Furkan Keskin and I'm a member of the group 8 frontend team.
    
### Responsibilities
* Form error interface.
* Finding a solution to the cache bug.
* Forgot Password interface.
* Settings Page interface and connections.
* Reset Password interface and connection.
* Profile Page interface and connections.
* Art Item Upload interface and connections.
* Handling the front end side of the image upload. (AWS s3, base 64, preview etc.)
* Art Item Page interface and connections.
* Comment Section interface and connections.
* Tag interface.
* Connecting the home and discover pages.
* Transitions between pages for a better user experience such as loading screens and notification pop-ups.
* Writing unit tests for some components.
* CSS and design improvements when Sinem needed help.
* Communication with the backend team for the integration stage.
* Project Plan updates.
* Note taker in a general meeting.
* Note taker in multiple front-end meetings.
* PR and issue reviews of the front end side.
* Testing some API endpoints from postman. (Some backend PR reviews as well)
* Providing sample art items/gallery for the presentation.
* Presenting the web side of the project.
* Filling in the Annotations section in the Milestone 2 report.
* Filling in the Standards section in the Milestone 2 report.
    
### Main Contributions
Since we are a fairly small sub-team, my responsibilities were not exactly in line with the project plan and were updated regularly, but in general I was able to take the above responsibilities and deliver them. Though I didn't do a very good job with some of them. 

    
**Code Related Issues**
* [FE-7](https://github.com/bounswe/bounswe2022group8/issues/232)
* [FE-8](https://github.com/bounswe/bounswe2022group8/issues/233)
* [FE-10](https://github.com/bounswe/bounswe2022group8/issues/241)
* [FE-11](https://github.com/bounswe/bounswe2022group8/issues/257)
* [FE-12](https://github.com/bounswe/bounswe2022group8/issues/260)
* [FE-14](https://github.com/bounswe/bounswe2022group8/issues/266)
* [FE-20](https://github.com/bounswe/bounswe2022group8/issues/310)
* [FE-23](https://github.com/bounswe/bounswe2022group8/issues/338)
    
    
**Management Related Issues**
* [MIL-14](https://github.com/bounswe/bounswe2022group8/issues/340)
* [MIL-15](https://github.com/bounswe/bounswe2022group8/issues/341)
* [MIL-16](https://github.com/bounswe/bounswe2022group8/issues/342)
    
    
**Pull Requests**  
* [feature/FE-8](https://github.com/bounswe/bounswe2022group8/pull/253)
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/271)
* [feature/FE-20](https://github.com/bounswe/bounswe2022group8/pull/322)
* [feature/FE-21](https://github.com/bounswe/bounswe2022group8/pull/330)
* [feature/FE-22](https://github.com/bounswe/bounswe2022group8/pull/334)
* [hotfix/FE-20](https://github.com/bounswe/bounswe2022group8/pull/337)
* [feature/FE-23](https://github.com/bounswe/bounswe2022group8/pull/339)
    

**Unit Tests**

You can find frontend unit tests [here.](https://github.com/bounswe/bounswe2022group8/tree/master/App/frontend/src/components/__test__)

My unittests:
    
* `HomeFooter.test.js`
* `IntroImage.test.js`
* `LoginModal.test.js`
* `ResetPasswordModal.test.js`
* `Searchbar.test.js`
    
    
**Additional**
    
PR reviews:
* [feature/BE-18](https://github.com/bounswe/bounswe2022group8/pull/252)
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/256)
* [feature/BE-21](https://github.com/bounswe/bounswe2022group8/pull/270)
    
    
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
* Updating existing APIs in accordance with the requests coming from frontend and mobile during the milestone week.

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
* [MIL-13: Pre-Release Version 0.2.0](https://github.com/bounswe/bounswe2022group8/issues/335)


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
* [feature/BE-30](https://github.com/bounswe/bounswe2022group8/pull/333)
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
* [feature/FE-22](https://github.com/bounswe/bounswe2022group8/pull/334)
* [feature/BE-28](https://github.com/bounswe/bounswe2022group8/pull/315) (I've lost so much time with this PR due to the errors and couldn't even merge it yet. I don't know why but the guy literally opened it without running the application)
    
</details>

<details>
    <summary> Mustafa Emre Erengül </summary>
I am Mustafa Emre Erengül, a team member of the Group 8. I specificly work on the Mobile development part of our project.

### Responsibilities
In the mobile application part of our project, we had some implementations that we would like to add before the Second Milestone. So we shared the implementations among our mobile team. As a team member I was responsible for implementations of creating a profile page, settings (editing profile) page, change password page, updating profile photo page and a page that allows users to add a new art item to their profile.
    
### Main Contributions
I implemented a profile page that allows users to dislay their uploaded art items and the exhibitions that they are attending. One can see user's username, name, surname, bio, location and profile photo by looking at this page. I also implement a settings page to enable users to make changes over this fields. Moreover a user can change his/her password and profile photo. Lastly I created an upload art item page which allows users to add new art items to their profile.  <br/>

**Code Related Issues**
* [MOB-7: Creating a profile page](https://github.com/bounswe/bounswe2022group8/issues/281) (implemented)
* [MOB-9: Redesign of the main navigation bar](https://github.com/bounswe/bounswe2022group8/issues/283) (implemented)
* [MOB-10: Changing password and the profile photo](https://github.com/bounswe/bounswe2022group8/issues/284) (implemented)
* [MOB-11: Uploading a new art item to the profile](https://github.com/bounswe/bounswe2022group8/issues/285) (implemented)
* [MOB-12: Renewing the mobile app icon and the name](https://github.com/bounswe/bounswe2022group8/issues/286) (implemented)
    
**Management Related Issues**
* [GEN-32: Logo for Application](https://github.com/bounswe/bounswe2022group8/issues/268) (contributed)
* [GEN-35: Application Name and Logo](https://github.com/bounswe/bounswe2022group8/issues/290) (completed)
    
**Pull Requests**
* [feature/MOB-7 : Profile Page Implementation](https://github.com/bounswe/bounswe2022group8/pull/280)
* [feature/MOB-8 : Editing Profile and Uploading Art Item](https://github.com/bounswe/bounswe2022group8/pull/323)
* [feature/MOB-9 : Change Password & Profile Photo](https://github.com/bounswe/bounswe2022group8/pull/327)

***Additional***

* [Feature/MOB-13](https://github.com/bounswe/bounswe2022group8/pull/314) (reviewed)
* [Feature/mob 18](https://github.com/bounswe/bounswe2022group8/pull/325) (reviewed)
    
</details>
