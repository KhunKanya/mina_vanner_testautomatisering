Feature: delete a contact
# US04 som användraen vill jag kunna ta bort en vän från listan, så jag kan hålla listan uppdaterad.

  Scenario: delete a contact
  Given änvandaren är i websidan på vänsidan
  And  Är vän med Tom Bombadil
  When Användaren tar bort Tom
  Then Tom är inte längre kompis