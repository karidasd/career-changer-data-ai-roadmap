# Stage 5: Advanced Prompt Engineering & Data Augmentation

Data analysts often deal with unstructured text data—such as customer survey responses, logs, or raw emails. Instead of manually reading and labeling these records, this stage teaches you how to leverage **Structured Prompting** and **Data Augmentation** to classify text, extract features, and audits records at scale.

## 🚀 Advanced Prompting Concepts to Learn
1.  **Few-Shot Learning**: Providing the LLM with 2-3 examples of input and output patterns so it learns the exact format (such as classification labels) before writing.
2.  **Structured JSON Mode**: Forcing the model to return valid, parsable JSON objects instead of conversational text. This allows you to directly import LLM output into Pandas DataFrames!
3.  **Chain-of-Thought (CoT) Data Auditing**: Prompting the model to write down its reasoning steps before making a final classification, which increases accuracy on complex data auditing tasks.

---

## 💻 Practice Script: `prompt_templates.json`
The file [prompt_templates.json](prompt_templates.json) contains production-ready JSON structured prompts that you can feed into Claude or ChatGPT to:
-   **Classify and Tag Support Tickets** with sentiment and priority.
-   **Anonymize PII (Personally Identifiable Information)** in customer logs.
-   **Extract Structured Entities** (dates, amounts, merchants) from unstructured receipts.

---

## 🤖 Prompt Templates: JSON Output Extraction
To extract structured data from unstructured user feedback, copy and paste this system prompt:

```text
You are a Data Extraction Assistant. Your goal is to analyze customer feedback and return structured information.

User Input:
"I ordered a model X10 laptop on 2026-06-25. The shipping was delayed by 3 days and the charger was missing. I paid $1,200."

Your output must be a valid JSON object with the following schema:
{
  "product_name": String,
  "transaction_date": String (format YYYY-MM-DD),
  "issues_flagged": Array of Strings,
  "monetary_value": Float,
  "sentiment_score": Integer (1 to 5, where 1 is extremely negative and 5 is positive)
}

Do not include any conversational introduction or code block tags. Return only the raw JSON.
```
