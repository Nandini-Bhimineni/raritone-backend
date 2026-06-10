from app.database.db import db
from bson.objectid import ObjectId

wallet_collection = db.wallets


async def create_wallet(data):
    """Create a new wallet for a customer"""
    wallet = {
        "customer_id": data.customer_id,
        "balance": data.balance
    }

    result = await wallet_collection.insert_one(wallet)

    wallet["_id"] = str(result.inserted_id)

    return wallet


async def get_wallets():
    """Get all wallets"""
    wallets = []

    async for wallet in wallet_collection.find():
        wallet["_id"] = str(wallet["_id"])
        wallets.append(wallet)

    return wallets


async def get_wallet_by_id(wallet_id: str):
    """Get wallet by ID"""
    try:
        wallet = await wallet_collection.find_one({"_id": ObjectId(wallet_id)})
        if wallet:
            wallet["_id"] = str(wallet["_id"])
        return wallet
    except:
        return None


async def get_wallet_by_customer(customer_id: str):
    """Get wallet by customer ID"""
    wallet = await wallet_collection.find_one({"customer_id": customer_id})
    if wallet:
        wallet["_id"] = str(wallet["_id"])
    return wallet


async def update_wallet(wallet_id: str, data):
    """Update wallet balance"""
    try:
        update_data = {}
        if data.balance is not None:
            update_data["balance"] = data.balance

        result = await wallet_collection.update_one(
            {"_id": ObjectId(wallet_id)},
            {"$set": update_data}
        )

        if result.modified_count > 0:
            wallet = await wallet_collection.find_one({"_id": ObjectId(wallet_id)})
            wallet["_id"] = str(wallet["_id"])
            return wallet
        return None
    except:
        return None


async def delete_wallet(wallet_id: str):
    """Delete a wallet"""
    try:
        result = await wallet_collection.delete_one({"_id": ObjectId(wallet_id)})
        return result.deleted_count > 0
    except:
        return False
