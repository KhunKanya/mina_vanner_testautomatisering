
# 🧪 Friends Contact – Web Test Automation Project
### Veckouppgift 6 (E2E + BDD använder behave och Playwright)

---------



## 🚀 Projektöversikt

### Detta projekt syftar till att automatisera tester för funktionaliteten kring hantering av vänner i webbapplikationen. Testerna säkerställer att användaren kan:
### 🔗 Web section: [Link](https://forverkliga.se/JavaScript/my-contacts/#/).

- ### Se en lista över sina vänner.
- ### Ändra information om en vän.
- ### Lägga till nya kontakter.
- ### Ta bort vänner.
- ### Söka efter vänner oberoende av stora eller små bokstäver.

## 📋 User Stories

- ###  **US01**: Som användare vill jag kunna se en lista över mina vänner, så att jag kan kontakta mina vänner.
- ###  **US02**: Som användare vill jag kunna ändra information, så att jag kan uppdatera kontaktuppgifter för mina vänner.
- ###  **US03**: Som användare vill jag kunna lägga till nya kontakter, så att jag kan hålla koll på mina vänner.
- ###  **US04**: Som användare vill jag kunna ta bort en vän från listan, så att jag kan hålla listan uppdaterad.
- ###  **US05**: Som användare vill jag kunna söka efter mina vänner på namn eller e-post, så att jag kan hitta dem oavsett om jag använder stora eller små bokstäver.

## 🛠️ Tech Stack

- ### **Test Framework**: Behave (Gherkin + Python)
- ### **Browser Automation**: Playwright
- ### **Språk**: Python 3.x


## 📁 Mappstruktur

``` text

├── src/
│   ├── features/
│   │   ├── add_contact.feature
│   │   ├── delete_contact.feature
│   │   ├── search_contact.feature
│   │   └── view_all_contact.feature
│   ├── pages/
│   │   └── base_page.py
│   ├── steps/
│   │   ├── add_contact.py
│   │   ├── delete_contact.py
│   │   ├── search_contact.py
│   │   └── view_all_contact.py
│   └── environment.py
├── requirements.txt
└── README.md
```

