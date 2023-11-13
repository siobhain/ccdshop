# TESTING

## 🚀 TABLE OF CONTENTS

* [RESPONSIVENESS TESTING](#responsiveness-testing)
* [BROWSER COMPABILITY TESTING](#browser-compability-testing)
* [BUGS RESOLVED AND UNRESOLVED](#bugs-resolved-and-unresolved)
* [LIGHTHOUSE REPORTS](#lighthouse-reports)
* [CODE VALIDATION](#code-validation)
* [USER STORIES TESTING](#user-story-testing)
* [FEATURES TESTING](#features-testing)

Return back to the [README.md](README.md) file.

- - -

## RESPONSIVENESS TESTING

<details>
<summary>👇</summary>

Both development and deployed versions of the project were tested on multiple devices & via chrome dev tools for responsiveness issues.

![Responsiveness](amires.JPG)

## BROWSER COMPABILITY TESTING

<details>
<summary>👇</summary>

The deployed project was tested on 3 browsers to check for compatibility issues and works as expected. 

|Browser | Screenshot | 
|:---:|:---: |
| Chrome | ![Chrome](docs/b-chrome.jpg)  |
| FireFox  | ![Firefox](docs/b-firefox.jpg)  |
| Edge  | ![Edge](docs/b-edge.jpg)  |

</details>

- - -

## BUGS RESOLVED AND UNRESOLVED 

☠️ The issues listed  below were indentified during the development of the project.

<details>
<summary>👇</summary>

</details>

- - -

## LIGHTHOUSE REPORTS

<details>
<summary>👇</summary>

Below are Lighthouse reports for the deployed project, lower than I want on performance & accessibility.  Third party code such as stripe utility , fontawesome CDN, bootstrap CDN, JQuery & google fonts effected performance but as they are necessary I was unable to improve on this. There are duplicate ARIA ID's used by ALLAuth which reduced the accessubility score.  The blue on yellow for the footer does not ahve a sufficient contrast ratio, this may not be corrected before submitting.



|Page | Screenshot | 
|:---:|:---: |
|Home |![Guest](docs/l-home.jpg) |
|Products |![Home](docs/l-products.jpg) |
|SignIn  |![Todo](docs/l-signin.jpg) |
|Bag  |![Full](docs/l-bag.jpg) |

</details>

- - -

## CODE VALIDATION

<details>
<summary>👇</summary>

### HTML

[HTML W3C Validator](https://validator.w3.org/) Screenshots

|Page |Screenshot | Notes  | 
|:---:|:----------------------:|---|
| Home  |![HTML Validation - Guest](docs/v-guest.jpg) |Observe on html source 4th line the Title CTB is Guest Home|
| Home Member |![HTML Validation - Main Feed](docs/v-member.jpg) | ||
| Sign  Up | ![HTML Validation - Signup](docs/v-signup.jpg)  |
| Sign  In | ![HTML Validation - Signin](docs/v-signin.jpg)  | Validate by the page source
| Log  In | ![HTML Validation - Signin](docs/v-login.jpg)  | Validate by the address
| Sign  Out | ![HTML Validation - Signout](docs/v-signout.jpg)  |
| Todo |  ![HTML Validation - Todo](docs/v-todo.jpg) | Yes there is a problem here as strictly speaking one should not have a button inside an anchor tag, This button is the Delete Task action.  The original plan was to use a modal when the user requested to delete a Task, but unfortunatley I could not get the Task ID data to the modal, I then had to revert to some sort of basic warning to the user so that where I started to use the tooltip to pop up a message to the user that this action cannot be undone & afaik to get the tooltip working I neede to use the button element.|
| Full |  ![HTML Validation - Full](docs/v-full.jpg) |
| Add Task |  ![HTML Validation - Add Task](docs/v-mewtask.jpg) |
| Update Task |  ![HTML Validation - Full](docs/v-update.jpg) |
| 404 | ![HTML Validation - Error 404](docs/v-404.jpg)  |
| Gate | ![HTML Validation - Gate](docs/v-soon.jpg)  |

- - - 

### CSS


[HTML W3C Validator](https://validator.w3.org/) also used to validate the css as shown :

![style.css](docs/v-css.jpg) |

- - - 

### JAVASCRIPT

The [JShint Validator](https://jshint.com/) was used to validate the JavaScript snippets.

- - - 

### PYTHON

The [Code Institute Python Linter](https://pep8ci.herokuapp.com) was used to validate Python files.

#### CTBPROJECT

| File | Screenshot  | Notes|
| --- | ------ |:---:|
| settings.py |  ![Settings](docs/v-settings.jpg) | Pass |
| urls.py (main) |  ![Urls](docs/v-purls.jpg) | Pass |


#### TASKAPP app

| File | Screenshot  | Notes|
| --- | --- | --- |
| admin.py | ![Admin](docs/v-admin.jpg)  | Pass |
| forms.py | ![Forms](docs/v-forms.jpg)  | Pass |
| models.py | ![Models](docs/v-models.jpg)  | Pass |
| urls.py |  ![Urls](docs/v-urls.jpg) | Pass |
| views.py | ![Views](docs/v-views.jpg)  | Pass |


- - -

## USER STORY TESTING

<details>
<summary>👇</summary>

I found that user stories (US) are a work in progress during the development of the project, I feel in a better position now that I am nearer the end of the project in defining US that I was at the start as having come through that process I now have a better understanding of them with clearly more to learn.  Armed with this knwoeldge I re define the US's here to aid in documenting US testing, Hence these will not follow the same USs as is in the  `@siobhain's CTB project`  [here](https://github.com/users/siobhain/projects/9) & deadline will not allow me to redo (regenerate) the US's on Github Project.

### New Site Users

- - -
As a first time user of the site, I want to be able to:


| User Stories |  Notes|
| --- | --- | 
| understand what the site is for and how to navigate the site, so I can decide whether or not to register / sign up. | Pass |
| register for an account, so that I can add Tasks and further explore the website. |  Pass |
| easily navigate the site, so that I can access what I need at the click of a button. | Pass |


### **Registered Users**

- - -

As a registered user of the site, I want to be able to:

*Must Have*

| User Stories |  Notes|
| --- |  --- |
| log in to my account, so that I can access the website. |Pass |
| log out of my account, so that I can end my session | Pass |
| view the current shared task board for the community group|  Pass |
| create, edit & delete my Tasks so that I have control of my content | Pass |
| see the date a task was created, so that I can know age of a task| Pass |
| view the full task board including completed tasks so I can see what the group has done in the past|  Pass |


*Won't Have this version*

| User Stories |  Notes|
| --- | --- | 
| change or reset password, so that user can regain access to my account | Pass |
| add a user picture so that user will be recognized in community  | Pass |
| see a users list, so that I can see contact details or picture of other members | Pass |
| add a task picture, so that I can better demonstrate work needed to be done | Pass |
| like or dislike other people's tasks, so that I can let them know I suport their task | Pass |
| view the number of likes on each task, so that I can see which is the most widely known about  | Pass |
| comment on other people's tasks, so that I can be involved in the conversation |  Pass |
| read the comments of tasks, so that I can know the thoughts from other members | Pass |

### **Admin User**

- - -

As an administrator for the site I want to be able to:

*Must Have*

| User Stories |  Notes|
| --- | --- | 
| publish and unpublish Tasks | Pass |
| Change the completed status of Tasks | Pass |
| search Tasks by user, status, date| Pass |

</details>
- - -

## FEATURES TESTING

<details>
<summary>👇</summary>

</details>

- - -

## AUTOMATED TESTING

<details>
<summary>👇</summary>

There was not automated testing implemented with this project.

- - -


</details>

Return back to the [README.md](README.md) file.