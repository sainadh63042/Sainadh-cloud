#Description

This Python script is designed to generate simulated log records for testing and development purposes.
It creates multiple log records based on a set of example log templates, 
filling in specific placeholders with random values. 
The generated log records are then written to an output file.

#configuration

You can customize the script's behavior by editing the config.json file.
Specify the number of times you want to repeat the log generation process and define example 
log templates with placeholders for dynamic values.

example:
{
   "num_repeats": 10,
   "example_records": [
       "Example record with dst1: {dst1} and dst2: {dst2}"]
       // Add more example records here
}

#Output

The simulated log records will be written to the simulated_records.txt file.

#commands to build and run docker image

1. sudo docker bulid -it multiple_records_img
2. sudo docker run -v /home/user/ipaddress_count:/container name -it multiple_recordds_img

