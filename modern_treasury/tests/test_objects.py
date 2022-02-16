from decimal import Decimal
import json
from unittest import TestCase
from unittest.mock import patch

from modern_treasury.objects.request.incoming_payment_detail import IncomingPaymentDetailRequest
from modern_treasury.objects.request.payment_order import PaymentOrderRequest
from modern_treasury.objects.webhook_events.incoming_payment_detail_event import IncomingPaymentDetailEvent
from modern_treasury.objects.webhook_events.payment_order_event import PaymentOrderEvent

from ..modern_treasury import ModernTreasury


class ObjectsTest(TestCase):
    def setUp(self):
        super().setUp()
    
    def test__incoming_payment_detail_request(self):
        request = IncomingPaymentDetailRequest(transfer_type="wire", direction="credit", amount=Decimal("10.0"))
        self.assertEqual(request.amount, 1000)
    
    def test__payment_order_request(self):
        request = PaymentOrderRequest(type="ach", amount=Decimal("10.0"), direction="credit")
        self.assertEqual(request.amount, 1000)

    def test__incoming_payment_detail_event(self):
        event = IncomingPaymentDetailEvent({
            "data": {
                "amount": 1000
            }
        })
        self.assertEqual(event.data.amount, 10.0)

    def test__payment_order_event(self):
        event = PaymentOrderEvent({
            "data": {
                "amount": 1000
            }
        })
        self.assertEqual(event.data.amount, 10.0)