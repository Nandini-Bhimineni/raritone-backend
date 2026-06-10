from datetime import datetime
import uuid

wallets_db = []
transactions_db = []
settlements_db = []
payouts_db = []
refunds_db = []

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- WALLET OPERATIONS ---
def create_wallet_service(data):
    for w in wallets_db:
        if w["customer_id"] == data.customer_id:
            return {"error": "Wallet already exists"}
    t = get_timestamp()
    wallet = {"id": len(wallets_db)+1, "customer_id": data.customer_id, "balance": float(data.initial_balance), "created_at": t, "updated_at": t}
    wallets_db.append(wallet)
    return wallet

def get_all_wallets_service(): return wallets_db
def get_wallet_by_customer_service(c_id): return next((w for w in wallets_db if w["customer_id"] == c_id), None)
def get_balance_service(c_id):
    w = get_wallet_by_customer_service(c_id)
    return {"customer_id": c_id, "balance": w["balance"]} if w else None

def add_money_service(data):
    w = get_wallet_by_customer_service(data.customer_id)
    if not w: return None
    w["balance"] += float(data.amount)
    w["updated_at"] = get_timestamp()
    return w

def deduct_money_service(data):
    w = get_wallet_by_customer_service(data.customer_id)
    if not w: return {"error": "Wallet not found"}
    if w["balance"] < data.amount: return {"error": "Insufficient funds"}
    w["balance"] -= float(data.amount)
    w["updated_at"] = get_timestamp()
    return w

# --- TRANSACTION OPERATIONS ---
def create_transaction_service(data):
    t = get_timestamp()
    tx = {
        "id": len(transactions_db)+1,
        "transaction_id": f"TXN-{uuid.uuid4().hex[:8].upper()}",
        **data.dict(),
        "created_at": t,
        "updated_at": t
    }
    transactions_db.append(tx)
    return tx

def get_all_transactions_service(): return transactions_db
def get_transaction_by_id_service(tx_id): return next((tx for tx in transactions_db if tx["transaction_id"] == tx_id), None)
def get_tx_by_customer_service(c_id): return [tx for tx in transactions_db if tx["customer_id"] == c_id]
def get_tx_by_vendor_service(v_id): return [tx for tx in transactions_db if tx["vendor_id"] == v_id]
def get_tx_by_status_service(status): return [tx for tx in transactions_db if tx["status"].lower() == status.lower()]

# --- SETTLEMENT OPERATIONS ---
def create_settlement_service(data):
    t = get_timestamp()
    st = {
        "id": len(settlements_db)+1,
        "settlement_id": f"SET-{uuid.uuid4().hex[:8].upper()}",
        **data.dict(),
        "status": "Settled",
        "created_at": t,
        "updated_at": t
    }
    settlements_db.append(st)
    return st

def get_all_settlements_service(): return settlements_db
def get_settlement_by_id_service(st_id): return next((s for s in settlements_db if s["settlement_id"] == st_id), None)
def get_settlements_by_vendor_service(v_id): return [s for s in settlements_db if s["vendor_id"] == v_id]

# --- PAYOUT OPERATIONS ---
def create_payout_service(data):
    t = get_timestamp()
    po = {
        "id": len(payouts_db)+1,
        "payout_id": f"PAY-{uuid.uuid4().hex[:8].upper()}",
        **data.dict(),
        "status": "Pending",
        "created_at": t,
        "updated_at": t
    }
    payouts_db.append(po)
    return po

def get_all_payouts_service(): return payouts_db
def get_payouts_by_vendor_service(v_id): return [p for p in payouts_db if p["vendor_id"] == v_id]
def update_payout_status(po_id, status):
    po = next((p for p in payouts_db if p["payout_id"] == po_id), None)
    if not po: return None
    po["status"] = status
    po["updated_at"] = get_timestamp()
    return po

# --- REFUND OPERATIONS ---
def create_refund_service(data):
    t = get_timestamp()
    rf = {
        "id": len(refunds_db)+1,
        "refund_id": f"REF-{uuid.uuid4().hex[:8].upper()}",
        **data.dict(),
        "status": "Refunded",
        "created_at": t,
        "updated_at": t
    }
    refunds_db.append(rf)
    return rf

def get_all_refunds_service(): return refunds_db
def get_refund_by_id_service(rf_id): return next((r for r in refunds_db if r["refund_id"] == rf_id), None)

# --- ANALYTICS ---
def get_total_revenue(): return {"total_revenue": sum(tx["amount"] for tx in transactions_db if tx["status"] == "Success")}
def get_total_transactions_count(): return {"total_transactions": len(transactions_db)}
def get_total_payouts_sum(): return {"total_payouts": sum(po["amount"] for po in payouts_db if po["status"] == "Approved")}
def get_total_refunds_sum(): return {"total_refunds": sum(rf["amount"] for rf in refunds_db if rf["status"] == "Refunded")}