# StarConnect
StarConnect is a web-based platform designed to connect sponsors and influencers for effective collaboration on advertising campaigns. The platform enables sponsors to create campaigns and reach out to influencers for promoting their products or services. Influencers can accept or negotiate ad requests based on their preferences, making it a streamlined process for both parties.

## Table of Contents
- Introduction
- Features
- Technologies Used
- Installation
- Usage

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

``git clone https://github.com/your-username/starconnect.git``

- Navigate in the project directory/folder
``cd starconnect``

- Create and activate a virtual environment:
``python3 -m venv myenv``

``source myenv/bin/activate  # On Windows: myenv\Scripts\activate``

- Install the required dependencies:
``pip install -r requirements.txt``

- Run the application:
``python run.py``


Usage
1. Admin: Monitor users and campaigns, flag inappropriate content.
2. Sponsors: Create and manage campaigns, search for influencers, send ad requests.
3. Influencers: Search for public campaigns, accept/reject ad requests, negotiate terms.
