# The Eye

I went ahead and created a mock Django application, serving different skeleton views, and implemented the_eye as a function within the project, to be called on various views
that we wish to monitor. It takes request data and tags (

## Assumptions
* I imagine that there would be a database configuration that I would work with, and that the_eye would spit out to
* I assumed whatever front-end application was running would have events tagged, and that I could take such tags and define the 'category' payload section with them

## TODO:
* Add the database configuration
* Handling large amounts of events in quick succession:
* 1)  Slugify URLs or figure out an optimal way of handling events to avoid collisions and race conditions.
* 2)  Another possibility is tying events to a session, and only after session termination would events be loaded into the database.
* 3)  A final possiblity is implementing threading for large amounts of requests. This would be potentially okay for sites where the range of events varied little from the average, but not especially feasible where event requests suddenly spiked.

I spent a large period of time studying up on my skills and re-teaching myself things for the best contribution here. My style tries to represent transparency
of my thought process, and of programming process for collaboration with the most clarity. After coming up to speed with Django from Flask, I decided this would be the best way of handle the events.


