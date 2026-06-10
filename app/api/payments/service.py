from datetime import datetime
from app.schemas.payment_schema import WalletCreate, WalletAmountUpdate

# In-memory database simulation
wallets_db = []

def get_current_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def find_wallet_by_customer(customer_id: int):
    for wallet in wallets_db:
        if wallet["customer_id"] == customer_id:
            return wallet
    return None

def create_wallet_service(data: WalletCreate):
    # Check if a wallet already exists for this customer
    existing_wallet = find_wallet_by_customer(data.customer_id)
    if existing_wallet:
        return {"error": "Wallet already exists for this customer"}
    
    timestamp = get_current_timestamp()
    new_wallet = {
        "id": len(wallets_db) + 1,
        "customer_id": data.customer_id,
        "balance": float(data.initial_balance),
        "created_at": timestamp,
        "updated_at": timestamp
    }
    wallets_db.append(new_wallet)
    return new_wallet

def get_all_wallets_service():
    return wallets_db

def get_wallet_by_customer_service(customer_id: int):
    return find_wallet_by_customer(customer_id)

def get_balance_service(customer_id: int):
    wallet = find_wallet_by_customer(customer_id)
    if not wallet:
        return None
    return {"customer_id": customer_id, "balance": wallet["balance"]}

def add_money_service(data: WalletAmountUpdate):
    wallet = find_wallet_by_customer(data.customer_id)
    if not wallet:
        return None
    
    wallet["balance"] += float(data.amount)
    wallet["updated_at"] = get_current_timestamp()
    return wallet

def deduct_money_service(data: WalletAmountUpdate):
    wallet = find_wallet_by_customer(data.customer_id)
    if not wallet:
        return {"error": "Wallet not found"}
    
    if wallet["balance"] < data.amount:
        return {"error": "Insufficient funds in wallet"}
        
    wallet["balance"] -= float(data.amount)
    wallet["updated_at"] = get_current_timestamp()
    return wallet