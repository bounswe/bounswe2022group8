# Group 8 - Milestone 3 - Group Review

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


**Important:** 
* Final deployment tagged version link: https://github.com/bounswe/bounswe2022group8/releases/tag/customer-presentation-3
* [Project Plan](https://github.com/bounswe/bounswe2022group8/wiki/CmpE-451-Project-Plan)
* [Requirements](https://github.com/bounswe/bounswe2022group8/wiki/Requirements)
* [Use Case Diagram](https://github.com/bounswe/bounswe2022group8/wiki/Use-case-diagram)
* [Sequence Diagram](https://github.com/bounswe/bounswe2022group8/wiki/Sequence-Diagrams)
* [Class Diagram](https://github.com/bounswe/bounswe2022group8/wiki/Class-Diagram)

## 1. Executive Summary
### *Description*


### *Changes since Milestone 2 (Current Status)*


#### Backend

#### Web frontend

#### Mobile


### *Future Plans*



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
 
</details>

<details>
    <summary> Sena Mumcu </summary>
 
</details>

<details>
    <summary> Furkan Keskin </summary>
 


</details>   
    
<details>
    <summary> Karahan Sarıtaş </summary>

|  Task Type   | Task Description   |Related Link(s) |
 |  :----:        |  :----:   |  :----: |
 |  Planning |  Documentation of the Week 11 BE Meeting.  |  [Week 11 BE Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-11-BE-Meeting-%235-(13.12.2022)) |
|  Implementation | Implementation of exhibition related APIs  | [#343](https://github.com/bounswe/bounswe2022group8/issues/343), [PR](https://github.com/bounswe/bounswe2022group8/pull/344), [PR](https://github.com/bounswe/bounswe2022group8/pull/385) |
| Implementation | Implementation of Annotation Service, writing unittests, documenting the APIs using Swagger, dockerizing the application, helping during the deployment and helping the integration with frontend. | [#348](https://github.com/bounswe/bounswe2022group8/issues/348), [PR](https://github.com/bounswe/bounswe2022group8/pull/359), [PR](https://github.com/bounswe/bounswe2022group8/pull/389) |
| Implementation | Fixing a bug related to Nginx on web | [#388](https://github.com/bounswe/bounswe2022group8/issues/388), [PR](https://github.com/bounswe/bounswe2022group8/pull/387) |
| Implementation | Implementation of an additional API that returns the artitems based on tags. | [#367](https://github.com/bounswe/bounswe2022group8/issues/367), [PR](https://github.com/bounswe/bounswe2022group8/pull/368)   |
| Implementation | Implementing unit tests for all APIs I've implemented so far. | [#370](https://github.com/bounswe/bounswe2022group8/issues/370), [PR](https://github.com/bounswe/bounswe2022group8/pull/382) | 
| Documentation | Creating a MIT license for the project | [#365](https://github.com/bounswe/bounswe2022group8/issues/365) |
| Documentation | Documenting the API endpoints and giving example inputs/outputs for Milestone | [#407](https://github.com/bounswe/bounswe2022group8/issues/407) |
| Documentation | Creating a tag that marks the final release version | [#413](https://github.com/bounswe/bounswe2022group8/issues/413) | 
| Documentation | Updating the class diagram with respect to the final version of our program | [#419](https://github.com/bounswe/bounswe2022group8/issues/419) |
| Documentation | Revising annotation related requirements |  [#414](https://github.com/bounswe/bounswe2022group8/issues/414) |
| Milestone | Overall maintenance of the project and fixing last-minute bugs if any |  - |
| Code Review | Reviewed a majority of the PRs belonging to backend/frontend/mobile. For specific details, please refer to each individual link. | [BE-36](https://github.com/bounswe/bounswe2022group8/pull/364), [BE-35](https://github.com/bounswe/bounswe2022group8/pull/358), [BE-32](https://github.com/bounswe/bounswe2022group8/pull/354), [BE-38](https://github.com/bounswe/bounswe2022group8/pull/371), [FE-19](https://github.com/bounswe/bounswe2022group8/pull/389), [BE-33](https://github.com/bounswe/bounswe2022group8/pull/381), [BE-40](https://github.com/bounswe/bounswe2022group8/pull/386), [BE-43](https://github.com/bounswe/bounswe2022group8/pull/404), [MOB-28](https://github.com/bounswe/bounswe2022group8/pull/411), [FE-32](https://github.com/bounswe/bounswe2022group8/pull/415), [FE-33](https://github.com/bounswe/bounswe2022group8/pull/417) |  


</details>



<details>
    <summary> Doğukan Türksoy </summary>
 

</details>



<details>
    <summary> Mustafa Cihan </summary>
  
    
</details>


## 3. Status of Deliverables



## 4. Progress According to Requirements

* The requirements page of the application [here](https://github.com/bounswe/bounswe2022group8/wiki/Requirements).
* Requirements satisfied so far: [Realized Requirements](https://github.com/bounswe/bounswe2022group8/wiki/Realized-Requirements)

## 5. API Endpoints
**@author: Karahan Sarıtaş**

* You can find the documentations of our API endpoints in the following URLs:
   * Application APIs: http://34.125.134.88:8000/api/v1/swagger/schema/ 
   * Annotation APIs: http://34.125.134.88:7000/api/v1/swagger/schema/

* We used Swagger to document our APIs and provide exemplary inputs/outputs for other teams. Please notice that you have to authorize yourself in order to test some of the APIs (since these can be called only by logged-in users in our application - not by guest users).
* There is this button called ```Authorize``` on the right corner in Swagger page. We have to use it to test APIs that require authorization. For example, in order to test the ```logout``` API, first you have to log in to the application and have a token with you. Try the ```login``` endpoint first, copy paste the token returned to you and click on the ```Authorize``` button. Input the token in the following format: "Token xxx". Replace `xxx` with the token and don't forget to put a space between the first word and your token. You can refer to this [PR](https://github.com/bounswe/bounswe2022group8/pull/245) for more details if you want.
* By using Swagger, you can test any API you want either with the example input we provided or some other input that complies with the specification.
* You can use the button below to test any functionality you want. All inputs are already prepared for you - you just have to sign-in or register to the application and use the generated token for authentication-required APIs. <br>
* You can find our collection as a [json file](https://raw.githubusercontent.com/bounswe/bounswe2022group8/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/CmpE451%20API.postman_collection.json) within this directory.
* Public Workspace: https://documenter.getpostman.com/view/16425196/2s8Z6x1sYP#02d71c3b-ce09-4b8a-a281-189d1c91441a (You can use the `Run in Postman` button at the top-right corner.)
* Let me provide the Postman Collection [here](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_3/CmpE451%20API%20-%20Production.postman_collection.json). `{{host}}` stands for `34.125.134.88`.

---
To give you an example, let me provide some consecutive API calls in a scenario.
1) Firstly, you should be registering to the application using `http://{{host}}:8000/api/v1/auth/register/` endpoint. You can call it with the following body:
```json
{
  "email": "plantinga@cornell.edu.tr",
  "username": "alvin.plantinga",
  "password": "revisionistwestern3",
  "password_confirm": "revisionistwestern3"
}
```
It will return an output in the following format:
```json
{
    "user": {
        "email": "plantinga@cornell.edu.tr",
        "username": "alvin.plantinga"
    },
    "token": "b03191f004b98d4207b178ecd25ff645f464e9d37d9730dc47c8a175f8216b45"
}
```
2. Then you should proceed with creating an art item. Input body is already provided for you. You should just change the token from the headers. Copy paste the generated token from the call above, and update the value of `Authorization` header. Then call the `http://{{host}}:8000/api/v1/artitems/me/upload/` API with the following input:
```json
{
    "title" : "A work of art",
    "description" :"An example of fine art, such as a painting or drawing.",
    "category": "SK",
    "artitem_image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="}
```
Output will be something like this:
```json
{
    "id": 9,
    "owner": {
        "id": 6,
        "username": "alvin.plantinga",
        "name": "",
        "surname": "",
        "profile_path": "avatar/default.png"
    },
    "title": "A work of art",
    "description": "An example of fine art, such as a painting or drawing.",
    "category": "SK",
    "tags": [],
    "artitem_path": "artitem/artitem-9.png",
    "likes": 0,
    "number_of_views": 0,
    "created_at": "27-12-2022 03:26:52",
    "sale_status": "NS",
    "minimum_price": 0,
    "bought_by": null
}
```
To avoid verbosity, the base64 string given above represents an extremely small image. But you can upload real images using the input bodies already provided for you in the collection.
3. Try to create an online exhibition using `http://{{host}}:8000/api/v1/exhibitions/me/online/`. 
```json
{       
    "title" : "Exploring Global Climate Change Through Photography",
    "description" :"Art exhibition at 5th Avenue.",
    "start_date": "2022-12-08T13:00:00.000Z",
    "end_date": "2022-12-19T13:00:00.000Z",
    "collaborators": [],
    "artitems_gallery": [],
    "artitems_upload": [
    {
        "title" : "Portrait of Joel Miller, a ruthless and cynical smuggler eventually tasked with smuggling and protecting Ellie Williams.",
        "description" :"Joel Miller from TLOU universe.",
        "tags": [],
        "category": "OT",
        "artitem_image": 
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="},
    {
        "title" : "Shipwreck",
        "description" :"Realistic depictions of coastal scenes and seascapes.",
        "tags": [],
        "category": "OT",
        "artitem_image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="}],
    "poster": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="
}
```
Output of this call will be something like this:
```json
{
    "id": 1,
    "owner": {
        "id": 1,
        "username": "alvin.plantinga",
        "name": "",
        "surname": "",
        "profile_path": "avatar/default.png"
    },
    "title": "Exploring Global Climate Change Through Photography",
    "description": "Art exhibition at 5th Avenue.",
    "poster": {
        "id": 2,
        "owner": 1,
        "title": "Exploring Global Climate Change Through Photography",
        "description": "Art exhibition at 5th Avenue.",
        "category": "PT",
        "tags": [],
        "artitem_path": "artitem/artitem-10.png",
        "created_at": "27-12-2022 03:28:22"
    },
    "collaborators": [],
    "artitems_gallery": [],
    "start_date": "08-12-2022 16:00:00",
    "end_date": "19-12-2022 16:00:00",
    "created_at": "27-12-2022 03:28:22",
    "updated_at": "27-12-2022 03:28:22",
    "status": "Finished",
    "artitems_upload": [
        {
            "id": 3,
            "title": "Shipwreck",
            "tags": [],
            "description": "Realistic depictions of coastal scenes and seascapes.",
            "category": "OT",
            "artitem_path": "artitem/artitem-11.png",
            "likes": 0,
            "created_at": "27-12-2022 03:28:23"
        },
        {
            "id": 4,
            "title": "Portrait of Joel Miller, a ruthless and cynical smuggler eventually tasked with smuggling and protecting Ellie Williams.",
            "tags": [],
            "description": "Joel Miller from TLOU universe.",
            "category": "OT",
            "artitem_path": "artitem/artitem-11.png",
            "likes": 0,
            "created_at": "27-12-2022 03:28:23"
        }
    ]
}
```
4. You can put your art item on sale starting from a minimum price of 200 dollars, using the API `http://{{host}}:8000/api/v1/artitems/<int:artitemid>/bids/` with the following body:
```json
{
  "sale_status": "FS",
  "minimum_price": 200
}
```
Output will be as follows:
```json
{
"detail": "The art item is successfully put on sale."
}
```
* You can do much more with all those APIs provided in the collection. Keep on exploring!

## 6. User Interface and User Experience


## 7. Annotations
### Frontend
### Mobile
### Backend
* Annotation service is completely up and ready for the usage of frontend/mobile, serving on http://34.125.134.88:7000/. 
* Swagger documentation with detailed input/output examples can be examined on http://34.125.134.88:7000/api/v1/swagger/schema/.
* Unittests covering the functionalities provided by Annotation APIs can be found [here](https://github.com/bounswe/bounswe2022group8/blob/master/App/annotations/api/test.py). 
* The work we have completed towards the application of the W3C
standards with respect to Annotations can be found in the next section.

## 8. Standards

### Annotations
* Annotations are implemented as a separate service located [here](https://github.com/bounswe/bounswe2022group8/tree/master/App/annotations). It uses a separate database than the actual database of the application. Our models can be found [here](https://github.com/bounswe/bounswe2022group8/blob/master/App/annotations/api/models.py).
* `Annotation` model directly represents an annotation relationship, whereas `Body` and `Target` constitute two essential participants of this relationship.
* Annotations may have 0 or more Bodies. Therefore it is created as a `ManyToMany` field. 
*  Annotations have 1 or more Targets. (As a part of our requirements, we only keep one target for each annotation.)
* An `Annotation` object may have different fields based on the use case. Here, you can find the properties of a **serialized** `Annotation` object.

|  Term  |  Type  | Description |
 |  :----:        |  :----:   |  :----: |
|  id | Property | The unique identity of the Annotation. | 
|  @context | Property | The context that determines the meaning of the JSON as an Annotation. | 
|  type | Relationship | The type of the Annotation. Related to `Type` object. | 
|  body | Relationship | The relationship between an annotation and its body. Related to `Body` object.  | 
|  target | Relationship | The relationship between an Annotation and its Target. | 
|  creator | Property | ID of the creator of the annotation. | 
|  created | Property| Date when the annotation is created. | 
|  modified | Property | Date when the annotation is modified. | 

Example:
> Scenario: User with the `user id = 1` and `username = peter.parker`, makes an image annotation. Annotated image is stored at https://cmpe451-production.s3.amazonaws.com/artitem/artitem-1.png (You can't open it directly since it's protected). Annotation consists of a rectangle located at `x = 357.59, y = 252.836, w = 492.50, h = 140.15` and a body associated with it: `"Dedicated to my brother"`. You can examine the resulting annotation down below:
```json
  {
    "id": "#a11bf464-e13e-4cf7-a8a0-7debfacca983",
    "body": [
      {
        "value": "Dedicated to my brother",
        "type": "TextualBody",
        "purpose": "commenting",
        "created": "2022-12-27T13:40:33.220980+03:00",
        "modified": "2022-12-27T13:40:33.221006+03:00",
        "creator": {
          "id": 1,
          "name": "peter.parker"
        }
      }
    ],
    "type": "Annotation",
    "target": {
      "id": "http://34.125.134.88/image1",
      "source": "https://cmpe451-production.s3.amazonaws.com/artitem/artitem-1.png",
      "type": "Image",
      "selector": {
        "value": "xywh=pixel:357.5931091308594,252.83668518066406,492.5091857910156,140.15553283691406",
        "type": "FragmentSelector",
        "conformsTo": "http://www.w3.org/TR/media-frags/"
      }
    },
    "creator": 1,
    "@context": "http://www.w3.org/ns/anno.jsonld"
  }
```
* A `Body` object may have different fields based on the use case. Here, you can find the properties of a `Body` object in our application.

|  Term  |  Type  | Description |
 |  :----:        |  :----:   |  :----: |
|  type | Relationship | The type of the Body. Related to `Type` object. | 
|  value| Property | Text value of the body. | 
|  format | Property | The format of the Web Resource's content. | 
|  creator | Relationship | Creator of the body. It's represented as a relationshio with `Creator` object. | 
|  created | Property| Date when the body is created. | 
|  modified | Property | Date when the body is modified. | 
|  purpose | Relationship | Date when the body is created. | 

An exemplary body object:
```json
{
"value": "Is it autumn though? Additionally, why are people running through the street?",
"type": "TextualBody",
"purpose": "commenting",
"created": "2022-12-27T14:37:30.766288+03:00",
"modified": "2022-12-27T14:37:30.766310+03:00",
"creator": {
    "id": 3,
    "name": "volkan.oge"
    }
}
```

* A `Target` object may have different fields based on the use case. Here, you can find tje properties of a `Target` object in our application.

|  Term  |  Type  | Description |
 |  :----:        |  :----:   |  :----: |
|  source | Property | The type of the Body. Related to `Type` object. | 
|  format | Property | Text value of the body. | 
|  language | Property | The format of the Web Resource's content. | 
|  type | Relationship | The type of the Target. Related to `Type` object. | 
| selector | Relationship | The selector(s) associated with the target. |

Here you can find an exemplary target from our application:
> Scenario: A user annotates the word `autumn` on an art item description. Starting and ending positions are stored as `TextPositionSelector`. Exact word is stored with `TextQuoteSelector`. Source image is https://cmpe451-production.s3.amazonaws.com/artitem/artitem-5.png. This means that the description (or title) of this art item is annotated.
```json
"target": {
    "id": "http://34.125.134.88/image8",
    "source": "https://cmpe451-production.s3.amazonaws.com/artitem/artitem-5.png",
    "type": "Image",
    "selector": [
        {
            "exact": "autumn",
            "type": "TextQuoteSelector"
        },
        {
            "start": 22,
            "end": 28,
            "type": "TextPositionSelector"
        }
    ]
}
```
* We also created `Type`, `Motivation`, `FragmentSelector`, `TextQuoteSelector`, `TextPositionSelector`, `Selector` and `Creator` models to represent the relationships between the models.

## 9. Individual Reports 

<details>
    <summary> Serdar Akol </summary>

</details>

<details>
    <summary> Elif Bayraktar </summary>
 
    

</details>



<details>
    <summary> Mustafa Cihan </summary>

</details>


<details>
    <summary> Metehan Dündar </summary>
    


</details>

<details>
    <summary> Mustafa Emre Erengül </summary>

    
</details>

<details>
    <summary> Furkan Keskin </summary>

</details>


<details>
    <summary> Sinem Koçoğlu </summary>
    



</details>

<details>
    <summary> Sena Mumcu </summary>


    
</details>

<details>
    <summary> Karahan Sarıtaş </summary>
    
I am [Karahan Sarıtaş](https://github.com/bounswe/bounswe2022group8/wiki/Karahan-Sar%C4%B1ta%C5%9F), a member of group 8. I'm working in the backend team, also trying to help frontend whenever it's needed.

### Responsibilities
* Maintenance of our Amazon S3 bucket throughout the development.
* Implementation of exhibition related APIs (both virtual exhibitions and offline exhibitions).
* Implementation of annotation service: 
   * Implementing a new Django application from scratch and configuring a separate database. ,
   * Implementation of models in compliance with [WADM](https://www.w3.org/TR/annotation-model/).
   * Implementation of image/text annotation APIs. 
   * Documentation using Swagger.
   * Dockerizing the application and helping the deployment.
   * Taking actions whenever it's necessary during the integration of annotations with frontend.
* Implementation of GET Art items by tag API.
* Implementation of backend unittests.
* Solving the refresh problem on web.
* Creating a license for the project.
* Creating a tag that marks the final release version.
* Revising requirements related to annotations.
* Actively communicating with frontend during the integrations and updating/correcting the existing functions via bugfix/hotfix upon requests.
* Updating the class diagram.
* Documentation of our application of W3C standards with respect to annotations.
* Documentation of our API endpoints and providing examples in the Group Review document.
* Reviewing all of the pull requests created by backend team, in addition to some pull requests created by frontend.

### Main Contributions

    
**Code Related Issues**
* [BE-30: [API] Implementation of Exhibition Related APIs](https://github.com/bounswe/bounswe2022group8/issues/343)
* [BE-31: [API] Implementation of Annotation Service](https://github.com/bounswe/bounswe2022group8/issues/348)
* [BE-34: Meeting Notes: Week #11 Meeting #5](https://github.com/bounswe/bounswe2022group8/issues/356)
* [BE-37: [API] GET Art Items by Tag](https://github.com/bounswe/bounswe2022group8/issues/367)
* [BE-39: Backend Unit Tests](https://github.com/bounswe/bounswe2022group8/issues/370)
* [BE-41: [API] Exhibitions of Currently Logged-in User](https://github.com/bounswe/bounswe2022group8/issues/384)
* [FE-30: Nginx Refresh Bug](https://github.com/bounswe/bounswe2022group8/issues/388)


**Management Related Issues**
* [MIL-19: Create License](https://github.com/bounswe/bounswe2022group8/issues/365)
* [MIL-20: API Endpoints Documentation](https://github.com/bounswe/bounswe2022group8/issues/407)
* [MIL-21: Final Release Version 0.3.0](https://github.com/bounswe/bounswe2022group8/issues/413)
* [MIL-22: Status of the Requirements](https://github.com/bounswe/bounswe2022group8/issues/414)
* [MIL-23: Milestone 3 Deliverables](https://github.com/bounswe/bounswe2022group8/issues/418)
* [MIL-24: Class Diagram](https://github.com/bounswe/bounswe2022group8/issues/419)

**Pull Requests**
* [feature/BE-30: Exhibitions](https://github.com/bounswe/bounswe2022group8/pull/344)
* [feature/BE-31: Annotation Service](https://github.com/bounswe/bounswe2022group8/pull/359)
* [feature/BE-37: Get Art Item by Tags](https://github.com/bounswe/bounswe2022group8/pull/368)
* [feature/BE-41: Exhibitions of Currently Logged-in User](https://github.com/bounswe/bounswe2022group8/pull/385)
* [bugfix/FE-30: Nginx Refresh Bug](https://github.com/bounswe/bounswe2022group8/pull/387)
* [bugfix/BE-30 - [1]](https://github.com/bounswe/bounswe2022group8/pull/390)
* [bugfix/BE-30 - [2]](https://github.com/bounswe/bounswe2022group8/pull/395)
* [bugfix/FE-19](https://github.com/bounswe/bounswe2022group8/pull/389) (I was both a reviewer and a contributor on this)
* [feature/BE-39: Backend Unittests [1]](https://github.com/bounswe/bounswe2022group8/pull/382)
* [feature/MIL-20: API Endpoints](https://github.com/bounswe/bounswe2022group8/pull/412)
* [MIL-19: Create License](https://github.com/bounswe/bounswe2022group8/issues/365)


**Unit Tests**
* You can find my annotation related unittests [here](https://github.com/bounswe/bounswe2022group8/blob/master/App/annotations/api/test.py).
* You can find my application related unittest [here](https://github.com/bounswe/bounswe2022group8/tree/master/App/backend/api/tests). 
* Overall, I have 56 unittests (17 unittests for annotations and 39 unittests for application). Of course, I can't list all of them here, so let me list the features for which I've implemented unittests:
* `text annotation`
* `image annotation`
* `artitem functionalities` 
* `follow/unfollow`
* `signup/login/logout`
* `profile functionalities`
* `offline exhibitions`
* `online exhibitions`

**Additional**

PR Reviews:
* [feature/BE-36: User Level](https://github.com/bounswe/bounswe2022group8/pull/364)
* [feature/BE-35: Art Item Category](https://github.com/bounswe/bounswe2022group8/pull/358)
* [feature/BE-32 : User History](https://github.com/bounswe/bounswe2022group8/pull/354)
* [feature/BE-38: Bidding System](https://github.com/bounswe/bounswe2022group8/pull/371)
* [bugfix/FE-19](https://github.com/bounswe/bounswe2022group8/pull/389)
* [feature/BE-33](https://github.com/bounswe/bounswe2022group8/pull/381)
* [feature/BE-40: Recommendation System](https://github.com/bounswe/bounswe2022group8/pull/386)
* [feature/BE-43: Backend Unittests [2]](https://github.com/bounswe/bounswe2022group8/pull/404)
* [feature/MOB-28](https://github.com/bounswe/bounswe2022group8/pull/411)
* [Feature/FE-32](https://github.com/bounswe/bounswe2022group8/pull/415)
* [hotfix/FE-33](https://github.com/bounswe/bounswe2022group8/pull/417)
    
Cancelled PR: [feature/BE-26: Full Text Search](https://github.com/bounswe/bounswe2022group8/pull/405)
</details>

<details>
    <summary> Doğukan Türksoy </summary>
    

   </details>
