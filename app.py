from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/spendwise"  # Use your MongoDB URI here
mongo = PyMongo(app)

@app.route('/')
def dashboard():
    transactions = mongo.db.transactions.find()  # Fetch all transactions from MongoDB

    # Calculate account balances
    balances = {}
    for transaction in transactions:
        account = transaction['account']
        amount = transaction['amount']
        if account not in balances:
            balances[account] = 0
        if transaction['type'] == 'Income':
            balances[account] += amount
        else:
            balances[account] -= amount

    # Fetch the data again for rendering
    transactions = mongo.db.transactions.find()
    
    return render_template('index.html', transactions=transactions, balances=balances)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    account = request.form['account']
    amount = float(request.form['amount'])
    reason = request.form['reason']
    transaction_type = request.form['type']

    # Save transaction to MongoDB
    mongo.db.transactions.insert_one({
        'account': account,
        'amount': amount,
        'reason': reason,
        'type': transaction_type
    })

    return redirect(url_for('dashboard'))

@app.route('/delete_log', methods=['POST'])
def delete_log():
    # Delete all transactions from MongoDB
    mongo.db.transactions.delete_many({})  # Delete all documents from transactions collection
    
    return redirect(url_for('dashboard'))

@app.route('/transfer_funds', methods=['POST'])
def transfer_funds():
    from_account = request.form['from_account']
    to_account = request.form['to_account']
    transfer_amount = float(request.form['transfer_amount'])

    # Update balances in database
    db.accounts.update_one({"name": from_account}, {"$inc": {"balance": -transfer_amount}})
    db.accounts.update_one({"name": to_account}, {"$inc": {"balance": transfer_amount}})

    # Log the transaction
    db.transactions.insert_one({
        "account": from_account,
        "amount": -transfer_amount,
        "reason": f"Transferred to {to_account}",
        "type": "Expense"
    })
    db.transactions.insert_one({
        "account": to_account,
        "amount": transfer_amount,
        "reason": f"Transferred from {from_account}",
        "type": "Income"
    })

    return redirect(url_for('dashboard'))



if __name__ == "__main__":
    app.run(debug=True)
