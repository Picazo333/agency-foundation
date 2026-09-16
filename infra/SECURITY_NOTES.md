# Security Notes

- Never commit secrets, tokens, passwords, private keys or `.env` files.
- Use least privilege for external integrations.
- Authentication and authorization are separate concerns.
- AI/MCP/system integrations require explicit permission, logging and output-validation design before production.
- Security decisions must be documented with the relevant system implementation.

## Extended Baseline (Neutral Technical Foundation)

- **.env Management:** A `.env.example` file is provided as the sole template for environment variables. Real `.env` files must be ignored by version control (verified via `.gitignore`).
- **API Key Handling:** Frontend applications must never expose private API keys. Use server-side proxy routes to handle sensitive requests.
- **AI Integration Guidelines:** AI-generated assets or code (e.g., from Gemini Asset Factory) must undergo provenance tracking and validation before inclusion. Prompts and inputs to external AI systems must not contain proprietary PII or unreleased financial data.
