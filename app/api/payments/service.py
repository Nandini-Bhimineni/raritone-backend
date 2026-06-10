from datetime import datetime

wallets = []
transactions = []
settlements = []
payout_requests = []


def create_wallet(data):

    wallet = {
        "wallet_id": len(wallets) + 1,
        **data.dict(),
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    wallets.append(wallet)

    return wallet


def get_wallets():
    return wallets


def create_transaction(data):

    transaction = {
        "transaction_id": len(transactions) + 1,
        **data.dict(),
        "status": "Success",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    transactions.append(transaction)

    return transaction


def get_transactions():
    return transactions


def create_settlement(data):

    settlement = {
        "settlement_id": len(settlements) + 1,
        **data.dict(),
        "status": "Pending",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    settlements.append(settlement)

    return settlement


def get_settlements():
    return settlements


def create_payout_request(data):

    payout = {
        "payout_id": len(payout_requests) + 1,
        **data.dict(),
        "status": "Requested",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    payout_requests.append(payout)

    return payout


def get_payout_requests():
    return payout_requests