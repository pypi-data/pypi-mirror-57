
rmqworkers -- Manage dynamic workers rabbitmq for Python applications
=====

![status](https://img.shields.io/badge/rmqworkers-stable-success)



Project rmqworkers offer high availability through simple, yet powerful library:
    This library doesn't work as a standalone.
    
This project require a rabbitmq server.

Please note that for development I've used a container:

How to run
-----


docker run -d --hostname my-rabbit --name rabbitmq-server -p 15672:15672 -p 5672:5672 rabbitmq:3-management

Default has credentials:
    user:  quest
    passw: quest

cd rmqworkers/examples

source venv/bin/activate or venv/Scripts/activate.sh

pip install -r requirements.txt

python example_1queue_in_and_1queue_out.py  

Expected output
--
Default will use thread.

publish in queue in { "job_info": "11111"}

Verify if in queue out is {'job_info': '11111!!!!!!!', 'add_something': 'something'}