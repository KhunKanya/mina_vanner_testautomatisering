
# 🧪 Mina Vänner - Test Automation Project  
**End-to-End Web Automation with Playwright & Behave (BDD)**  
[![Playwright](https://img.shields.io/badge/Playwright-2.4+-45ba4b?logo=playwright)](https://playwright.dev)
[![Behave](https://img.shields.io/badge/Behave-1.2.7-green)](https://behave.readthedocs.io/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-black?logo=githubactions)](https://github.com/features/actions)

Automated test solution for contact management features, implementing BDD methodology with industry-standard tools. Validates critical user workflows for friend management systems.

## 🔍 Project Overview
Automates testing of core functionalities:
- **Contact Management** (Add/View/Edit/Delete)
- **Case-Insensitive Search**
- **Data Validation**
- **UI Responsiveness**

Implements all user stories with Gherkin scenarios and CI/CD pipeline.

## 🚀 User Stories Implemented
| ID   | Feature                  | Status | Scenario Count |
|------|--------------------------|--------|----------------|
| US01 | View Friend List         | ✅     | 3              |
| US02 | Edit Contact Info        | ✅     | 4              |
| US03 | Add New Contacts         | ✅     | 5              |
| US04 | Remove Friends           | ✅     | 3              |
| US05 | Search Contacts (Case-Insensitive)| ✅ | 6              |

## 🛠️ Tech Stack
- **Testing Framework**: Behave (BDD)
- **Browser Automation**: Playwright
- **Language**: Python 3.10+
- **Reporting**: Built-in Behave reports
- **CI/CD**: GitHub Actions
- **OS**: Cross-platform (Windows/Linux/macOS)

## ⚙️ Setup & Execution
```bash
# 1. Clone repository
git clone https://github.com/KhunKanya/mina_vanner_testautomatisering.git
cd mina_vanner_testautomatisering

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install

# 4. Run tests (headless mode)
behave

# 5. Run with UI (headed mode)
behave --tags=@ui -D headed=true