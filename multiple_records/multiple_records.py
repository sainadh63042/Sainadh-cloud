import json
import random


# open the config json file and load data to variable
with open("config.json", "r") as config_file:
    config_data = json.load(config_file)


# Function to simulate multiple records
def simulate_records(num_repeats, example_records):
    simulated_records = []

    # Generate random dst ip address
    for i in range(num_repeats):
        random_dst1 = "203.0.113." + str(random.randint(1, 5))
        random_dst2 = "198.52.100." + str(random.randint(1, 5))

        # Fill in the placeholders with random dst ip addresses
        for record in example_records:
            record = record.format(dst1=random_dst1, dst2=random_dst2)
            simulated_records.append(record)

    return simulated_records


# Function to write the simulates records
def write_records_in_file(simulated_records):
    # write the simulated records to text file
    output_file = "simulated_records.txt"
    with open(output_file, "w") as file:
        for record in simulated_records:
            file.write(record + "\n")
        file.close()


def main():
    simulated_records = simulate_records(config_data["num_repeats"], config_data["example_records"])
    write_records_in_file(simulated_records)
    print(f"{len(simulated_records)} records has been simulated")


if __name__ == "__main__":
    main()
