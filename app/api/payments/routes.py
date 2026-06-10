from fastapi import APIRouter, HTTPException
from app.schemas import payment_schema as schema
from app.api.payments import service

router = APIRouter(prefix="/payments", tags=["Payments Module"])

# ================= WALLET APIs =================
@router.post("/wallet")
def create_wallet(data: schema.WalletCreate):
    res = service.create_wallet_service(data)
    if "error" in res: raise HTTPException(status_code=400, detail=res["error"])
    return res

@router.get("/wallet")
def get_all_wallets(): return service.get_all_wallets_service()

@router.get("/wallet/{customer_id}")
def get_wallet_by_customer(customer_id: int):
    w = service.get_wallet_by_customer_service(customer_id)
    if not w: raise HTTPException(status_code=404, detail="Wallet not found")
    return w

@router.get("/wallet/balance/{customer_id}")
def get_wallet_balance(customer_id: int):
    b = service.get_balance_service(customer_id)
    if not b: raise HTTPException(status_code=404, detail="Wallet not found")
    return b

@router.put("/wallet/add-money")
def add_money(data: schema.WalletAmountUpdate):
    w = service.add_money_service(data)
    if not w: raise HTTPException(status_code=404, detail="Wallet not found")
    return w

@router.put("/wallet/deduct-money")
def deduct_money(data: schema.WalletAmountUpdate):
    res = service.deduct_money_service(data)
    if "error" in res: raise HTTPException(status_code=400, detail=res["error"])
    return res

# ================= TRANSACTION APIs =================
@router.post("/transaction")
def create_transaction(data: schema.TransactionCreate): return service.create_transaction_service(data)

@router.get("/transaction")
def get_all_transactions(): return service.get_all_transactions_service()

@router.get("/history") # Matches GET /payments/history
def get_transaction_history(): return service.get_all_transactions_service()

@router.get("/transaction/{transaction_id}")
def get_transaction_by_id(transaction_id: str):
    tx = service.get_transaction_by_id_service(transaction_id)
    if not tx: raise HTTPException(status_code=404, detail="Transaction not found")
    return tx

@router.get("/transaction/customer/{customer_id}")
def get_transactions_by_customer(customer_id: int): return service.get_tx_by_customer_service(customer_id)

@router.get("/transaction/vendor/{vendor_id}")
def get_transactions_by_vendor(vendor_id: int): return service.get_tx_by_vendor_service(vendor_id)

@router.get("/status/{status}")
def get_transactions_by_status(status: str): return service.get_tx_by_status_service(status)

# ================= SETTLEMENT APIs =================
@router.post("/settlement")
def create_settlement(data: schema.SettlementCreate): return service.create_settlement_service(data)

@router.get("/settlement")
def get_all_settlements(): return service.get_all_settlements_service()

@router.get("/settlement/{settlement_id}")
def get_settlement_by_id(settlement_id: str):
    s = service.get_settlement_by_id_service(settlement_id)
    if not s: raise HTTPException(status_code=404, detail="Settlement not found")
    return s

@router.get("/settlement/vendor/{vendor_id}")
def get_settlements_by_vendor(vendor_id: int): return service.get_settlements_by_vendor_service(vendor_id)

# ================= PAYOUT APIs =================
@router.post("/payout")
def create_payout(data: schema.PayoutCreate): return service.create_payout_service(data)

@router.get("/payout")
def get_all_payouts(): return service.get_all_payouts_service()

@router.get("/payout/vendor/{vendor_id}")
def get_payouts_by_vendor(vendor_id: int): return service.get_payouts_by_vendor_service(vendor_id)

@router.put("/payout/{payout_id}/approve")
def approve_payout(payout_id: str):
    p = service.update_payout_status(payout_id, "Approved")
    if not p: raise HTTPException(status_code=404, detail="Payout record not found")
    return p

@router.put("/payout/{payout_id}/reject")
def reject_payout(payout_id: str):
    p = service.update_payout_status(payout_id, "Rejected")
    if not p: raise HTTPException(status_code=404, detail="Payout record not found")
    return p

# ================= REFUND APIs =================
@router.post("/refund")
def create_refund(data: schema.RefundCreate): return service.create_refund_service(data)

@router.get("/refund")
def get_all_refunds(): return service.get_all_refunds_service()

@router.get("/refund/{refund_id}")
def get_refund_by_id(refund_id: str):
    r = service.get_refund_by_id_service(refund_id)
    if not r: raise HTTPException(status_code=404, detail="Refund record not found")
    return r

# ================= ANALYTICS APIs =================
@router.get("/total-revenue")
def total_revenue(): return service.get_total_revenue()

@router.get("/total-transactions")
def total_transactions(): return service.get_total_transactions_count()

@router.get("/total-payouts")
def total_payouts(): return service.get_total_payouts_sum()

@router.get("/total-refunds")
def total_refunds(): return service.get_total_refunds_sum()