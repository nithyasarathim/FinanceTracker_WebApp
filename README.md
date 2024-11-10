
# SpendWise Web Application

SpendWise is a web application in the realm of instantaneous personal finance management using Flask as the programming framework. It can assist users how to manage their expenditure, maintain and operate accounts and also how to transfer money easily. The application involves creation of account, recording and entering of transactions, balance check as well as executing transfer of funds across accounts.

## Features

- **Account Management**: Have many accounts to work with and assign some of them high balances and others low balances.
- **Income and Expense Tracking**: Record and document all forms of income and expenditure that relate to any account.
- **Fund Transfer**: Transfer specified sums of money as well as constantly moving money from one account to another.
- **MongoDB Integration**: All data collected are saved in MongoDB which makes it persistent across sessions.
- **Responsive Design**: Easy to use and interactive layout for proper navigation on both web and mobile platforms.

## Installation

To run the project locally, follow these steps:

### Prerequisites

- Python 3.6 or higher
- MongoDB (to use MongoDB you should ensure it is running locally or use an instance from the cloud)

### Steps

1. Clone the repository:
   **`git clone https://github.com/nithyasarathim/FinanceTracker_WebApp.git`**
   **`cd spendwise`**

2. Create and activate a virtual environment:

   - For **Windows**:
     **`py -m venv venv`**  
     **`venv\Scripts\activate`**

   - For **macOS/Linux**:
     **`python3 -m venv venv`**  
     **`source venv/bin/activate`**

3. Install the required packages:
   **`pip install -r requirements.txt`**

4. Set up MongoDB:

   If you’re following these steps with a local MongoDB instance, you want to make sure that MongoDB is actually running.  
   For cloud MongoDB, update the `MONGO_URI` in the `config.py` file to have the link of your cloud database.

5. Run the application:
   **`python app.py`**

   The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

### Account Management

The account page should be accessed to create as well as administer accounts.  
This feature allows you to view your balance in each of the accounts as of now.

### Transactions

Record your income and your expenditure under the respective account to be provided.  
To fund your accounts, use the **Transfer Funds** tab or to transfer funds between your accounts.

### Fund Transfer

Under the transferring part, choose the **From Account** and the **To Account**, then enter the particular sum you would like to transfer.  
The dropdown will change based on the account that is available in the system.

## Technologies Used

- **Flask**: A lightweight Python-based framework for web applications.
- **MongoDB**: Database used for storage of data different from the traditional SQL models.
- **HTML/CSS**: For creating the front-end view for the application.
- **JavaScript**: For the change of data in the page, like when we need to update drop-downs.

## License

The project is under the MIT License as indicated in the LICENSE file.

## Acknowledgments

- I am grateful to the Flask and MongoDB community for giving out powerful frameworks.
- Grateful to all the open source contributors for their valuable materials.
