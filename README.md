# 🔥 StarConnect 🔥 | [Live Link 🚀](https://badalwanjari.pythonanywhere.com/) 
StarConnect is a web-based platform designed to connect sponsors and influencers for effective collaboration on advertising campaigns. The platform enables sponsors to create campaigns and reach out to influencers for promoting their products or services. Influencers can accept or negotiate ad requests based on their preferences, making it a streamlined process for both parties.

## Table of Contents
- Introduction
- Features
- Technologies Used
- Installation
- Usage
- Flow
- ERD

## Introduction
StarConnect addresses the growing need for an efficient platform that brings together sponsors and influencers. By facilitating smooth communication and negotiation, it ensures that sponsors can effectively promote their products, while influencers can benefit monetarily.

## Features
- Admin Dashboard: View all users, campaigns, ad requests, and flagged content.
- Campaign Management: Sponsors can create, update, or delete campaigns.
- Request Management: Sponsors can create, edit, and delete ad requests, while influencers can accept or negotiate them.
- Search Functionality: Sponsors can search for influencers, and influencers can search for public campaigns.
- Role-Based Access: Different functionalities are available for admins, sponsors, and influencers.

## Technologies Used
- Backend: Flask
- Frontend: Jinja2, Bootstrap, HTML, CSS
- Database: SQLite
- Language: Python

## Installation

- Clone the repository:

```sh
git clone https://github.com/your-username/starconnect.git
```

- Navigate in the project directory/folder

```sh
cd starconnect
```

- Create and activate a virtual environment:

```sh
python3 -m venv myenv
.\myenv\Scripts\activate
```


- Install the required dependencies:

```sh
pip install -r requirements.txt
```

- Run the application:
  
```
python run.py
```
or
```
python flask --app run.py run
```


## Usage
1. Admin: Monitor users and campaigns, flag inappropriate content.
2. Sponsors: Create and manage campaigns, search for influencers, send ad requests.
3. Influencers: Search for public campaigns, accept/reject ad requests, negotiate terms.

## Flow of the app
![Flow diagram](https://github.com/badalwanjari/StarConnect/blob/master/flow.jpg?raw=true)

## ERD
![ERD diagram](https://github.com/badalwanjari/StarConnect/blob/master/ERD.png?raw=true)
