#!/usr/bin/env python
# coding: utf-8

# In[34]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[35]:


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank +" of " + self.suit


# In[36]:


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
            
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# In[37]:


class Player:
    def __init__(self,name):
        self.name=name;
        self.all_cards=[]
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if(type(new_cards)==type([])):
           self.all_cards.extend(new_cards)
        else:
           self.all_cards.append(new_cards)
    def __str__(self):
           return f'Player {self.name} has {len(self.all_cards)} cards.'


# In[38]:


player_one=Player('One')
player_two=Player('Two')
new_deck = Deck()
new_deck.shuffle()

#splitting 52 cards among two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# In[39]:


game_on=True


# In[40]:


round_num=0

while game_on:
    round_num+=1
    print(f'Round {round_num}')
    
    if len(player_one.all_cards)==0:
        print("Player Two Wins")
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print("Player One Wins")
        game_on=False
        break
    #starting new round
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    
    #at war i.e when both players have same cards
    
    at_war=True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war=False
            
        else:
            print("War!")
            
            if len(player_one.all_cards)<5:
                print("Player one unable to declare war")
                print("Player TWO wins!")
                game_on=False
                break
            elif len(player_two.all_cards)<5:
                print("Player two unable to declare war")
                print("Player ONE wins!")
                game_on=False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

