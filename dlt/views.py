# views.py

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from .blockchain import Blockchain, Token


class DisplayChainView(View):
    def get(self, request):
        blockchain = Blockchain()
        blockchain.add_block("First block after Genesis")
        blockchain.add_block("Second block after Genesis")

        # Add tokens to blocks
        for block in blockchain.chain:
            token1 = Token("Alice", "Bob", 50)  # Example sender: Alice, receiver: Bob, value: 50
            token2 = Token("Bob", "Alice", 30)  # Example sender: Bob, receiver: Alice, value: 30
            blockchain.add_tokens_to_block(block, [token1, token2])

        chain_data = []
        for block in blockchain.chain:
            chain_data.append(block.get_block_data())
        return render(request, 'chain.html', {'chain_data': chain_data})


class ValidateChainView(View):
    def get(self, request):
        blockchain = Blockchain()
        blockchain.add_block("First block after Genesis")
        blockchain.add_block("Second block after Genesis")
        if blockchain.is_valid():
            return HttpResponse("Blockchain is valid.")
        else:
            return HttpResponse("Blockchain is invalid.")


class DisplayTransactionsView(View):
    def get(self, request):
        blockchain = Blockchain()
        transaction_history = []

        for block in blockchain.chain:
            for token in block.tokens:
                transaction_history.append({'sender': token.sender, 'receiver': token.receiver, 'value': token.value})

        return render(request, 'transactions.html', {'transaction_history': transaction_history})