from modern_treasury import VirtualAccountRequest, PaymentOrderRequest
from modern_treasury.modern_treasury import ModernTreasury
from modern_treasury.objects.request.incoming_payment_detail import IncomingPaymentDetailRequest


modern_treasury = ModernTreasury.create(organization_id='4aedefda-78df-4cfc-a3e5-42c2ba3f7e9a',
                                        api_key='test-CxfzxGrJqmNtoUmmyQyXyDR85yi8dGP33zmeYLfzCzuka2D6UpiJLAMscjrX1wPj')

incoming_payment_detail = IncomingPaymentDetailRequest(
    transfer_type="wire",
    direction="credit",
    amount=13243377,
    internal_account_id="5539abff-cb03-42dd-bb6b-423de9a5ec31",
    virtual_account_id="9ae2e7ea-5595-43ab-af02-2c53c8ce960e",
)

# counterparties = modern_treasury.list_counterparties()
# for counterparty in counterparties:
#     result = modern_treasury.delete_counterparty_by_id(counterparty.id)
#     print(result)

breakpoint()
result = modern_treasury.post_incoming_payment_detail(incoming_payment_detail_request=incoming_payment_detail)
print(result.json)
