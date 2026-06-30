# API Security Reference

## Rate Limiting in Next.js / Vercel

### Using Upstash Redis (recommended for Vercel)
```bash
npm install @upstash/ratelimit @upstash/redis
```

```javascript
// lib/ratelimit.ts
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

export const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '10 s'), // 10 requests per 10 seconds
});

// In your API route:
export async function POST(req: Request) {
  const ip = req.headers.get('x-forwarded-for') ?? 'anonymous';
  const { success } = await ratelimit.limit(ip);
  if (!success) return new Response('Too Many Requests', { status: 429 });
  // ... rest of handler
}
```

## Input Validation

### Using Zod (recommended)
```bash
npm install zod
```

```javascript
import { z } from 'zod';

const InputSchema = z.object({
  message: z.string().min(1).max(1000).trim(),
  userId: z.string().uuid(),
});

export async function POST(req: Request) {
  const body = await req.json();
  const result = InputSchema.safeParse(body);
  if (!result.success) {
    return new Response('Invalid input', { status: 400 });
  }
  const { message, userId } = result.data;
  // Safe to use now
}
```

## Error Handling — Don't Leak Internals

```javascript
// ❌ Bad — exposes internals
catch (error) {
  return new Response(error.message, { status: 500 });
}

// ✅ Good — generic message, internal logging
catch (error) {
  console.error('[API Error]', error); // Log for you, not the user
  return new Response('Something went wrong', { status: 500 });
}
```

## HTTPS
Vercel enforces HTTPS automatically. Verify by:
- Checking that your Vercel domain shows a valid SSL certificate
- Adding HSTS headers in `next.config.js` for extra protection

## Common Mistakes
- No rate limiting on AI-powered routes (these are expensive to abuse)
- Trusting user-supplied IDs without validating against the authenticated session
- Returning full error objects (including stack traces) to the client
