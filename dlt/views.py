# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .blockchain import Blockchain


class DisplayChainView(View):
    def get(self, request):
        blockchain = Blockchain()
        blockchain.add_block("First block after Genesis")
        blockchain.add_block("Second block after Genesis")
        chain_data = []
        for block in blockchain.chain:
            chain_data.append({
                'index': block.index,
                'timestamp': block.timestamp,
                'data': block.data,
                'hash': block.hash,
                'previous_hash': block.previous_hash
            })
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
