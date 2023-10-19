# UE-AD-A1-REST

Flask, REST, and OpenAPI TP

# Introduction:

This repository contains the source code and documentation for the Flask, REST, and OpenAPI TP.
The TP includes setting up a REST service (Movie), creating a REST service (Showtime) from an OpenAPI specification, creating a REST service (Booking) from another OpenAPI specification, and creating a REST service (User) that interacts with the Booking and Movie services.

# API and Documentation:

- Movie service (Port 3200)

* This service is used to get information about a movie and add new movies.
* To lookup a movie in the database, hit: http://127.0.0.1:3200/<movie_id>
  GET /movies/7daf7208-be4d-4944-a3ae-c1c2f516f3e6
  Returns the specified movie.
  {
  "director": "Paul McGuigan",
  "id": "7daf7208-be4d-4944-a3ae-c1c2f516f3e6",
  "rating": 6.4,
  "title": "Victor Frankenstein"
  }

- Showtime service (Port 3202)

* This service is used get a list of movies playing on a certain date.
* To lookup all showtimes, hit: http://127.0.0.1:3202/showtimes
  GET /showtimes
  Returns a list of all showtimes by date.
  [
  {
  "date": "20151130",
  "movies": [
  "720d006c-3a57-4b6a-b18f-9b713b073f3c",
  "a8034f44-aee4-44cf-b32c-74cf452aaaae",
  "39ab85e5-5e8e-4dc5-afea-65dc368bd7ab"
  ]
  },
  {
  "date": "20151201",
  "movies": [
  "267eedb8-0f5d-42d5-8f43-72426b9fb3e6",
  "7daf7208-be4d-4944-a3ae-c1c2f516f3e6",
  "39ab85e5-5e8e-4dc5-afea-65dc368bd7ab",
  "a8034f44-aee4-44cf-b32c-74cf452aaaae"
  ]
  }
  ]

* To get movies playing on a certain date:
  GET /showtimes/20151130
  Returns all movies playing on the date.
  {
  "date": "20151130",
  "movies": [
  "720d006c-3a57-4b6a-b18f-9b713b073f3c",
  "a8034f44-aee4-44cf-b32c-74cf452aaaae",
  "39ab85e5-5e8e-4dc5-afea-65dc368bd7ab"
  ]
  }

- Booking service (Port 3201)

* To lookup booking information for users and add new bookings.
* To get all bookings in the system : http://127.0.0.1:3201/bookings
  GET /bookings
  Returns a list of all booking information in the system.
  [
  {
  "dates": [
  {
  "date": "20151201",
  "movies": [
  "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
  ]
  }
  ],
  "userid": "chris_rivers"
  },
  {
  "dates": [
  {
  "date": "20151201",
  "movies": [
  "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
  ]
  },
  {
  "date": "20151202",
  "movies": [
  "276c79ec-a26a-40a6-b3d3-fb242a5947b6"
  ]
  }
  ],
  "userid": "garret_heaton"
  }
  ]

* To get booking information for a user:
  GET /bookings/chris_rivers
  {
  "dates": [
  {
  "date": "20151201",
  "movies": [
  "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
  ]
  }
  ],
  "userid": "chris_rivers"
  }

* To add a new booking for a user : http://127.0.0.1:3201/bookings/<user_id>
  POST /bookings/chris_rivers
  Body :
  {
  "date": "20151201",
  "movies": "a8034f44-aee4-44cf-b32c-74cf452aaaae"
  }

- User service (Port 3203)

* To lookup informations about the users and their bookings.
* To lookup information about a user: http://127.0.0.1:3203/user/<user_id>
  GET /user/chris_rivers
  {
  "id": "chris_rivers",
  "last_active": 1360031010,
  "name": "Chris Rivers"
  }

* To get user reservation by date : http://127.0.0.1:3203/user/reservations/<user_id>
  GET /user/reservations/chris_rivers
  Body :
  {
  "date" : "20151201"
  }
  Result :
  [
  {
  "date": "20151201",
  "movies": [
  "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
  ]
  }
  ]

* To get films informations from the booking of a user : http://127.0.0.1:3203/user/reservation_details/<user_id>
  GET /user/reservation_details/chris_rivers
  Returns a list of date and movie informations.
  {
  "date": "20151201",
  "movies": [
  {
  "director": "Ryan Coogler",
  "id": "267eedb8-0f5d-42d5-8f43-72426b9fb3e6",
  "rating": 8.8,
  "title": "Creed"
  }
  ]
  }
