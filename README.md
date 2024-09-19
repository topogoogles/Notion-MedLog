# Notion MedLog

A Python application for logging timestamps to Notion databases. Such logging may be used for medicine intake timestamp records, further consistency evaluation, control and analysis, etc.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This project provides a simple Python application that logs timestamps to Notion databases. It's designed to be easily integrated into existing healthcare workflows, allowing quick and efficient recording of patient data directly to Notion pages.

## Features

- Logs medicine in-take timestamps or any similar activity that require logging to Notion databases
- Supports timestamped entries
- Configurable database ID and authentication token
- Easy-to-use command-line interface

## Requirements

To run this application, you'll need:

- Python 3.6+
- Notion API access token
- Notion database ID

These requirements can be installed using pip:
`pip install -r requirements.txt`

## Setup Instructions

1. Clone the repository:
`git clone https://github.com/topogoogles/notion-medlog.git`
`cd notion-medlog`
2. Create a `.env` file in the project root directory:
`NOTION_TOKEN=your_notion_integration_token_here`
`DATABASE_ID=your_database_id_here`
Your Database ID can be found in the URL of your Notion database page, usually this is the string immediately following the username or workspace identifier and before any query parameters
3. Install the required packages:
`pip install -r requirements.txt`
4. Ensure you have the necessary permissions to read from and write to the specified Notion database (Use the `Configuration` tab when creating the integration [https://www.notion.so/profile/integrations]).

## Usage

To log a new entry, simply run the script with the desired timestamp (in the *"YYYY-MM-DD hh:mm:ss"* format, wrapped in double quotes) or run the app without passing the timestamp parameter, it will log by default the time and date the app was run:

`python app.py "2023-05-15 10:30:00"`

This will create a new page in your specified Notion database with the given timestamp. Make sure the database has a __timestamp__ property set.

For more information on available commands, run:

`python app.py --help`

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Notion API documentation
- Python community resources
