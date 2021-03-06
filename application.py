#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import stripe
from flask import Flask, render_template, request

'''
    Test Credit Card
    Number: 4242 4242 4242 4242
    Expiration Date: Any date in the future (not expired)
    CVC: Any 3 digits
'''

stripe_keys = {
    'secret_key':      'your_secret_key',
    'publishable_key': 'your_publishable_key'
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])


@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500
    # Create customer
    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )
    # Make charge
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )
    return render_template('charge.html', amount=amount)


if __name__ == '__main__':
    app.run(debug=True)
