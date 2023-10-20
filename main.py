import genanki
import csv

model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

deck = genanki.Deck(2059400110, 'Lang Deck')

# Open the CSV file for reading
csv_file_path = 'data.csv'
with open(csv_file_path, 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    # Iterate through each row in the CSV
    for row in csv_reader:
        # Extract data from the CSV
        question = row['Question']
        answer = row['Answer']

        # Create a new note for this row
        my_note = genanki.Note(
            model=model,
            fields=[question, answer]
        )

        # Add the note to the deck
        deck.add_note(my_note)


package = genanki.Package(deck)
package.write_to_file('my_deck.apkg')
print("Imported notes from the CSV file.")
