from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received by ccdshop: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print('\033[31m' + 'in pay success handler' + '\033[0m')

        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received by ccdshop: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        print('\033[31m' + 'in failed handle' + '\033[0m')

        return HttpResponse(
            content=f'Webhook payment failed received by ccdshop: {event["type"]}',
            status=200)
            
    from django.http import HttpResponse

