from fastapi import APIRouter, HTTPException
from app.schemas.payment_schema import WalletCreate, WalletAmountUpdate
from app.api.payments.service import (
    create_wallet_service,
    get_all_wallets_service,
    get_wallet_by_customer_service,
    get_balance_service,
    add_money_service,
    deduct_money_service
)

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/wallet")
def create_wallet(wallet_in: WalletCreate):
    result = create_wallet_service(wallet_in)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/wallet")
def get_all_wallets():
    return get_all_wallets_service()

@router.get("/wallet/{customer_id}")
def get_wallet_by_customer(customer_id: int):
    wallet = get_wallet_by_customer_service(customer_id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found for this customer")
    return wallet

@router.get("/wallet/balance/{customer_id}")
def get_wallet_balance(customer_id: int):
    balance_info = get_balance_service(customer_id)
    if not balance_info:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return balance_info

@router.put("/wallet/add-money")
def add_money(update_in: WalletAmountUpdate):
    wallet = add_money_service(update_in)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@router.put("/wallet/deduct-money")
def deduct_money(update_in: WalletAmountUpdate):
    result = deduct_money_service(update_in)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result