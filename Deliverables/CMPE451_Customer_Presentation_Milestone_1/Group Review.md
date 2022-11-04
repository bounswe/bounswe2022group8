# Group 8 - Milestone 1 - Group Review

## Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [List and status of deliverables](#2-list-and-status-of-deliverables)
3. [Evaluation of the status of deliverables and its impact on your project plan](#3-evaluation-of-deliverables-and-impact)
4. [Evaluation of tools and processes you have used to manage your team project](#4-evaluation-of-tools-and-processes)
5. [The requirements addressed in this milestone](#5-the-requirements-addressed-in-this-milestone)
6. [Overall description of responsibilities that are assigned to each member](#6-responsibilities)
7. [A Summary of work performed by each team member](#7-summary-of-work)

### 1. Executive Summary







### 2. List and Status of Deliverables




### 3. Evaluation of Deliverables and Impact




### 4. Evaluation of Tools and Processes




##### 1) Mobile Team
<details>
    <summary> Visual Studio Code (VSCode) </summary>
    
  Visual Studio Code is a commonly used IDE to develop applications with most programming languages. It is lightweight and it has a perfect interface for viewing folders, splitting screen and using terminals. We used some very useful Visual Studio Code extensions. Mobile team used flutter/dart extension, Frontend team used React extension and Backend team used Django extension for their development. Also all teams are used extensions for Git to push/pull operations and Docker extension to track container activities. We also managed SSH connection with our deployment environment via Remote extension of VSCode. 
 </details>    
<details>
       <summary>  Flutter/Dart  </summary>
    
   Before researching mobile frameworks, we decided not to use Java since it is harder to deal with errors in this language in our sense. We came up with 2 alternatives, React Native and Flutter. Our team had little experience with JavaScript, so decided to go with *Flutter*. Flutter is created by Google. It uses Dart as the programming language, which is very similar to Java in terms of syntax. Flutter has lots of official and unofficial resources. Flutter has a perfect VSCode plugin, it helps a lot at developing processes. Also it has a feature called “hot reload”, you don’t need to restart Flutter application again and again when you change the code, except in some structural cases. This feature also speeded up our development.  
    </details>    
<details>
       <summary> Android Studio  </summary>
    
  Android Studio is a commonly used IDE for Android developers. Since VSCode has great plugins for Git, Docker etc. and our team is accustomed with VSCode, we used Android Studio only to create and start an Android Virtual Device (as known as Emulator). When we start the emulator, the flutter application runs on this emulator automatically.
    </details>    
##### 2) Backend Team
##### 3) Frontend Team
   
<details>
       <summary>  VS Code  </summary>
    Microsoft Visual Studio Dode is an useful editor to manage the project with backend side because we can run both sides on the same window when we want to test if frontend and backend connected successfully. Also, it is easy to install extensions such as Eslint used to find and fix problems in javascript code and Prettier that is a code formatter. What's more, VS code is convenient to carry out git management. 
</details> 
<details>
       <summary> Javascript   </summary>
    We prefer using javascript for frontend because we are familiar with React.js library a little. It is beginner-friendly and there are a lot of resources related to it available on the internet. Also, it is compatible with Node.js to develop an web application. 
    </details> 
    <details>
       <summary> React.js  </summary>
    It is an open source library that makes it easier to develop user interfaces. It has many features such as hooks, states etc. which provides capability to develop featured user interfaces.
    </details> 
    <details>
       <summary> Node.js   </summary>
    It is a framework to develop web applications using backend API services. By its package manager, it is easy to see modules installed for the project properly. Besides, it benefits from javascript interpreters. In development of frontend applications, using javascript with react.js and node.js is very common. That's way, there are many resources on the internet to find a solution for possible errors we encounter in the process of development.
    </details> 
    <details>
       <summary> Bootstrap   </summary>
    It is an open source frontend development css framework providing pre-defined design templates, syntax, and css classes for components. We benefit from these templates and make improvements on them to design our user interfaces.
    </details> 
    <details>
       <summary> Docker   </summary>
    We have to dockerize the frontend to automate deployment by using Docker Desktop. Dockerization files work well in local, but in the process of deployment an error occured related to extensive amount of browser cache. We will try to solve that problem as soon as possible to make deployment process faster and free of error.
    </details> 
    
### 5. The Requirements Addressed in this Milestone
<summary>1.1.1. Registration/Login</summary>

Please refer to our requirements for glossary and further details.

* 1.1.1.1. Users shall be able to register to the application providing their e-mail, username and password.
   * 1.1.1.1.1. Both e-mail and username shall be unique for each account. 
   * 1.1.1.1.2. Username of the user must start with a letter, cannot end with an underscore, must have at least 6 characters and can consist of letters, numbers or underscores.
   * 1.1.1.1.3. Passwords of the user must have at least 10 characters, cannot be similar to his e-mail or username and cannot be a common password. 
* 1.1.1.2. Users shall be able to log in to the application using their credentials, (username or e-mail), and password.
* 1.1.1.3. Logged-in users shall be able to safely log out.
<summary> 2.6. Security</summary>

* 2.6.1. User passwords shall be at least 10 characters long and cannot consist entirely of letters.
* 2.6.2. User passwords shall be stored in a database using PBKDF2 algorithm with a SHA256 hash.

### 6. Responsibilities

* Karahan Sarıtaş

  1. Revision of requirements and making necessary changes.
  2. Creating the initial structure of our Django project. Configuration of settings for both development and production environment.
  3. Dockerization of the backend service.
  5. Implementation of registration API.
  6. Implementation of login API.
  7. Implementation of logout API.
  8. Research on tokenization and authentication mechanisms.
  9. Helping frontend team for the connection.
  10. Dockerization of frontend and deployment.

### 7. Summary of Work

<details>
    <summary> Karahan Sarıtaş </summary>

|  Task Type   | Task Description   | Related Link(s) |
 |  :----:        |  :----:    |  :----: |
 |  Planning |  Attended weekly meeting #1. I introduced our Github repository to our new friend and <br>talked about what we have been up to in the previous course in general.    | [Weekly Meeting #1](https://github.com/bounswe/bounswe2022group8/wiki/Week-1-Meeting-Notes-1) |
 | Communication | Set up the Discord channel for CmpE451  |  [#154](https://github.com/bounswe/bounswe2022group8/issues/154)|
 | Communication | Update the communication plan. |  [#159](https://github.com/bounswe/bounswe2022group8/issues/159) |
|  Planning |  Attended weekly meeting #2 and weekly meeting #3.    |  [Weekly Meeting #2](https://github.com/bounswe/bounswe2022group8/wiki/Week-2-Meeting-%232), [Weekly Meeting #3](https://github.com/bounswe/bounswe2022group8/wiki/Week-2--Meeting-Notes-3) |
 | Documentation | Documentation of our weekly meeting notes.  | [#160](https://github.com/bounswe/bounswe2022group8/issues/160) |
 | Planning | Review the project planning for CmpE451.   | [#161](https://github.com/bounswe/bounswe2022group8/issues/161)|
 | Requirements Elicitation | Review all the requirements to recall our design.  | [#162](https://github.com/bounswe/bounswe2022group8/issues/162)|
 | Requirements Elicitation| Revise the requirements _Notifications_ critically.    | [#163](https://github.com/bounswe/bounswe2022group8/issues/163)|
 | Requirements Elicitation| Revise the requirements _Bidding System_ critically.    | [#166](https://github.com/bounswe/bounswe2022group8/issues/166)|
 | Requirements Elicitation| Revise the requirements _Verification and Level System_ critically.  | [#167](https://github.com/bounswe/bounswe2022group8/issues/167)|
| Communication | Creating an agenda and determining some of <br> the topics we have to discuss in the next meeting. |[Agenda & Questions & Answers](https://github.com/bounswe/bounswe2022group8/wiki/Agenda-&-Questions-&-Answers)| 
| Requirements Elicitation | Made the necessary corrections on _follow_ and _visibility of art item_ features as decided in the meeting. | [#169](https://github.com/bounswe/bounswe2022group8/issues/168), [#172](https://github.com/bounswe/bounswe2022group8/issues/172)|
 |  Planning |  Attended first backend meeting.   |  [BE Week #3 Meeting #1](https://github.com/bounswe/bounswe2022group8/wiki/Week-3-Backend-Meeting-Notes-1) |
 | Documentation | Documentation of our weekly meeting notes.  | [#181](https://github.com/bounswe/bounswe2022group8/issues/181) |
 | Implementation | Made the initials for our Django project. Prepared a detailed _README_ <br> file to make sure that everyone is one the page. | [#179](https://github.com/bounswe/bounswe2022group8/issues/179), [PR](https://github.com/bounswe/bounswe2022group8/pull/180) |
 | Implementation | Dockerized the backend. | [#188](https://github.com/bounswe/bounswe2022group8/issues/188), [PR](https://github.com/bounswe/bounswe2022group8/pull/189) |
 | Implementation & Review | Reviewed the pull request and also made some additions to solve a possible merge conflict.  | [#187](https://github.com/bounswe/bounswe2022group8/issues/187), [PR](https://github.com/bounswe/bounswe2022group8/pull/190) |
 | Implementation | Made some research on Django folder structures and re-organized our directory.  | [#192](https://github.com/bounswe/bounswe2022group8/issues/192), [PR](https://github.com/bounswe/bounswe2022group8/pull/191) |
 | Implementation | Implemented login/logout APIs using tokenization for authentication.  | [#195](https://github.com/bounswe/bounswe2022group8/issues/195), [#199](https://github.com/bounswe/bounswe2022group8/issues/199), [PR](https://github.com/bounswe/bounswe2022group8/pull/200) |
|Implementation| Implemented API for registration.  | [#194](https://github.com/bounswe/bounswe2022group8/issues/194), [PR](https://github.com/bounswe/bounswe2022group8/pull/196) |
| Research | Trying to find out what is tokenization, examining previous repositories, asking people from different teams and googling. (I think we should have learned this concept in CmpE352 along with REST APIs.) | - |
 |  Planning |  Attended weekly meeting #4.      |  [Weekly Meeting #4](https://github.com/bounswe/bounswe2022group8/wiki/Week-4--Meeting-Notes-4) |
 |  Documentation | Prepared the deliverables folder, opened a general issue.    |  [#201](https://github.com/bounswe/bounswe2022group8/issues/201) |
 |  Requirements | Reviewed the signup/login requirements and update them.   |  [#202](https://github.com/bounswe/bounswe2022group8/issues/202) |
| Milestone I Documentation | Added _the requirements addressed in this milestone_ subsection to Milestone document. | [#201](https://github.com/bounswe/bounswe2022group8/issues/201) |
| Implementation| Solved an issue in the dockerized database. | [PR](https://github.com/bounswe/bounswe2022group8/pull/206) |
| Implementation| Configured `CORS` settings in backend and help frontend team use the APIs.  | [#206](https://github.com/bounswe/bounswe2022group8/issues/211), [PR](https://github.com/bounswe/bounswe2022group8/pull/210) |
| Review | Reviewed a PR related to CI/CD (not merged yet) |  [PR](https://github.com/bounswe/bounswe2022group8/pull/215) |
| Implementation | Dockerization of frontend and deployment | [#224](https://github.com/bounswe/bounswe2022group8/issues/224), [PR](https://github.com/bounswe/bounswe2022group8/pull/225) |
|  Planning |  Attended weekly meeting #5.    |  [Weekly Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-5-Meeting-Notes-5) |
 |  Planning |  Attended backend weekly meeting #2.   |  [BE Weekly Meeting #2](https://github.com/bounswe/bounswe2022group8/wiki/Week-5--BE-Meeting-%232-(02.11.2022)) |

