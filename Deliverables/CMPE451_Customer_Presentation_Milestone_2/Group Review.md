# Group 8 - Milestone 2 - Group Review

### Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [List and status of deliverables](#2-list-and-status-of-deliverables)
3. [Evaluation of the status of deliverables and its impact on your project plan](#3-evaluation-of-deliverables-and-impact)
4. [Evaluation of tools and processes you have used to manage your team project](#4-evaluation-of-tools-and-processes)
5. [The requirements addressed in this milestone](#5-the-requirements-addressed-in-this-milestone)
6. [Overall description of responsibilities that are assigned to each member](#6-responsibilities)
7. [A Summary of work performed by each team member](#7-summary-of-work)

## 1. Executive Summary
### *Description*


### *Overall Status*


### *Future Plans*




## 2. List and Status of Deliverables
|Deliverable|Status|Date Delivered| 
|-----|:--------:|:------:| 
| _to be continued_ | _to be continued_ | _to be continued_|




## 3. Evaluation of Deliverables and Impact
### Software Requirements Specification

### Software Design (UML)

### Scenarios and Mockups

### Project Plan

### Individual Contributions Reports

### Group Review



## 4. Evaluation of Tools and Processes

### 1) Mobile Team
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
### 2) Backend Team

<details>
    <summary> Visual Studio Code (VSCode) </summary>
    We used Visual Studio Code as our IDE for the development. With its extensions for Python and for Github, VSCode enabled the backend team write code easily. It also provided smart code completion, on-the-fly error checking which overall helped us focus on the implementation.
</details>

<details>
    <summary> Python Django & Rest Framework </summary>
 To implement the backend of our web application we used Django framework which provides many built-in function that helped the backend team implement the web application easily. We could integrate the application with PostgreSQL without any issues and additional code fabric. With the help of migration files we were able to create models and switch between different databases.
    
We decided to use Django Rest framework because of its flexibility. With Django framework, Rest is one of the most used frameworks for web applications. That is why there is a big community online and we got a lot of support from the community with explanation videos, error messages etc. We were able to use knox and implement logout API endpoint in one line of code easily.
</details>

<details>
    <summary> PostgreSQL </summary>
    PostgreSQL is an open-source object-relational database system that supports both relational and non-relational querying. It supports the programming language that we used (Python) and we were able to integrate out Django application with our database. There is also a big support community online that use PostgreSQL with Django applications, thus we could get help from online videos while working on DB-app connection. PostgreSQL is also reliable and secure which helped us focus on implementation rather than possible security issues that we could face.
    
</details>

<details>
    <summary> Postman </summary>
During API testing, we used Postman frequently because it offers an easy user interface and allows us send calls to out API functions. It also supports different types of inputs which made our job easier, we could send data in the same format overall. 
</details>


### 3) Frontend Team
   
<details>
       <summary>  VS Code  </summary>
    Microsoft Visual Studio Code is an useful editor to manage the project with backend side because we can run both sides on the same window when we want to test if frontend and backend connected successfully. Also, it is easy to install extensions such as Eslint used to find and fix problems in javascript code and Prettier that is a code formatter. What's more, VS code is convenient to carry out git management. 
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
    
## 5. The Requirements Addressed in this Milestone
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

## 6. Responsibilities


## 7. Summary of Work

