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
* Public Workspace: https://documenter.getpostman.com/view/16425196/2s8Z6x1sYP#02d71c3b-ce09-4b8a-a281-189d1c91441a 
* [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/f352c8e9d0e1c7647570?action=collection%2Fimport)
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


## 8. Standards


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
    

</details>

<details>
    <summary> Doğukan Türksoy </summary>
    

   </details>