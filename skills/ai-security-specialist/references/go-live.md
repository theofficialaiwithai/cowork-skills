# Go-Live Security Checklist Reference

## Pre-Launch Final Pass

### Environment Variables
```bash
# Verify all required env vars are set in Vercel production
vercel env ls --environment production

# Common ones to check:
# DATABASE_URL
# ANTHROPIC_API_KEY
# CLERK_SECRET_KEY
# NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY
# SUPABASE_SERVICE_ROLE_KEY (if used server-side)
# NEXT_PUBLIC_SUPABASE_URL
# NEXT_PUBLIC_SUPABASE_ANON_KEY
# SENTRY_DSN
```

### CORS Configuration
```javascript
// next.config.js
const nextConfig = {
  async headers() {
    return [
      {
        source: '/api/:path*',
        headers: [
          {
            key: 'Access-Control-Allow-Origin',
            value: process.env.NODE_ENV === 'production'
              ? 'https://yourdomain.com'  // Replace with your actual domain
              : '*',
          },
          { key: 'Access-Control-Allow-Methods', value: 'GET, POST, PUT, DELETE, OPTIONS' },
          { key: 'Access-Control-Allow-Headers', value: 'Content-Type, Authorization' },
        ],
      },
    ];
  },
};
```

### No Console.log with Sensitive Data
```bash
# Quick audit — search your codebase:
grep -r "console.log" ./app ./lib ./components | grep -v "node_modules"
# Review each one — remove or wrap in NODE_ENV check
```

### Authentication End-to-End Test
Run through manually before launch:
- [ ] New user can sign up
- [ ] User receives verification email
- [ ] Login works with correct credentials
- [ ] Wrong password is rejected cleanly (no info leak)
- [ ] Protected routes redirect unauthenticated users
- [ ] Logout clears session completely
- [ ] Admin routes are inaccessible to regular users

### Graceful Error Handling
```javascript
// Verify your global error boundary is set up
// app/error.tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <h2>Something went wrong.</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
  // Note: don't render error.message in production
}
```

### Production Agentic Workflow Test
Before going live, run your full agentic workflow once in production mode:
- [ ] Trigger the workflow as a real user would
- [ ] Check the audit log — did the action get recorded?
- [ ] Check the database — did the right data get written?
- [ ] Check error monitoring — did Sentry catch anything?
- [ ] Check that no sensitive data appeared in the response

## Post-Launch Security Habits
- Review Sentry errors weekly
- Run `npm audit` monthly
- Rotate API keys every 6 months or after any team change
- Review Vercel access logs if anything suspicious happens
- Check Clerk's security dashboard for unusual login patterns
