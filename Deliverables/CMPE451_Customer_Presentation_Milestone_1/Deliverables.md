# Deliverables

Here you can find hyperlinks to our deliverable documents:
* [Software Requirements Specification](https://github.com/bounswe/bounswe2022group8/wiki/Requirements)
* Software Design (UML)
* Scenarios and Mockups
* Project Plan
* Individual Contribution Reports
* Customer Milestone 1 Group Review


# Individual Contributions

<details>
    <summary> Mustafa Cihan </summary>
I am Mustafa Cihan a member of group 8. I am working on mobile application of our project.

### Responsibilities
I am responsible for mobile application. For this milestone I mostly worked on frontend of mobile application. I designed landing page, login page, signup page and home page. Also I implemented pages that I designed.

### Main Contributions
I mainly worked on mobile app so I gave most of my effort to develop mobile application.<br/>

**Code Related Issues**
* [MOB-1: Design and Code Flutter Files for Login and Sign-Up](https://github.com/bounswe/bounswe2022group8/issues/198)
* [MOB-4: Creating a Homepage](https://github.com/bounswe/bounswe2022group8/issues/213)
* [MOB-5: Adding error notifications on login and sign-up]()
* [MOB-3: Connecting Mobile App with Backend](https://github.com/bounswe/bounswe2022group8/issues/208) made [commit](https://github.com/bounswe/bounswe2022group8/commit/ab54c1f7421d943cb31c427005342a2c24466440)  to this issue.

**Management Related Issues**
* [GEN-27: Meeting Notes: Week#4 Meeting#4](https://github.com/bounswe/bounswe2022group8/issues/207)
* [MOB-2: Meeting Notes: Week#3 Mobile Meeting#1](https://github.com/bounswe/bounswe2022group8/issues/205)
* [GEN-25:Revise the Copyright Infringement Requirement](https://github.com/bounswe/bounswe2022group8/issues/178)
* [GEN-21: Create a Wikipage for Conventions](https://github.com/bounswe/bounswe2022group8/issues/173)
* [GEN-3: Week #1 Meeting #1 Notes](https://github.com/bounswe/bounswe2022group8/issues/155)

**Pull Requests**
* [feature/MOB-1](https://github.com/bounswe/bounswe2022group8/pull/204)
* [feature/MOB-4](https://github.com/bounswe/bounswe2022group8/pull/216)
* [feature/MOB-5](https://github.com/bounswe/bounswe2022group8/pull/219)
* Reviewed [Feature/MOB-3](https://github.com/bounswe/bounswe2022group8/pull/221)
</details>
    
<details>
    <summary> Sinem Koçoğlu </summary>
I am Sinem Koçoğlu and I am member of group 8 frontend team.

### Responsibilities
* Creation of first design of login and signup pages.
* Research on frontend tools.
* Providing authentication for login and signup.
* Providing connection to backend.
* Dockerization of frontend.

### Main Contributions
I have created the first view for login and signup pages while creating the frontend project. I shared my knowledge about frontend tools with my teammate. Then, I studied and worked on authentication and tokenizaton for login and sign up. I configured backend and database on local in order to test if authentication and tokenization works well. I did research on dockerization of frontend projects and dockerize it.

**Code Related Issues**
* [FE-2](https://github.com/bounswe/bounswe2022group8/issues/185): Research on Frontend Tools 
* [FE-3](https://github.com/bounswe/bounswe2022group8/issues/186): Design and code CSS Files for Login and Sign Up 
* [FE-4](https://github.com/bounswe/bounswe2022group8/issues/203): Connection Between Backend and Frontend
* [FE-5](https://github.com/bounswe/bounswe2022group8/issues/217): Dockerize frontend

**Management Related Issues**
* [GEN-16](https://github.com/bounswe/bounswe2022group8/issues/168): Revise Profile Management 
* [GEN-17](https://github.com/bounswe/bounswe2022group8/issues/169): Revise Exhibition
* [GEN-25](https://github.com/bounswe/bounswe2022group8/issues/177): Meeting Notes: Week#2 Meeting#3

**Pull Requests**
* [Feature/FE-5](https://github.com/bounswe/bounswe2022group8/pull/218)
* Reviewed [Feature/FE-3](https://github.com/bounswe/bounswe2022group8/pull/220)
* 
**Additional Information**
* First, I have created project in [CodeSandBox](https://codesandbox.io/s/artcommunityplatform-ilgl9c?file=/src/Login.js) to experience css tools.Then, Furkan Keskin took the responsibility of creating design by using css. That's way, he uploaded the project to git.
* I did not create a pr to merge authentication file to the branch 'feature/FE-3' because I have already downloaded updated backend folder to my branch to test if everything worked well. Not to destruct folder structure, Furkan Keskin copied the only authentication file manually to his branch.

</details>
    
# Milestone Group Review

### The requirements addressed in this milestone

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
