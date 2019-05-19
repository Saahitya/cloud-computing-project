# Container Orchestrator  
The project is focused on building a container orchestrator that can perform load
balancing, fault tolerance, and auto-scaling. <br />
Functionalities implemented with container orchestrator :
  - Start and stop Acts containers programmatically, and allocate ports for
them on localhost.
  - Load balance all incoming HTTP requests (to the Acts EC2 instance)
equally between all running Acts containers in a round-robin fashion
  - Monitor the health of each container through a health check API, and if a
container is found to be unhealthy, stop the container and start a new one
to replace it.
  - Increase the number of Acts containers if the network load increases above
a certain threshold.
## Design 
 - Load Balancing : <br /><br />
 One of the main task of the orchestrator is to load balance the incoming
requests among ‘n’ active containers running on different ports starting
from 8000.<br /> This is done by maintaining a data structure which contains container ids
and corresponding ports. Whenever orchestrator gets a request it checks
this data-structure for the active containers and sends the request to one of
the container in round robin fashion.<br /><br />
  - Fault Tolerance : <br /><br /> Fault tolerance is implemented in a separate thread which checks the
health of all the active containers. In case if a container is detected to be
unhealthy, that particular container is killed and a new container is started
which listens to the same port number as of the previous container.<br /><br />
  - Scaling : <br /><br />Scaling is again implemented in a separate thread, unlike fault tolerance
scaling checks for the number of requests to the micro-service every two
minutes.<br /> It checks the current number of containers and required number of
containers (according to given specification). In case if there are more
number of containers needed it creates the required number of containers.
If there are less number of requests needed scaling will kill the unwanted
containers starting from the container which was mapped to greater port
number. <br /><br />
  - There may be race-conditions since the application uses 3 threads.
Appropriate locks have been used to prevent the race-conditions among
threads. <br />
  - Persistence : <br /><br />
  Since all the data written by the containers are temporary and get erased
once the container completes its task, a virtual volume is attached and this
volume will be shared across all the containers.<br /><br />
  - Generic orchestrator engine : <br /><br />
  Takes input a configuration files with starting port number, fault check
interval time, scaling interval time as parameters and sets up the engine accordingly. If the configuration file is not given then these parameters are
set to their default values as mentioned in the specification.<br /><br />
  - Integration with the mobile app : <br /><br />
  Backend was successfully integrated with the given frontend and 100 images
across different categories were uploaded using the app.
  
