# Authentication & Access Reference

## Clerk-Specific Hardening

### MFA Enforcement
```javascript
// In your Clerk dashboard: Enable MFA under Security settings
// In code — require MFA for sensitive routes:
import { auth } from '@clerk/nextjs/server';

export async function GET() {
  const { userId, sessionClaims } = await auth();
  if (!sessionClaims?.mfa_enabled) {
    return new Response('MFA required', { status: 403 });
  }
}
```

### Session Expiration
- In Clerk Dashboard → Sessions → set token lifetime (recommend 24h for standard, 1h for sensitive apps)
- Never use infinite sessions for production apps

### RBAC Setup
```javascript
// Define roles in Clerk metadata
// In Clerk Dashboard → Users → set publicMetadata: { role: "admin" | "user" | "viewer" }

// Protect routes by role
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isAdminRoute = createRouteMatcher(['/admin(.*)']);

export default clerkMiddleware(async (auth, req) => {
  if (isAdminRoute(req)) {
    const { sessionClaims } = await auth();
    if (sessionClaims?.metadata?.role !== 'admin') {
      return new Response('Forbidden', { status: 403 });
    }
  }
});
```

### Common Mistakes
- Relying on frontend-only route protection (always enforce on the server)
- Not rotating Clerk secret keys after team member offboarding
- Using the same API key across dev and production environments
