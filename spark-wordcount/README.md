## Spark Word Count Application

### Before building:
* Put your text file into the folder with Dockerfile

### To build the container:
* Open Command Line and go into the folder with the Dockerfile
* Run the following command: `docker build .`

### To create the container:
* Run the following command: `docker container create -i -t --name <your_name> <image_id>`

### To run the container:
* First run command: `docker container start <container_name>`
* Then: `docker exec -it <container_name> bash`

### To run the program:
* Run the following command: `python spark_wordcount.py <your_text_file>`
* Output will be inside `output` folder in a file called `part-00000`
* Before another run to have to delete `output` folder and its content

### Tips:
* There is a sample text file inside the folder called `text.txt`