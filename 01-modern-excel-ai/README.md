# Stage 1: Modern Excel & AI-Powered Formula Engineering

Excel remains the most widely used data tool in the corporate world. However, the modern analyst does not rely on old, fragile VLOOKUPs. This stage covers **Dynamic Array Formulas** and **AI-augmented formula generation**.

## 🚀 Modern Excel Concepts to Learn
1.  **Dynamic Arrays**: Functions that return a list of values spanning multiple cells (spilling).
    *   `=FILTER(array, include)`: Dynamically filters records based on conditions.
    *   `=UNIQUE(array)`: Extracts unique records, replacing manual remove-duplicate clicks.
    *   `=SORT(array, sort_index)`: Sorts lists dynamically.
2.  **Next-Gen Lookup**:
    *   `=XLOOKUP(lookup_value, lookup_array, return_array)`: Faster, looks left or right, handles errors, and returns whole arrays.
3.  **AI Formula Engineering**:
    *   Using LLMs (Claude or ChatGPT) to write complex nested functions based on natural language descriptions (e.g. "Write an Excel formula to check if the date is a weekend and if sales exceed $500").

---

## 💻 Practice Dataset: `sales_leads.csv`
Open [sales_leads.csv](sales_leads.csv) directly in Microsoft Excel (or Google Sheets) to practice.

### Exercises:
1.  **Extract Unique Verticals**:
    In cell E2, enter:
    `=UNIQUE(B2:B20)`
    Observe how Excel automatically spills the list of unique business verticals.
2.  **Filter High-Value Leads**:
    In cell G2, enter:
    `=FILTER(A2:C20, C2:C20 > 50000)`
    This filters and displays all lead names, verticals, and values exceeding $50,000.
3.  **XLOOKUP Contact Finder**:
    Locate a lead value dynamically:
    `=XLOOKUP("Apex Corp", A2:A20, C2:C20)`

---

## 🤖 Prompt Templates: Let AI Write Your Excel Formulas
Copy and paste this prompt into Claude or ChatGPT to design complex Excel logic:

```text
Act as an Advanced Excel expert. I need a formula for Microsoft Excel 365.
My dataset structure:
- Column A: Invoice Date (format YYYY-MM-DD)
- Column B: Region (Text)
- Column C: Invoice Amount (Number)

I want a formula that:
1. Checks if the date in Column A is a Saturday or Sunday.
2. If it is a weekend, multiply Column C by 0.15 (15% tax).
3. If it is a weekday, multiply Column C by 0.10 (10% tax).
4. Return 0 if Column C is empty or 0.

Write the formula starting with '=' and explain the logic.
```
