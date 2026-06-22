# Azure Inventory Reporter

A Python-based Azure inventory and reporting tool that authenticates to Microsoft Azure, collects infrastructure information, and exports the results into multiple report formats.

## Features

- Authenticate to Azure using the Azure SDK
- Enumerate Azure Resource Groups
- Enumerate Azure Virtual Machines
- Export inventory data to JSON
- Export VM inventory to CSV
- Modular project structure for future expansion
- Foundation for infrastructure reporting and cloud asset management

## Technologies Used

- Python 3
- Azure SDK for Python
- Azure Identity
- Azure Resource Management SDK
- Azure Compute Management SDK
- JSON
- CSV

## Project Structure

```text
azure-inventory-reporter/
├── src/
│   ├── auth.py
│   ├── inventory.py
│   ├── exporters.py
│   └── report.py
│
├── output/
│
├── samples/
│
├── main.py
├── requirements.txt
└── README.md
```

## How It Works

1. Authenticate to Azure using `DefaultAzureCredential`
2. Connect to the target subscription
3. Collect inventory information:
   - Resource Groups
   - Virtual Machines
4. Store results in a Python inventory object
5. Export results to:
   - JSON
   - CSV

## Installation

### Clone the Repository

```bash
git clone https://github.com/JoshuaKDev/azure-inventory-reporter.git
cd azure-inventory-reporter
```

### Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Authenticate to Azure

```bash
az login
```

### Configure Subscription ID

Update the following variable in `main.py`:

```python
SUBSCRIPTION_ID = "YOUR_SUBSCRIPTION_ID"
```

## Usage

Run the application:

```bash
python main.py
```

Example output:

```text
Resource Groups

rg-terraform-lab (centralus)
NetworkWatcherRG (centralus)

Virtual Machines

{'name': 'vm-lab', 'location': 'centralus'}
```

## Generated Reports

### JSON Inventory

```text
output/inventory.json
```

Contains structured inventory data for all collected resources.

### CSV Export

```text
output/virtual_machines.csv
```

Contains Virtual Machine inventory data in spreadsheet-friendly format.

## Example Workflow

```text
Azure Subscription
        ↓
Azure SDK Authentication
        ↓
Resource Collection
        ↓
Inventory Object
        ↓
JSON Export
        ↓
CSV Export
```

## Future Enhancements

- Markdown report generation
- Storage account inventory
- Virtual network inventory
- Network Security Group inventory
- Public IP inventory
- Subscription summary reporting
- Configuration through environment variables
- HTML dashboard export

## Learning Objectives

This project demonstrates:

- Cloud automation
- Azure SDK development
- Python scripting
- API integration
- Data serialization
- Infrastructure reporting
- Cloud asset inventory management

## Screenshots

### Application Output

_Add screenshot here_

### JSON Export

<img width="407" height="743" alt="Screenshot 2026-06-21 at 9 38 32 PM" src="https://github.com/user-attachments/assets/7a0e40ea-f2db-4009-890c-f1eff6eae79e" />


### CSV Export

_Add screenshot here_

## Author

Joshua Kitchen

- GitHub: https://github.com/JoshuaKDev
- Website: https://www.jkcloudsecurity.com
