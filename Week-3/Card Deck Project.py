import random
suits = ['♠', '♥', '♦', '♣']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [f"{value}{suit}" for suit in suits for value in values]

card_num = int(input("How many Cards you Want to Draw: "))
face_cards = ['J♠', 'Q♠', 'K♠', 'J♥', 'Q♥', 'K♥', 'J♦', 'Q♦', 'K♦', 'J♣', 'Q♣', 'K♣']

dock = random.sample(deck, card_num)

drawn_face_cards = [card for card in dock if card in face_cards]

print("You drew:", dock)
print("Face cards among them:", drawn_face_cards)
