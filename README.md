# Financing Matchmaker for M&A

## Overview
The Financing Matchmaker for M&A is an AI-powered platform that simplifies the process of securing financing for mergers and acquisitions. It helps users discover and compare financing options, assess eligibility, generate tailored document checklists, and track financing progress. This app is designed to reduce friction in the M&A financing process, enabling faster and more accurate decision-making.

## Key Features
- **Lender Recommendation Engine**: Matches buyers with suitable lenders based on deal size, industry, and repayment preferences.
- **Eligibility Checker**: Uses AI to assess the compatibility of the user's deal with specific lender requirements.
- **Document Checklist Generator**: Automatically provides a tailored checklist of required documents for each lender.
- **Progress Tracker**: Visualizes the status of financing applications to provide clarity and transparency.

## Tech Stack
- **Frontend**: Streamlit for interactive UI.
- **Backend**: Python Flask/Django for business logic.
- **Database**: SQLite for storing lender and deal data.
- **AI**:
  - TF-IDF for extracting and analyzing textual data.
  - Cosine Similarity for matching compatibility between deals and lenders.
  - Document Checklist Generator for tailored preparation guidance.

## Installation and Usage

### Prerequisites
- Python 3.10 or higher
- Pip (Python package manager)

### Installation
1. Clone this repository:

2. Install dependencies:


3. Set up the database:


4. Run the app:


5. Open the app in your browser using the URL provided by Streamlit.

## How It Works
1. **Input Deal Information**:
   - Enter details like deal size, industry, and repayment timeline.
2. **Lender Matching**:
   - The app recommends lenders based on compatibility and displays key metrics (e.g., interest rates, terms).
3. **Document Checklist**:
   - Generate a tailored checklist of documents required for financing.
4. **Track Progress**:
   - Visualize and monitor the status of financing applications.

## Sample Test Data

### Buyer Input:
- **Deal Size**: $15M
- **Industry**: Healthcare
- **Repayment Timeline**: 5 years

### Expected Output:
- **Lender Recommendations**:
  - ABC Bank: Interest 6%, Term 5 years, Compatibility: High.
  - XYZ PE Firm: Interest 8%, Term 7 years, Compatibility: Medium.
- **Document Checklist**:
  - Financial Statements (Last 3 Years).
  - Projections (5 Years).
  - LOI (Letter of Intent).

