# IP Protection Reference

## Copyright

### What's automatically protected
- Your source code (the moment you write it)
- Written curriculum, lesson plans, documentation
- Brand copy, social posts, frameworks you've written
- App UI and design

### How to strengthen it
- **Private GitHub repo** = timestamped proof of creation (use this always)
- **Register with US Copyright Office** at copyright.gov ($65 per work) for legal standing to sue
- Add copyright notice to your app footer: `© 2026 HumanFirst AI / AI with AI Ventures LLC`

## Trademarks

### What to protect
- HumanFirst AI
- AI with AI
- Vibe Lab
- Pigeon
- Reenai
- Any other product names you're building a business around

### How to file
1. Search at **USPTO.gov** (TESS database) to check availability
2. File at **USPTO.gov** ($250–$350 per class)
3. Key classes for your work:
   - Class 41: Education and training services
   - Class 42: Software as a service, AI services
   - Class 35: Business consulting, marketing services

### Timeline
- USPTO review: 8–12 months
- Protection begins from filing date (not approval)
- Use ™ immediately after filing, ® only after registration

## Trade Secrets

### What qualifies
- Your system prompts and agent instructions
- Your Skill files and workflow architectures
- Your LLM Council framework
- Your DBS framework
- Proprietary curriculum structures

### How to protect them
- Keep them out of public GitHub repos
- Don't publish full system prompts on social media or YouTube
- If sharing publicly, share the *concept* not the *implementation*
- Watermark anything you do share: "© 2026 HumanFirst AI — adamma@aiwithai.ai"

## NDAs for Collaborators

### When to use
- Anyone helping you build (developers, designers, contractors)
- Anyone you pitch to before launch
- Podcast or workshop guests who see behind-the-scenes content

### Free NDA resources
- **Docusign** — free NDA template + e-signature
- **HelloSign** — free for 3 docs/month
- **LegalZoom** — one-time NDA for ~$39

### Key clauses to include
- Definition of confidential information (code, prompts, frameworks, business plans)
- Duration (2–5 years standard)
- Exclusions (what's already public)
- Remedies (injunctive relief, not just damages)

## AI Tool Data Policies — Know What You're Agreeing To

| Tool | Trains on your data? | Notes |
|------|---------------------|-------|
| Anthropic API | ❌ No (by default) | Safe for proprietary content |
| Claude.ai (Free) | ✅ May be used | Don't paste proprietary system prompts here |
| Claude.ai (Pro) | ❌ No | Opt-out available |
| Make.com | Review ToS | Check enterprise data processing agreement |
| Zapier | Review ToS | Has enterprise DPA available |
| Vercel | ❌ No | Infrastructure only |
| Neon | ❌ No | Infrastructure only |

**Rule of thumb**: Always check the data processing agreement (DPA) before feeding proprietary content into any third-party AI tool.

## GitHub Repo Best Practices
- All production repos: **private by default**
- Never commit `.env` files (add to `.gitignore` from day one)
- Use branch protection on `main` — no direct pushes
- Archive repos of shipped apps instead of deleting them (preserves timestamp record)
