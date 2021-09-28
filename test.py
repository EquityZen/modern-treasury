import random

from modern_treasury import VirtualAccountRequest, ExpectedPaymentRequest, PaymentOrderRequest, \
    AccountDetailsRequest, CounterPartyRequest, AccountRequest, AddressRequest
from modern_treasury.modern_treasury import ModernTreasury
from modern_treasury.objects.request.external_account import ExternalAccountRequest
from modern_treasury.objects.request.routing_details import RoutingDetailsRequest

modern_treasury = ModernTreasury.create(organization_id='4aedefda-78df-4cfc-a3e5-42c2ba3f7e9a',
                                        api_key='test-CxfzxGrJqmNtoUmmyQyXyDR85yi8dGP33zmeYLfzCzuka2D6UpiJLAMscjrX1wPj')

internal_accounts = modern_treasury.get_internal_accounts()

internal_account = internal_accounts[0]

virtual_account_request = VirtualAccountRequest(name="dork", internal_account_id=internal_account.id)

virtual_account = modern_treasury.create_virtual_account(virtual_account_request)

# expected_payment_request = ExpectedPaymentRequest(
#     amount_upper_bound=5000,
#     amount_lower_bound=5000,
#     direction='credit',
#     internal_account_id=virtual_account.id,
#     type='ach',
#     currency='USD',
#     metadata={'dork': 'bork_id'},
# )

# response = modern_treasury.create_expected_payment(expected_payment_request=expected_payment_request)

account_details = AccountDetailsRequest(
    account_number='55555555',
    account_number_type='other'
)

routing_details = RoutingDetailsRequest(routing_number_type = "aba", routing_number = "121141822")

address_request = AddressRequest(line1='street 123',
                                 line2='',
                                 locality='NY',
                                 region='Brooklyn',
                                 postal_code ='11215',
                                 country='US')

account_request = AccountRequest(address=address_request,
                                 account_type='checking',
                                 account_details_list=[account_details],
                                 routing_details_list=[routing_details])

counterparty_request = CounterPartyRequest(name=f'A NEW COUNTERPARTY',
                                           account_request_list=[account_request],
                                           metadata={'buyer_id': '000'}
                                           )

counterparty = modern_treasury.create_counterparty_account(
    counterparty_request=counterparty_request
)


external_account_request = ExternalAccountRequest(
    party_address=address_request
)

new_routing_details = RoutingDetailsRequest(routing_number_type = "aba", routing_number = "123456789")

new_account_details = AccountDetailsRequest(
    account_number='123456789',
    account_number_type='clabe',
)

new_external_account = modern_treasury.update_external_account(external_account_request=external_account_request,
                                                               external_account_id=counterparty.accounts[0].id)

deleted_result = modern_treasury.delete_routing_details(
    external_account_id=counterparty.accounts[0].id,
    routing_details_id=counterparty.accounts[0].routing_details[0].id)

routing = modern_treasury.get_routing_details_by_id(
    external_account_id=counterparty.accounts[0].id,
    routing_details_id=counterparty.accounts[0].routing_details[0].id)

new_routing_details = modern_treasury.create_routing_details(
    routing_details=new_routing_details,
    external_account_id=new_external_account.id
)
print('stuff')

# results = modern_treasury.list_counterparties(metadata={'buyer_id': '123'})
# for result in results:
#     modern_treasury.delete_counterparty_by_id(result.id)
#     print(result)




#
#
# payment_order_request = PaymentOrderRequest(type='ach',
#                                             originating_account_id=internal_account.id,
#                                             originating_party_name='client account',
#                                             receiving_account_id=counterparty.id,
#                                             amount=1000,
#                                             account_type='checking',
#                                             currency='USD',
#                                             direction='debit')
# result = modern_treasury.create_payment_order(payment_order_request=payment_order_request)
# print(result.json)
