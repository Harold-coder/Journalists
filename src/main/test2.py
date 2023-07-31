test = ['A Climate Warning from the Cradle of Civilization', 'The Secret History of Gun Rights: How Lawmakers Armed the N.R.A.', 'Amid the Counterattack’s Deadly Slog, a Glimmer of Success for Ukraine', 'Russia Says 2 Drones Hit Buildings in Moscow in Latest Wave of Attacks', 'Russia Takes Its Ukraine Information War Into Video Games', 'Inside the Party Switch that Blew Up North Carolina Politics', 'At Least 43 Killed in Blast at Political Rally in Pakistan', 'What Is It About Montecito?', 'New York City Had a Migrant Crisis. It Hired a Covid Expert to Help.', 'The Legacy Dilemma: What to Do About Privileges for the Privileged?', '$60 Million Refund Request Shows Financial Pressure on Trump From Legal Fees', 'Trump Threatens Republicans Who Don’t Help Him Exact Vengeance', 'Megan Rapinoe Is Not Going Quietly', 'The Weekender', 'The New York Times News Quiz, July 28, 2023', 'He Created the Katamari Games, but They’re Rolling On Without Him', 'How Trump Could Wreck Things for Republicans in 2024', 'What ‘Oppenheimer’ Doesn’t Tell You About the Trinity Test', 'The Research Scandal at Stanford Is More Common Than You Think', 'It Was Never Just About the Butterflies', 'A New Recipe for a Very Old Hummus', 'Why Is It So Darn Hot?', 'In Israel, High Stakes for High Court: Democracy’s Fate', 'A Federal Food Safety Case Reveals Latest New York City Rat Horror Story', 'West African Nations Threaten Military Action Unless Niger Coup Is Undone', 'Terence Crawford Stands Alone at the Top of Boxing', 'A Recipe for Love? Add ‘Water and Sunlight.’']

def getRelevant(articles):
    titles_list = []
    index = 0
    for title in articles:
        titles_list.append(str(index)+ ": " + title)
        index += 1
    
    return titles_list

print(getRelevant(test))