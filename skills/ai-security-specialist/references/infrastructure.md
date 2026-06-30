# Infrastructure Security Reference

## Dependency Auditing

### Run a full audit
```bash
# Check for known vulnerabilities
npm audit

# Auto-fix low-risk issues
npm audit fix

# See what's outdated
npm outdated
```

### Interpreting results
- **Critical / High**: Fix immediately before going live
- **Moderate**: Fix within the week
- **Low**: Fix in your next maintenance pass
- If `npm audit fix` breaks things, address manually or pin the safe version

## Error Monitoring — Sentry Setup

### Install
```bash
npm install @sentry/nextjs
npx @sentry/wizard@latest -i nextjs
```

### Basic config (sentry.client.config.ts)
```javascript
import * as Sentry from '@sentry/nextjs';

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 0.1, // 10% of transactions for performance
  // Don't send PII to Sentry
  beforeSend(event) {
    if (event.user) {
      delete event.user.email; // Strip emails from error reports
    }
    return event;
  },
});
```

## Vercel Environment Variable Scoping

### Three environments in Vercel
- **Production**: Your live app (main branch)
- **Preview**: Pull request deployments
- **Development**: Local `vercel dev`

### Best practice
- Never share production secrets with preview environments
- Use separate API keys for prod vs. dev where possible
- Audit your Vercel env vars: Dashboard → Project → Settings → Environment Variables

## Serverless Function Timeouts

### Set in vercel.json
```json
{
  "functions": {
    "app/api/chat/route.ts": {
      "maxDuration": 30
    },
    "app/api/agent/route.ts": {
      "maxDuration": 60
    }
  }
}
```

- Default Vercel timeout: 10s (Hobby), 15s (Pro)
- AI agent routes often need 30–60s — set explicitly
- Infinite timeout = potential runaway costs if something loops

## Secrets in URLs — What to Avoid
```
❌ /api/data?userId=abc&apiKey=sk-123   ← shows in browser history and logs
✅ Pass sensitive data in request body (POST) or Authorization header
```

## Console.log in Production
```javascript
// Before going live, audit for exposed data:
// Search codebase for: console.log

// Replace sensitive logs with:
if (process.env.NODE_ENV === 'development') {
  console.log('Debug info:', data);
}

// Or use a proper logger that respects env:
import pino from 'pino';
const logger = pino({ level: process.env.LOG_LEVEL || 'info' });
```
