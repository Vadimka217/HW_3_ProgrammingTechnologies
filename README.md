# HW3: Docker & Bash

Generate zoo animal CSV data and create an HTML report with Docker containers.

## Commands

```bash
./run.sh build_generator    # build generator image
./run.sh run_generator      # generate data/data.csv

./run.sh build_reporter     # build reporter image  
./run.sh run_reporter       # generate data/report.html

./run.sh create_local_data  # generate data.csv locally (without Docker)
./run.sh structure          # show project structure
./run.sh clear_data         # clean data/ folder
./run.sh inside_generator   # show /data from generator container
./run.sh inside_reporter    # show /data from reporter container