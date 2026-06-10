from fastapi import APIRouter

from app.schemas.payment_schema import (
    WalletCreate,
    TransactionCreate,
    SettlementCreate,
    PayoutRequestCreate
)

from app.api.payments.service import (
    create_wallet,
    get_wallets,
    create_transaction,
    get_transactions,
    create_settlement,
    get_settlements,
    create_payout_request,
    get_payout_requests
)

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/wallet")
def wallet(data: WalletCreate):
    return create_wallet(data)


@router.get("/wallet")
def wallets():
    return get_wallets()


@router.post("/transaction")
def transaction(data: TransactionCreate):
    return create_transaction(data)


@router.get("/transaction")
def transactions():
    return get_transactions()


@router.post("/settlement")
def settlement(data: SettlementCreate):
    return create_settlement(data)


@router.get("/settlement")
def settlements():
    return get_settlements()


@router.post("/payout")
def payout(data: PayoutRequestCreate):
    return create_payout_request(data)


@router.get("/payout")
def payouts():
    return get_payout_requests()