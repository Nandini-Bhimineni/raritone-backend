from fastapi import APIRouter, HTTPException

from app.schemas.wallet_schema import (
    WalletCreate,
    WalletUpdate,
    WalletResponse
)

from app.api.wallets.service import (
    create_wallet,
    get_wallets,
    get_wallet_by_id,
    get_wallet_by_customer,
    update_wallet,
    delete_wallet
)

router = APIRouter(
    prefix="/wallets",
    tags=["Wallets"]
)


@router.post("/", response_model=WalletResponse)
async def create_new_wallet(data: WalletCreate):
    """Create a new wallet"""
    return await create_wallet(data)


@router.get("/", response_model=list)
async def list_wallets():
    """Get all wallets"""
    return await get_wallets()


@router.get("/{wallet_id}", response_model=WalletResponse)
async def get_wallet(wallet_id: str):
    """Get wallet by ID"""
    wallet = await get_wallet_by_id(wallet_id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet


@router.get("/customer/{customer_id}", response_model=WalletResponse)
async def get_customer_wallet(customer_id: str):
    """Get wallet by customer ID"""
    wallet = await get_wallet_by_customer(customer_id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found for this customer")
    return wallet


@router.put("/{wallet_id}", response_model=WalletResponse)
async def update_wallet_balance(wallet_id: str, data: WalletUpdate):
    """Update wallet balance"""
    wallet = await update_wallet(wallet_id, data)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet


@router.delete("/{wallet_id}")
async def delete_customer_wallet(wallet_id: str):
    """Delete a wallet"""
    success = await delete_wallet(wallet_id)
    if not success:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"message": "Wallet deleted successfully"}
